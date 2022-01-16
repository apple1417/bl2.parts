---
part_reference:
  - name: Accessory
    src: /pistols/^images/parts/accessory.png
  - name: Barrel
    src: /pistols/^images/parts/barrel.png
  - name: Body
    src: /pistols/^images/parts/body.png
  - name: Grip
    src: /pistols/^images/parts/grip.png
  - name: Sight
    src: /pistols/^images/parts/sight.png

accessory_overrides:
  - idx: 2
    footnote: same_laser_model
  - idx: 5
    footnote: same_laser_model
    bonus_block:
      - group_idx: 1
        overrides:
          - idx: 3
            footnote: different_times
          - idx: 4
            footnote: different_times
          - idx: 6
            footnote: different_times
          - idx: 7
            footnote: different_times
          - idx: 10
            footnote: different_times
          - idx: 11
            footnote: different_times

barrel_overrides:
  - idx: 3
    footnote: same_model
  - idx: 4
    footnote: same_model
  - idx: 10
    bonus_block:
      - group_idx: 2
        overrides:
          - idx: 1
            footnote: spin_up
            replace:
              from: class="bad"
              to: ""
      - group_idx: 4
        overrides:
          - idx: 1
            footnote: spin_up
            replace:
              from: class="good"
              to: ""

body_names:
 - GD_Weap_Pistol.Body.Pistol_Body_Bandit
 - GD_Weap_Pistol.Body.Pistol_Body_Dahl
 - GD_Weap_Pistol.Body.Pistol_Body_Hyperion
 - GD_Weap_Pistol.Body.Pistol_Body_Jakobs
 - GD_Weap_Pistol.Body.Pistol_Body_Maliwan
 - GD_Weap_Pistol.Body.Pistol_Body_Tediore
 - GD_Weap_Pistol.Body.Pistol_Body_Torgue
 - GD_Weap_Pistol.Body.Pistol_Body_Vladof

body_overrides:
  - idx: 1
    name: Bandit
  - idx: 2
    name: Dahl
  - idx: 3
    name: Hyperion
  - idx: 4
    name: Jakobs
  - idx: 5
    name: Maliwan
  - idx: 6
    name: Tediore
  - idx: 7
    name: Torgue
  - idx: 8
    name: Vladof

special_body_names:
 - GD_Weap_Pistol.Body.Pistol_Body_Bandit_2
 - GD_Weap_Pistol.Body.Pistol_Body_Bandit_4


---

# Pistol Parts Guide
Pistols are made out of 5 main visible parts.

<style>
#part_reference {
    width: 80%;
    margin: auto;
}
</style>
{% include part_reference.html
    id="part_reference"
    parts=page.part_reference
    image_class="big"
%}

## Accessory
There are 9 non-unique accessories, including a "no accessory" part with no model.

<style>
</style>
{% include parts.html 
    parts=site.data.pistols.accessories
    meta=site.data.pistols.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.accessory_overrides
%}
{% include footnote_end.html
    same_laser_model=" While these have the same model in your inventory, the Accuracy Laser part has an actual laser coming out of its model in game ([comparison](/pistols/^images/accessories/laser_comp.png))."
    different_times="The bonuses in each pair are applied at different times of the calculation."
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has.

<style>
    #prefixes table {
        margin-left: -5%;
        width: 110%;
    }
</style>
{% include prefixes.html parts=site.data.pistols.accessories id="prefixes" %}

## Barrel
There are 10 non-unique barrels.

{% include parts.html 
    parts=site.data.pistols.barrels
    meta=site.data.pistols.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.barrel_overrides
%}
{% include footnote_end.html
    spin_up="No pistols support spin up time, so this is completely neutral."
    same_model="These share the same model."
%}

## Bodies
There are 32 non-unique bodies, one for each rarity-manufacturer combination. Most bodies share the
same stats, based on rarity.

{% assign bodies = site.data.pistols.bodies
                   | where_exp: "body", "page.body_names contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.pistols.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.body_overrides
%}

{% include body_table.html
    body_list=site.data.pistols.bodies
    meta=site.data.pistols.meta
    common="GD_Weap_Pistol.Body.Pistol_Body_Dahl"
    uncommon="GD_Weap_Pistol.Body.Pistol_Body_Dahl_2"
    rare="GD_Weap_Pistol.Body.Pistol_Body_Dahl_3"
    very_rare="GD_Weap_Pistol.Body.Pistol_Body_Dahl_4"
    simple_bonuses=true
%}

The *Uncommon*{:.uncommon} and *Very Rare*{:.very-rare} Bandit bodies break this pattern. These both
have a drum mag rather than a stick, and thus have an extra mag size bonus.

{% assign bodies = site.data.pistols.bodies
                   | where_exp: "body", "page.special_body_names contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.pistols.meta
    simple_bonuses=true
%}


## Grips
There are 8 non-unique grips.

{% include parts.html 
    parts=site.data.pistols.grips
    meta=site.data.pistols.meta
    mesh_image=true
    simple_bonuses=true
%}

## Sights
There are 9 non-unique sights, including a "no sight" part with no model. Some sight bonuses are
only applied while aiming.

{% include parts.html 
    parts=site.data.pistols.sights
    meta=site.data.pistols.meta
    mesh_image=true
    simple_bonuses=true
%}

Click [here](/pistols/zoom/) for a comparison of the zoom level of each sight.

## Element
The element parts have no model, but instead add lights over the weapon in their relevant colours.
There are six non-unique element parts, one for each element, and one for no element.

{% include parts.html 
    parts=site.data.pistols.elements
    meta=site.data.pistols.meta
    simple_bonuses=true
%}

## Material
The material parts also have no model, instead defining the actual textures applied ontop of all the
other models.

There are 44 non-unique material parts. Like with bodies, there's one for each rarity-manufacturer
combination. In Tina DLC, each manufactuer gets an additional gemstone material, and in TPS,
Hyperion has an additional "Old Hyperion" material per rarity.

Most materials provide no stat bonuses. The exceptions are listed below.

{% assign bonus_materials = site.data.pistols.materials | where_exp: "part", "part.bonuses" %}
{% include parts.html
    parts=bonus_materials
    meta=site.data.pistols.meta
    simple_bonuses=true
%}

## Weapon Balance
The Weapon Balance defines what parts a certain weapon can have. Balances themselves do not affect
stats, but are they very important for the actual generation of weapons.

## Weapon Type Definition
Like the name might suggest, the definition essentialy defines all the unique properties of each
weapon type. There is one definition per manufacturer.

Definitions may provide stat bonuses. Those which do are listed below.

{% assign bonus_definitions = site.data.pistols.definitions | where_exp: "part", "part.bonuses" %}
{% include parts.html
    id="definitions"
    parts=bonus_definitions
    meta=site.data.pistols.meta
    simple_bonuses=true
%}

Definitions are also very important if you're trying to calculate exact stats.

<details>
    <summary>Expand</summary>

To start with, they define the base values used by all stats stored on the weapon.

{% include definition_base_table.html meta=site.data.pistols.meta %}

They also define all grade bonuses, and how exactly they get converted into standard bonuses.

{% include definition_grade_table.html meta=site.data.pistols.meta %}

</details>
