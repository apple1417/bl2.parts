from __future__ import annotations

import unrealsdk
import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Collection, Dict, Mapping, Optional, Set, Tuple, TypeVar, Union

from Mods.ModMenu import Game  # type: ignore

from . import YAML, float_error


@dataclass
class KnownStat:
    value: float
    multiplier_str: Optional[str] = None
    offset: float = 0

    def get_formula(self) -> YAML:
        formula: YAML = {}
        if self.multiplier_str:
            formula["multiplier_str"] = self.multiplier_str
        if self.offset:
            formula["offset"] = self.offset
        return formula


@dataclass
class ItemClassData:
    def_class: str
    part_class: str


@dataclass
class _PartTypeData:
    index: int
    name: str
    plural: str
    slot: str

    def title(self) -> str:
        return self.name.replace("_", " ").title()


class BasePartTypeEnum(Enum):
    value: _PartTypeData

    def __init__(self, *args: Any) -> None:
        if any(self.value.index == d.index for d in self.__class__):
            raise ValueError(f"Duplicate index {self.value.index} in {self.__class__.name}")

    @classmethod
    def from_index(cls, idx: int) -> BasePartTypeEnum:
        # Deliberately using a list + index 0 to force an IndexError
        return [d for d in cls if d.index == idx][0]

    @classmethod
    def from_plural(cls, plural: str) -> BasePartTypeEnum:
        val = next((x for x in cls if x.plural == plural), None)
        if val is None:
            raise ValueError(f"Couldn't find plural '{plural}'")
        return val

    def title(self) -> str:
        return self.value.title()

    @property
    def index(self) -> int:
        return self.value.index

    @property
    def name(self) -> str:
        return self.value.name

    @property
    def plural(self) -> str:
        return self.value.plural

    @property
    def slot(self) -> str:
        return self.value.slot


_T = TypeVar("_T")


def _load_obj_set(class_name: str, obj_names: Collection[str]) -> Set[unrealsdk.UObject]:
    """
    Given a class and a collection of object names, returns a set of all objects which are loaded.

    Args:
        class_name: The class name for the objects to try load.
        obj_names: A collection of object names to try load.
    Returns:
        A set of objects which were found.
    """
    all_objs = set()
    for name in obj_names:
        obj = unrealsdk.FindObject(class_name, name)
        if obj is not None:
            all_objs.add(obj)
    return all_objs


def _load_obj_dict(class_name: str, obj_data: Mapping[str, _T]) -> Dict[unrealsdk.UObject, _T]:
    """
    Given a class and a mapping of object names to some arbitrary data, returns a dict of all
     objects which are loaded to their relevant data.

    Args:
        class_name: The class name for the objects to try load.
        obj_data: A mapping of object names to try load to arbitrary data.
    Returns:
        A dict of objects which were found to their relevant data.
    """
    all_objs = {}
    for name, data in obj_data.items():
        obj = unrealsdk.FindObject(class_name, name)
        if obj is not None:
            all_objs[obj] = data
    return all_objs


BASE_SCALING_CONSTANT: str = "&beta;"


ALLOWED_DEFINITION_CLASSES: Tuple[str, ...] = (
    "ArtifactDefinition",
    "ClassModDefinition",
    "CrossDLCClassModDefinition",
    "GrenadeModDefinition",
    "ShieldDefinition",
    "WeaponTypeDefinition",
)

DEFINITION_BLACKLIST: Tuple[str, ...] = (
    "BuzzaxeWeaponTypeDefinition",
    "MissionItemDefinition",
    "TurretWeaponTypeDefinition",
    "UsableCustomizationItemDefinition",
    "UsableItemDefinition",
    "VehicleWeaponTypeDefinition",
)

"""
Maps item type to a set of definitions.
For weapons, this is all their definitions, including uniques.
For items, it's only their non unique definitions - we'll use classes from `ITEM_CLASS_OVERRIDES`
 to grab them instead.

Is this distinction a hacky confusing mess? Sure. Does it work? Kinda :)
"""
ALL_DEFINITIONS: Dict[str, Tuple[str, ...]] = {
    "grenade": (
        "GD_GrenadeMods.A_Item.GrenadeMod_Standard",
    ),
    "launcher": (
        "GD_Weap_Launchers.A_Weapons.WT_Bandit_Launcher",
        "GD_Weap_Launchers.A_Weapons.WT_Maliwan_Launcher",
        "GD_Weap_Launchers.A_Weapons.WT_Tediore_Launcher",
        "GD_Weap_Launchers.A_Weapons.WT_Torgue_Launcher",
        "GD_Weap_Launchers.A_Weapons.WT_Vladof_Launcher",
    ),
    "laser": (
        "GD_Cork_Weap_Lasers.A_Weapons.WT_Dahl_Laser",
        "GD_Cork_Weap_Lasers.A_Weapons.WT_Hyperion_Laser",
        "GD_Cork_Weap_Lasers.A_Weapons.WT_Maliwan_Laser",
        "GD_Cork_Weap_Lasers.A_Weapons.WT_Tediore_Laser",
    ),
    "pistol": (
        "GD_Weap_Pistol.A_Weapons.WeaponType_Bandit_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Dahl_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Hyperion_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Jakobs_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Maliwan_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Tediore_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Torgue_Pistol",
        "GD_Weap_Pistol.A_Weapons.WeaponType_Vladof_Pistol",
    ),
    "rifle": (
        "GD_Anemone_Weapons.AssaultRifle.PeakOpener.WT_PeakOpener",
        "GD_Weap_AssaultRifle.A_Weapons.WT_Bandit_AssaultRifle",
        "GD_Weap_AssaultRifle.A_Weapons.WT_Dahl_AssaultRifle",
        "GD_Weap_AssaultRifle.A_Weapons.WT_Jakobs_AssaultRifle",
        "GD_Weap_AssaultRifle.A_Weapons.WT_Torgue_AssaultRifle",
        "GD_Weap_AssaultRifle.A_Weapons.WT_Vladof_AssaultRifle",
    ),
    "shield": (
        "GD_Cork_Shields.A_Item.Shield_Nova_Ice",
        "GD_Cork_Shields.A_Item.Shield_Spike_Ice",
        "GD_Shields.A_Item.Shield_Absorption",
        "GD_Shields.A_Item.Shield_Booster",
        "GD_Shields.A_Item.Shield_Chimera",
        "GD_Shields.A_Item.Shield_Impact",
        "GD_Shields.A_Item.Shield_Juggernaut",
        "GD_Shields.A_Item.Shield_Nova_Corrosive",
        "GD_Shields.A_Item.Shield_Nova_Explosive",
        "GD_Shields.A_Item.Shield_Nova_Fire",
        "GD_Shields.A_Item.Shield_Nova_Shock",
        "GD_Shields.A_Item.Shield_Roid",
        "GD_Shields.A_Item.Shield_Spike_Corrosive",
        "GD_Shields.A_Item.Shield_Spike_Explosive",
        "GD_Shields.A_Item.Shield_Spike_Fire",
        "GD_Shields.A_Item.Shield_Spike_Shock",
        "GD_Shields.A_Item.Shield_Standard",
    ),
    "shotgun": (
        "GD_Weap_Shotgun.A_Weapons.WT_Bandit_Shotgun",
        "GD_Weap_Shotgun.A_Weapons.WT_Hyperion_Shotgun",
        "GD_Weap_Shotgun.A_Weapons.WT_Jakobs_Shotgun",
        "GD_Weap_Shotgun.A_Weapons.WT_Tediore_Shotgun",
        "GD_Weap_Shotgun.A_Weapons.WT_Torgue_Shotgun",
    ),
    "smg": (
        "GD_Weap_SMG.A_Weapons.WT_SMG_Bandit",
        "GD_Weap_SMG.A_Weapons.WT_SMG_Dahl",
        "GD_Weap_SMG.A_Weapons.WT_SMG_Hyperion",
        "GD_Weap_SMG.A_Weapons.WT_SMG_Maliwan",
        "GD_Weap_SMG.A_Weapons.WT_SMG_Tediore",
    ),
    "sniper": (
        "GD_Weap_SniperRifles.A_Weapons.WeaponType_Dahl_Sniper",
        "GD_Weap_SniperRifles.A_Weapons.WeaponType_Hyperion_Sniper",
        "GD_Weap_SniperRifles.A_Weapons.WeaponType_Jakobs_Sniper",
        "GD_Weap_SniperRifles.A_Weapons.WeaponType_Maliwan_Sniper",
        "GD_Weap_SniperRifles.A_Weapons.WeaponType_Vladof_Sniper",
        "GD_Anemone_Weap_SniperRifles.A_Weapons.WeaponType_Jakobs_Sniper",
    )
}

UNIQUE_WEAPON_DEFINITIONS: Set[unrealsdk.UObject] = _load_obj_set("WeaponTypeDefinition", {
    "GD_Anemone_Weapons.AssaultRifle.PeakOpener.WT_PeakOpener",
    "GD_Anemone_Weap_SniperRifles.A_Weapons.WeaponType_Jakobs_Sniper"
})

ITEM_CLASS_OVERRIDES: Dict[str, ItemClassData] = {
    "grenade": ItemClassData("GrenadeModDefinition", "GrenadeModPartDefinition"),
    "shield": ItemClassData("ShieldDefinition", "ShieldPartDefinition"),
}

NON_UNIQUE_BALANCES: Dict[str, Tuple[str, ...]] = {
    "grenade": tuple(
        obj_start + suffix
        for obj_start in (
            "GD_GrenadeMods.A_Item.GM_AreaEffect",
            "GD_GrenadeMods.A_Item.GM_BouncingBetty",
            "GD_GrenadeMods.A_Item.GM_Mirv",
            "GD_GrenadeMods.A_Item.GM_Singularity",
            "GD_GrenadeMods.A_Item.GM_Standard",
            "GD_GrenadeMods.A_Item.GM_Transfusion",
        )
        for suffix in ("", "_2_Uncommon", "_3_Rare", "_4_VeryRare")
    ),
    "laser": (
        "GD_Cork_Weap_Lasers.A_Weapons.Laser_Dahl_4_VeryRare",
        "GD_Cork_Weap_Lasers.A_Weapons.Laser_Hyperion_4_VeryRare",
        "GD_Cork_Weap_Lasers.A_Weapons.Laser_Maliwan_4_VeryRare",
        "GD_Cork_Weap_Lasers.A_Weapons.Laser_Old_Hyperion_4_VeryRar",
        "GD_Cork_Weap_Lasers.A_Weapons.Laser_Tediore_4_VeryRare",
        "GD_Ma_Weapons.A_Weapons.Laser_Dahl_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Laser_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Laser_Maliwan_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Laser_Tediore_6_Glitch",
    ),
    "launcher": (
        "GD_Ma_Weapons.A_Weapons.RL_Bandit_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.RL_Maliwan_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.RL_Tediore_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.RL_Torgue_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.RL_Vladof_6_Glitch",
        "GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare",
        "GD_Weap_Launchers.A_Weapons.RL_Bandit_5_Alien",
        "GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare",
        "GD_Weap_Launchers.A_Weapons.RL_Maliwan_5_Alien",
        "GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare",
        "GD_Weap_Launchers.A_Weapons.RL_Tediore_5_Alien",
        "GD_Weap_Launchers.A_Weapons.RL_Torgue_4_VeryRare",
        "GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare",
        "GD_Weap_Launchers.A_Weapons.RL_Vladof_5_Alien",
    ),
    "pistol": (
        "GD_Aster_Weapons.Pistols.Pistol_Bandit_4_Quartz",
        "GD_Aster_Weapons.Pistols.Pistol_Dahl_4_Emerald",
        "GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond",
        "GD_Aster_Weapons.Pistols.Pistol_Jakobs_4_Citrine",
        "GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine",
        "GD_Aster_Weapons.Pistols.Pistol_Tediore_4_CubicZerconia",
        "GD_Aster_Weapons.Pistols.Pistol_Torgue_4_Rock",
        "GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet",
        "GD_Ma_Weapons.A_Weapons.Pistol_Bandit_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Dahl_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Jakobs_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Maliwan_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Old_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Tediore_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Torgue_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Pistol_Vladof_6_Glitch",
        "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_5_Alien",
        "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_5_Alien",
        "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_5_Alien",
        "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_5_Alien",
        "GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_2_Uncommon",
        "GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_3_Rare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Old_Hyperion",
        "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_5_Alien",
        "GD_Weap_Pistol.A_Weapons.Pistol_Torgue_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare",
        "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_5_Alien",
    ),
    "rifle": (
        "GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz",
        "GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald",
        "GD_Aster_Weapons.AssaultRifles.AR_Jakobs_4_Citrine",
        "GD_Aster_Weapons.AssaultRifles.AR_Torgue_4_Rock",
        "GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet",
        "GD_Ma_Weapons.A_Weapons.AR_Bandit_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.AR_Dahl_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.AR_Jakobs_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.AR_Torgue_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.AR_Vladof_6_Glitch",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_5_Alien",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_5_Alien",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_4_VeryRare",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_4_VeryRare",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare",
        "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_5_Alien",
    ),
    "shield": tuple([
        "GD_Cork_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Ice_01_Common",
        "GD_Cork_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Ice_02_Uncommon",
        "GD_Cork_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Ice_03_Rare",
        # There is no very rare ¯\_(ツ)_/¯
    ] + [
        obj_start + suffix
        for obj_start in (
            "GD_Cork_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Ice_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_",
            "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_",
        )
        for suffix in ("01_Common", "02_Uncommon", "03_Rare", "04_VeryRare")
    ]),
    "shotgun": (
        "GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz",
        "GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond",
        "GD_Aster_Weapons.Shotguns.SG_Jakobs_4_Citrine",
        "GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia",
        "GD_Aster_Weapons.Shotguns.SG_Torgue_4_Rock",
        "GD_Ma_Weapons.A_Weapons.SG_Bandit_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SG_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SG_Jakobs_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SG_Old_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SG_Tediore_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SG_Torgue_6_Glitch",
        "GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare",
        "GD_Weap_Shotgun.A_Weapons.SG_Bandit_5_Alien",
        "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare",
        "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_5_Alien",
        "GD_Weap_Shotgun.A_Weapons.SG_Jakobs_4_VeryRare",
        "GD_Weap_Shotgun.A_Weapons.SG_Old_Hyperion_4_VeryRare",
        "GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare",
        "GD_Weap_Shotgun.A_Weapons.SG_Tediore_5_Alien",
        "GD_Weap_Shotgun.A_Weapons.SG_Torgue_4_VeryRare",
    ),
    "smg": (
        "GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz",
        "GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald",
        "GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond",
        "GD_Aster_Weapons.SMGs.SMG_Maliwan_4_Aquamarine",
        "GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia",
        "GD_Ma_Weapons.A_Weapons.SMG_Bandit_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SMG_Dahl_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SMG_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SMG_Maliwan_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SMG_Old_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.SMG_Tediore_6_Glitch",
        "GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Bandit_5_Alien",
        "GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Dahl_5_Alien",
        "GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Hyperion_5_Alien",
        "GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Maliwan_5_Alien",
        "GD_Weap_SMG.A_Weapons.SMG_Old_Hyperion_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare",
        "GD_Weap_SMG.A_Weapons.SMG_Tediore_5_Alien",
    ),
    "sniper": (
        "GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald",
        "GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond",
        "GD_Aster_Weapons.Snipers.SR_Jakobs_4_Citrine",
        "GD_Aster_Weapons.Snipers.SR_Maliwan_4_Aquamarine",
        "GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet",
        "GD_Ma_Weapons.A_Weapons.Sniper_Dahl_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Sniper_Hyperion_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Sniper_Jakobs_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Sniper_Maliwan_6_Glitch",
        "GD_Ma_Weapons.A_Weapons.Sniper_Vladof_6_Glitch",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_5_Alien",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_5_Alien",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_5_Alien",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Old_Hyperion_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare",
        "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_5_Alien",
    ),
}

ITEM_TYPE_IGNORES: Dict[Game, Tuple[str, ...]] = {
    Game.BL2: (
        "laser",
    ),
}

MODIFIER_NAMES: Tuple[str, ...] = (
    "scale",
    "pre-add",
    "post-add"
)


# Probably should have a better way of doing this ¯\_(ツ)_/¯
class GenericPartType(BasePartTypeEnum):
    Definition: _PartTypeData = _PartTypeData(-9999, "Definition", "definitions", "")


class WeaponPartType(BasePartTypeEnum):
    Body: _PartTypeData = _PartTypeData(0, "Body", "bodies", "BodyPartData")
    Grip: _PartTypeData = _PartTypeData(1, "Grip", "grips", "GripPartData")
    Barrel: _PartTypeData = _PartTypeData(2, "Barrel", "barrels", "BarrelPartData")
    Sight: _PartTypeData = _PartTypeData(3, "Sight", "sights", "SightPartData")
    Stock: _PartTypeData = _PartTypeData(4, "Stock", "stocks", "StockPartData")
    Element: _PartTypeData = _PartTypeData(5, "Element", "elements", "ElementalPartData")
    Accessory: _PartTypeData = _PartTypeData(6, "Accessory", "accessories", "Accessory1PartData")
    AltAccessory: _PartTypeData = _PartTypeData(7, "Alt Accessory", "alt_accessories", "Accessory2PartData")
    Material: _PartTypeData = _PartTypeData(8, "Material", "materials", "MaterialPartData")


class ItemPartType(BasePartTypeEnum):
    Alpha: _PartTypeData = _PartTypeData(0, "Alpha", "alpha", "AlphaPartData")
    Beta: _PartTypeData = _PartTypeData(1, "Beta", "beta", "BetaPartData")
    Gamma: _PartTypeData = _PartTypeData(2, "Gamma", "gamma", "GammaPartData")
    Delta: _PartTypeData = _PartTypeData(3, "Delta", "delta", "DeltaPartData")
    Epsilon: _PartTypeData = _PartTypeData(4, "Epsilon", "epsilon", "EpsilonPartData")
    Zeta: _PartTypeData = _PartTypeData(5, "Zeta", "zeta", "ZetaPartData")
    Eta: _PartTypeData = _PartTypeData(6, "Eta", "eta", "EtaPartData")
    Theta: _PartTypeData = _PartTypeData(7, "Theta", "theta", "ThetaPartData")
    Material: _PartTypeData = _PartTypeData(8, "Material", "material", "MaterialPartData")

    def get_def_slot(self) -> str:
        definition_slots: Tuple[str, ...] = (
            "AlphaParts",
            "BetaParts",
            "GammaParts",
            "DeltaParts",
            "EpsilonParts",
            "ZetaParts",
            "EtaParts",
            "ThetaParts",
            "MaterialParts",
        )
        return definition_slots[self.index]


def part_type_from_plural(plural: str) -> BasePartTypeEnum:
    """
    Given a part type plural, return it's corosponding part type enum value.

    Args:
        plural: The plural to look up.
    Returns:
        The part type enum where the plural came from.
    """
    try:
        return GenericPartType.from_plural(plural)
    except ValueError:
        try:
            return WeaponPartType.from_plural(plural)
        except ValueError:
            return ItemPartType.from_plural(plural)


PART_LIST_SLOTS: Tuple[str, ...] = (
    "RuntimePartListCollection",
    "PartListCollection"
)

PART_TYPE_OVERRIDES: Dict[str, BasePartTypeEnum] = {
    "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Dahl": WeaponPartType.Stock,
    "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Hyperion": WeaponPartType.Stock,
    "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Jakobs": WeaponPartType.Stock,
    "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Maliwan": WeaponPartType.Stock,
    "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Vladof": WeaponPartType.Stock,
    "GD_Anemone_Weapons.Rocket_Launcher.WorldBurn.L_Barrel_Torgue_WorldBurn": WeaponPartType.Barrel,
    "GD_Anemone_Weapons.Shotguns.SG_Barrel_Alien_Swordsplosion": WeaponPartType.Barrel,
    "GD_Cork_Weap_Lasers.Accessory.Laser_Accessory_Rosie_Thorns": WeaponPartType.Accessory,
    "GD_Cork_Weap_Shotgun.Stock.SG_Stock_Jakobs_Boomacorn": WeaponPartType.Stock,
    "GD_Cork_Weap_Shotgun.Stock.SG_Stock_Jakobs_TooScoops": WeaponPartType.Stock,
    "GD_Cork_Weap_SMG.Sight.SMG_Sight_Hyperion_BlackSnake": WeaponPartType.Sight,
    "GD_Orchid_BossWeapons.AssaultRifle.AR_Accessory_Bayonet_Rapier": WeaponPartType.AltAccessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_1": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_2": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_None": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize": WeaponPartType.Accessory,
    "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy": WeaponPartType.Accessory,
    "GD_Weap_Launchers.Exhaust.L_Exhaust_Bandit": WeaponPartType.Stock,
    "GD_Weap_Launchers.Exhaust.L_Exhaust_Maliwan": WeaponPartType.Stock,
    "GD_Weap_Launchers.Exhaust.L_Exhaust_Tediore": WeaponPartType.Stock,
    "GD_Weap_Launchers.Exhaust.L_Exhaust_Torgue": WeaponPartType.Stock,
    "GD_Weap_Launchers.Exhaust.L_Exhaust_Vladof": WeaponPartType.Stock,
    "GD_Weap_Shotgun.Stock.SG_Stock_Bandit": WeaponPartType.Stock,
    "GD_Weap_Shotgun.Stock.SG_Stock_Hyperion": WeaponPartType.Stock,
    "GD_Weap_Shotgun.Stock.SG_Stock_Jakobs": WeaponPartType.Stock,
    "GD_Weap_Shotgun.Stock.SG_Stock_Tediore": WeaponPartType.Stock,
    "GD_Weap_Shotgun.Stock.SG_Stock_Torgue": WeaponPartType.Stock,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_1": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_2": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_None": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized": WeaponPartType.Accessory,
    "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload": WeaponPartType.Accessory,
    "GD_Weap_SMG.Sight.SMG_Sight_Bandit": WeaponPartType.Sight,
    "GD_Weap_SMG.Sight.SMG_Sight_Dahl": WeaponPartType.Sight,
    "GD_Weap_SMG.Sight.SMG_Sight_Hyperion": WeaponPartType.Sight,
    "GD_Weap_SMG.Sight.SMG_Sight_Maliwan": WeaponPartType.Sight,
    "GD_Weap_SMG.Sight.SMG_Sight_None": WeaponPartType.Sight,
    "GD_Weap_SMG.Sight.SMG_Sight_Tedior": WeaponPartType.Sight,
    "GD_Weap_SniperRifles.Stock.SR_Stock_Dahl": WeaponPartType.Stock,
    "GD_Weap_SniperRifles.Stock.SR_Stock_Hyperion": WeaponPartType.Stock,
    "GD_Weap_SniperRifles.Stock.SR_Stock_Jakobs": WeaponPartType.Stock,
    "GD_Weap_SniperRifles.Stock.SR_Stock_Maliwan": WeaponPartType.Stock,
    "GD_Weap_SniperRifles.Stock.SR_Stock_Vladof": WeaponPartType.Stock,
}

"""
Dict of:
```
"<obj name>": {
    "name": "<name>",
    "game_overrides": {
        "<game>": "<name>"
    }
    "type": "<weapon type>",
    "slot": "<part slot>",
}
```

`game_overrides` is optional if not needed.
"""
PART_NAMES: Dict[str, Dict[str, Union[str, Dict[str, str]]]]

with open("Mods/bl2parts/part_names.json") as file:
    PART_NAMES = json.load(file)


WEAPON_MANU_ATTRIBUTES: Dict[unrealsdk.UObject, str] = _load_obj_dict("AttributeDefinitionBase", {
    "D_Attributes.WeaponManufacturer.Weapon_Is_Bandit": "Bandit",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Dahl": "Dahl",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Hyperion_Old": "Old Hyperion",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Hyperion": "Hyperion",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Jakobs": "Jakobs",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Maliwan": "Maliwan",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Tediore": "Tediore",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Torgue": "Torgue",
    "D_Attributes.WeaponManufacturer.Weapon_Is_Vladof": "Vladof",
})

KNOWN_ATTRIBUTES: Dict[unrealsdk.UObject, KnownStat] = _load_obj_dict("AttributeDefinitionBase", {
    "D_Attributes.ExperienceResourcePool.PlayerExperienceLevel": KnownStat(1, "[Player Level]"),
})

# `ConstantAttributeValueResolver`s
for _obj_name in (
    "GD_Anemone_Shields.Misc.Att_UniversalShieldBaseDelayConstant",
    "GD_Shields.Misc.Att_Shield_BaseExplosiveDamageResistance",
    "GD_Shields.Misc.Att_UniversalShieldBaseDelayConstant",
    "GD_Orchid_Shields.Attributes.Attr_BladeElementalDamageModifier",
):
    _obj = unrealsdk.FindObject("AttributeDefinitionBase", _obj_name)
    if _obj is None:
        continue
    KNOWN_ATTRIBUTES[_obj] = KnownStat(float_error(_obj.ValueResolverChain[0].ConstantValue))

# `DesignerAttributeDefinition`s`
for _obj_name in (
    "GD_Shields.Misc.Att_ShieldResistance_Base",
    "GD_Shields.Misc.Att_ShieldResistance_PerGradeUpgrade",
    "GD_Shields.Misc.Att_UniversalShieldBaseDelay",  # The onther one has `Constant` at the end
):
    _obj = unrealsdk.FindObject("DesignerAttributeDefinition", _obj_name)
    if _obj is None:
        continue
    KNOWN_ATTRIBUTES[_obj] = KnownStat(float_error(
        _obj.BaseValue.BaseValueConstant * _obj.BaseValue.BaseValueScaleConstant
    ))


KNOWN_INITALIZATIONS: Dict[unrealsdk.UObject, KnownStat] = _load_obj_dict("AttributeInitializationDefinition", {
    "GD_Aster_Shields.Misc.Init_Blockade_Resistance_Minor": KnownStat(-0.005, "[Shield Level]", -0.075),
    # Used for the prismatic bulwark - this is not at all how it actually calculates it, but it's
    #  equivalent, and it makes it a lot easier having this in the same format as everything else
    "GD_Shields.Misc.Init_StatBonus_Medium": KnownStat(0.0045, "[Shield Level]", 0.12),
})

# Scaling * multiplier
for _obj_name in (
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_GrenadeModDamage",
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_GrenadeModStatusEffectDamage",
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_ProjectileDamage",
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_ShieldDamage",
):
    _obj = unrealsdk.FindObject("AttributeInitializationDefinition", _obj_name)
    if _obj is None:
        continue
    KNOWN_INITALIZATIONS[_obj] = KnownStat(
        float_error(
            _obj.ValueFormula.Multiplier.BaseValueConstant
            * _obj.ValueFormula.Multiplier.BaseValueScaleConstant
        ),
        BASE_SCALING_CONSTANT
    )

# Scaling * a `ConstantAttributeValueResolver` in multiplier
for _obj_name in (
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_HealthBonusFromShields_Formula",
    "GD_Balance_HealthAndDamage.Shields.Init_ShieldItem_CapacityMaxValue",
):
    _obj = unrealsdk.FindObject("AttributeInitializationDefinition", _obj_name)
    if _obj is None:
        continue
    KNOWN_INITALIZATIONS[_obj] = KnownStat(
        float_error(
            _obj.ValueFormula.Multiplier.BaseValueAttribute.ValueResolverChain[0].ConstantValue
            * _obj.ValueFormula.Multiplier.BaseValueScaleConstant
        ),
        BASE_SCALING_CONSTANT
    )

_regen_obj = unrealsdk.FindObject(
    "AttributeInitializationDefinition",
    "GD_Balance_HealthAndDamage.Shields.Init_ShieldItem_BaseRegenRatePercentage"
)
_capacity_obj = next(filter(
    lambda obj: obj.Name == "Init_ShieldItem_CapacityMaxValue",
    KNOWN_INITALIZATIONS.keys()
))
assert _regen_obj.ValueFormula.Multiplier.InitializationDefinition == _capacity_obj
KNOWN_INITALIZATIONS[_regen_obj] = KnownStat(
    float_error(
        KNOWN_INITALIZATIONS[_capacity_obj].value
        * _regen_obj.ValueFormula.Multiplier.BaseValueScaleConstant
        * _regen_obj.ValueFormula.Level.BaseValueConstant
        * _regen_obj.ValueFormula.Level.BaseValueScaleConstant
    ),
    BASE_SCALING_CONSTANT
)


MOONSTONE_PARTS: Set[unrealsdk.UObject] = _load_obj_set("WeaponPartDefinition", (
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Boominator",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_FastLearner",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_HardenUp",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_None",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Oxygenator",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_PiercingRounds",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Punisher",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Safeguard",
    "GD_Weap_Accessories.Moonstone.Moonstone_Attachment_Serenity",
))


GLITCH_PARTS: Set[unrealsdk.UObject] = _load_obj_set("WeaponPartDefinition", (
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0044",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0324",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0341",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0404",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0421",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_0440",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_1034",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_1042",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_1432",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_2104",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_2143",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_2403",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_3214",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_3240",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_3410",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4004",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4032",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4040",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4103",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4210",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4321",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4400",
    "GD_Ma_Weapons.Glitch_Attachments.Glitch_Attachment_4444",
))


CONSTRAINT_NAMES: Dict[unrealsdk.UObject, str] = _load_obj_dict("AttributeDefinitionBase", {
    "D_Attributes.GrenadeMod.GrenadeModIsIncendiary": "Fire",
    "D_Attributes.GrenadeMod.GrenadeModIsCorrosive": "Corrosive",
    "D_Attributes.GrenadeMod.GrenadeModIsShock": "Shock",
    "D_Attributes.GrenadeMod.GrenadeModIsSlag": "Slag",
    "D_Attributes.GrenadeMod.GrenadeModIsIce": "Cryo",
    "D_Attributes.WeaponType.Weapon_Is_Laser": "Laser",
})


IGNORED_POST_INIT_PARTS: Set[unrealsdk.UObject] = _load_obj_set("WeaponPartDefinition", (
    "GD_Weap_Shotgun.Barrel.SG_Barrel_Jakobs_RockSalt",
))


# These are split by part class to make unintentional conflicts a bit less likely
ATTRIBUTES_TO_IGNORE: Dict[str, Set[unrealsdk.UObject]] = {
    "ShieldPartDefinition": _load_obj_set("AttributeDefinitionBase", {
        # These are just duplicates of the grades that already exist, only used for naming
        "D_Attributes.Shield.ShieldCapacitySlotGradeMinusRarity",
        "D_Attributes.Shield.ShieldRechargeRateSlotGradeMinusRarity",
        "D_Attributes.Shield.ShieldRechargeDelaySlotGradeMinusRarity",
        "D_Attributes.Shield.ShieldSpecialSlotGradeMinusRarity",
    }),
    "ShieldDefinition": _load_obj_set("AttributeDefinitionBase", {
        # This just straight up does nothing
        "GD_Shields.Misc.Att_BoosterShield_IEDDamage",
    })
}

GRADES_TO_IGNORE: Dict[str, Tuple[str, ...]] = {
    "ShieldDefinition": (
        # This never does anything, but is based on the base shield scaling, so keeping it causes a
        #  tonne of conflicts when merging the games
        "MaxHealth",
    ),
    "ShieldPartDefinition": (
        # This is defined with a valid value on most shields, but the only places that provide a
        #  bonus to it are shield definitions which don't define it, so it never does anything
        "MaxHealth",
        # These fields (only on maliwan battery) don't use the right slot name, so don't trigger the
        #  intended effects
        "CorrosiveImpactResistance",
        "CorrosivePassiveResistance",
        "IncendiaryImpactResistance",
        "IncendiaryPassiveResistance",
        "ShockImpactResistance",
        "ShockPassiveResistance",
        # This one is only on a maliwan battery again, and this time leads to a valid slot, but it's
        #  to a completely useless attribute, and it doesn't actually have a value, it's always 0
        "ExplosiveDamageResistance",
    )
}

# This will add +0 grades only *if* they also activate the slot
# These are generally for slots done entirely within the base value
ALLOWED_ZERO_GRADES: Dict[str, Tuple[str, ...]] = {
    "ShieldDefinition": (
        # Used by the Antagonist
        "DeflectChance",
        # Used by the blockage, for it's damage reduction
        "NormalDamageResist",
        "FireDamageResist",
        "ShockDamageResist",
        "CorrosiveDamageResist",
        "ExplosiveDamageResist",
        "SlagDamageResist",
    ),
    "ShieldPartDefinition": (
        # Used by the maliwan capacitors
        "FireResist",
        "ShockResist",
        "CorrosiveResist",
        "IceResist",
    )
}

MESH_OVERRIDES: Dict[unrealsdk.UObject, str] = _load_obj_dict("WillowInventoryPartDefinition", {
    "GD_Cork_Weap_Lasers.Accessory.Laser_Accessory_Rosie_Thorns": "Acc_Body_2",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate": "Acc_Body_1",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage": "Acc_Body_2",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated": "Acc_Body_3",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized": "Acc_Stock_1",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload": "Acc_Stock_2",
    "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload": "Acc_Stock_2",
})
