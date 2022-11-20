import unrealsdk
from typing import Dict

from Mods.ModMenu import Game  # type: ignore

from . import YAML, float_error
from .data import (ATTRIBUTES_TO_IGNORE, BASE_SCALING_CONSTANT, CONSTRAINT_NAMES, GRADES_TO_IGNORE,
                   KNOWN_ATTRIBUTES, KNOWN_INITALIZATIONS, MODIFIER_NAMES, PART_NAMES)

WEAPON_DAMAGE_INIT: unrealsdk.UObject = unrealsdk.FindObject(
    "AttributeInitializationDefinition",
    "GD_Balance_HealthAndDamage.HealthAndDamage.Init_WeaponDamage"
)

WEAPON_DAMAGE_ATTR: str = "D_Attributes.Weapon.WeaponDamage"
STATUS_CHANCE_ATTR: str = "D_Attributes.Weapon.WeaponBaseStatusEffectChanceModifier"
STATUS_DAMAGE_ATTR: str = "D_Attributes.Weapon.WeaponStatusEffectDamage"

SIMPLE_WEAPON_BASE_VALUES: Dict[str, str] = {
    "BurstInterval": "D_Attributes.Weapon.WeaponBurstInterval",
    "BurstShotAccuracyImpulseScale": "D_Attributes.Weapon.WeaponBurstShotAccuracyImpulseScale",
    "ClipSize": "D_Attributes.Weapon.WeaponClipSize",
    "FireRate": "D_Attributes.Weapon.WeaponFireInterval",
    "PerShotAccuracyImpulse": "D_Attributes.Weapon.WeaponPerShotAccuracyImpulse",
    "ProjectilesPerShot": "D_Attributes.Weapon.WeaponProjectilesPerShot",
    "ReloadTime": "D_Attributes.Weapon.WeaponReloadSpeed",
    "ShotCost": "D_Attributes.Weapon.WeaponShotCost",
    "Spread": "D_Attributes.Weapon.WeaponSpread",
    "ZoomedEndFOV": "D_Attributes.Weapon.WeaponZoomEndFOV",
}


def get_definition_data(def_obj: unrealsdk.UObject) -> YAML:
    """
    Gets data about the provided definition.

    Args:
        def_obj: The definition object to process
    Returns:
        YAML data describing the definition
    """

    def_name = def_obj.PathName(def_obj)

    friendly_name: str
    if def_name in PART_NAMES:
        name_data = PART_NAMES[def_name]
        override = name_data.get("game_overrides", {}).get(Game.GetCurrent()._name_)  # type: ignore

        friendly_name = override if override is not None else name_data["name"]  # type: ignore
    else:
        friendly_name = def_name.split(".")[-1]

    data = {
        "_obj_name": def_name,
        "name": friendly_name,
        "base": []
    }

    if def_obj.Class.Name == "WeaponTypeDefinition":
        for field, attr in sorted(SIMPLE_WEAPON_BASE_VALUES.items()):
            data["base"].append({
                "attribute": attr,
                "value": float_error(getattr(def_obj, field))
            })

        assert def_obj.InstantHitDamage.BaseValueAttribute is None
        assert def_obj.InstantHitDamage.InitializationDefinition == WEAPON_DAMAGE_INIT
        assert def_obj.StatusEffectDamage.BaseValueAttribute is None
        assert def_obj.StatusEffectDamage.InitializationDefinition == WEAPON_DAMAGE_INIT
        assert def_obj.BaseStatusEffectChanceModifier.BaseValueAttribute is None
        assert def_obj.BaseStatusEffectChanceModifier.InitializationDefinition is None

        data["base"].append({
            "attribute": WEAPON_DAMAGE_ATTR,
            "value": float_error(8 * def_obj.InstantHitDamage.BaseValueScaleConstant),
            "value_formula": {
                "multiplier_str": BASE_SCALING_CONSTANT,
            }
        })
        data["base"].append({
            "attribute": STATUS_DAMAGE_ATTR,
            "value": float_error(8 * def_obj.StatusEffectDamage.BaseValueScaleConstant),
            "value_formula": {
                "multiplier_str": BASE_SCALING_CONSTANT,
            }
        })
        data["base"].append({
            "attribute": STATUS_CHANCE_ATTR,
            "value": float_error(
                def_obj.BaseStatusEffectChanceModifier.BaseValueConstant
                * def_obj.BaseStatusEffectChanceModifier.BaseValueScaleConstant
            ),
        })

    grades = []
    for idx, slot in enumerate(def_obj.AttributeSlotEffects):
        if (
            slot.AttributeToModify is None
            or slot.AttributeToModify in ATTRIBUTES_TO_IGNORE.get(def_obj.Class.Name, ())
        ):
            continue

        if slot.SlotName in GRADES_TO_IGNORE.get(def_obj.Class.Name, ()):
            continue

        grade_data = {
            "slot": slot.SlotName,
            "attribute": def_obj.PathName(slot.AttributeToModify),
            "type": MODIFIER_NAMES[slot.ModifierType],
        }

        if slot.ConstraintAttribute:
            if slot.ConstraintAttribute not in CONSTRAINT_NAMES:
                constraint_name = def_obj.PathName(slot.ConstraintAttribute)
                unrealsdk.Log(f"Unknown constraint '{constraint_name}' on '{def_name}'")
                grade_data["constraint"] = constraint_name
            else:
                grade_data["constraint"] = CONSTRAINT_NAMES[slot.ConstraintAttribute]

        for value_key, bvc_struct in (
            ("base", slot.BaseModifierValue),
            ("per_grade", slot.PerGradeUpgrade),
        ):
            attr = bvc_struct.BaseValueAttribute
            init = bvc_struct.InitializationDefinition

            if attr is None and init is None:
                grade_data[value_key] = float_error(
                    bvc_struct.BaseValueConstant * bvc_struct.BaseValueScaleConstant
                )

            elif (
                (attr in KNOWN_ATTRIBUTES and init is None)
                or (attr is None and init in KNOWN_INITALIZATIONS)
            ):
                stat_data = KNOWN_INITALIZATIONS[init] if attr is None else KNOWN_ATTRIBUTES[attr]

                grade_data[value_key] = float_error(
                    stat_data.value * bvc_struct.BaseValueScaleConstant
                )

                formula = stat_data.get_formula()
                if formula:
                    grade_data[value_key + "_formula"] = formula

            else:
                unrealsdk.Log(f"Unparseable grade {value_key} in index {idx} of '{def_name}'")
                continue

        grades.append(grade_data)

    data["grades"] = grades

    return data
