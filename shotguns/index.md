---
part_reference:
  - name: Accessory
    src: /shotguns/^images/parts/accessory.png
  - name: Barrel
    src: /shotguns/^images/parts/barrel.png
  - name: Body
    src: /shotguns/^images/parts/body.png
  - name: Grip
    src: /shotguns/^images/parts/grip.png
  - name: Sight
    src: /shotguns/^images/parts/sight.png
  - name: Stock
    src: /shotguns/^images/parts/stock.png

accessory_overrides:
- idx: 4
  footnote: same_model
- idx: 5
  footnote: same_model
- idx: 6
  footnote: same_model

barrel_overrides:
- idx: 2
  footnote: same_etech_model
- idx: 3
  footnote: same_etech_model
  image_src: /shotguns/^images/barrels/etech_hyperion.png
  bonus_block:
    - group_idx: 1
      overrides:
        - idx: 1
          footnote: different_times
        - idx: 2
          footnote: different_times
- idx: 4
  bonus_block:
    - group_idx: 2
      overrides:
        - idx: 1
          footnote: hyperion_inverse_impulse
          replace:
            from: class="bad"
            to: class="good"
- idx: 5
  bonus_block:
    - group_idx: 1
      overrides:
        # Jakobs barrel has two seperate impulse grades, which we can combine into one
        - idx: 2
          ignore: true
        - idx: 3
          replace:
            from: "&times;1.5"
            to: "&times;1.75"

body_names:
 - GD_Weap_Shotgun.Body.SG_Body_Bandit
 - GD_Weap_Shotgun.Body.SG_Body_Hyperion
 - GD_Weap_Shotgun.Body.SG_Body_Jakobs
 - GD_Weap_Shotgun.Body.SG_Body_Tediore
 - GD_Weap_Shotgun.Body.SG_Body_Torgue

body_overrides:
- idx: 1
  name: Bandit
- idx: 2
  name: Hyperion
- idx: 3
  name: Jakobs
- idx: 4
  name: Tediore
- idx: 5
  name: Torgue
---

# Shotgun Parts Guide
Shotguns are made out of 6 main visible parts.

<style>
#part_reference img {
    max-width: calc(var(--img-size-big) + var(--img-size-increment));
    max-height: calc(var(--img-size-big) + var(--img-size-increment));
    min-height: revert;
}
</style>
{% include part_reference.html id="part_reference" parts=page.part_reference %}

Other parts include the element, the material, weapon balance, and the weapon type definition.

## Accessories
There are 9 non-unique accessories, including a "no accessory" part with no model.

<style>
#accessories img {
    min-width: var(--img-size-standard);
    min-height: var(--img-size-standard);
    max-width: var(--img-size-big);
}
</style>
{% include parts.html 
    id="accessories"
    parts=site.data.shotguns.accessories
    meta=site.data.shotguns.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.accessory_overrides
%}
{% include footnote_end.html
    same_model="These all use the same model."
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has.

{% include prefixes.html parts=site.data.shotguns.accessories %}

## Barrels
There are 7 non-unique barrels.

{% include parts.html 
    image_class="big"
    parts=site.data.shotguns.barrels
    meta=site.data.shotguns.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.barrel_overrides
%}
{% include footnote_end.html
    same_etech_model="These both use the same model, but (unsupringly) the Hyperion version only spawns on Hyperion guns."
    different_times="The two bonuses are applied at different times of the calculation."
    hyperion_inverse_impulse="While this type of bonus would be bad on all other manufacturers, on Hyperion it's actually good. See the [accuracy guide](/accuracy/#hyperion) for more. "
%}

## Bodies
There are 20 non-unique bodies, one for each rarity-manufacturer combination. All bodies of the
same rarity share the same stats.

<style>
#bodies > div:nth-child(2) > img {
    max-width: var(--img-size-big);
    min-height: var(--img-size-standard)
}
</style>
{% assign bodies = site.data.shotguns.bodies
                   | where_exp: "body", "page.body_names contains body._obj_name" %}
{% include parts.html
    id="bodies"
    parts=bodies
    meta=site.data.shotguns.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.body_overrides
%}

{% include body_table.html 
    body_list=site.data.shotguns.bodies
    meta=site.data.shotguns.meta
    common="GD_Weap_Shotgun.Body.SG_Body_Bandit"
    uncommon="GD_Weap_Shotgun.Body.SG_Body_Bandit_2"
    rare="GD_Weap_Shotgun.Body.SG_Body_Bandit_3"
    very_rare="GD_Weap_Shotgun.Body.SG_Body_Bandit_4"
    simple_bonuses=true
%}

## Grips
There are 5 non-unique grips.

{% include parts.html 
    parts=site.data.shotguns.grips
    meta=site.data.shotguns.meta
    mesh_image=true
    simple_bonuses=true
%}

## Sights
There are 6 non-unique sights, including a "no sight" part with no model. Some sight bonuses are
only applied while aiming.

{% include parts.html 
    image_class="small"
    parts=site.data.shotguns.sights
    meta=site.data.shotguns.meta
    mesh_image=true
    simple_bonuses=true
%}

Click [here](/shotguns/zoom/) for a comparison of the zoom level of each sight.

## Stocks
There are 5 non-unique stocks.
{% include parts.html 
    parts=site.data.shotguns.stocks
    meta=site.data.shotguns.meta
    mesh_image=true
    simple_bonuses=true
%}

## Elements
The element parts have no model, but instead add lights over the weapon in their relevant colours.
There are six non-unique element parts, one for each element, and one for no element. None of them
give any stat bonuses, good or bad. 

## Materials
The material parts also have no model, instead defining the actual textures applied ontop of all the
other models.

There are 29 non-unique material parts. Like with bodies, there's one for each rarity-manufacturer
combination. In Tina DLC, each manufactuer gets an additional gemstone material, and in TPS,
Hyperion has an additional "Old Hyperion" material per rarity.

Most materials provide no stat bonuses. The exceptions are listed below.
{% assign bonus_materials = site.data.shotguns.materials | where_exp: "part", "part.bonuses" %}
{% include parts.html
    parts=bonus_materials
    meta=site.data.shotguns.meta
    simple_bonuses=true
%}

## Weapon Balances
The Weapon Balance defines what parts a certain weapon can have. Balances themselves do not affect
stats, but are they very important for the actual generation of weapons.

## Weapon Type Definitions
Like the name might suggest, the definition essentialy defines all the unique properties of each
weapon type. There is one definition per manufacturer.

Definitions may provide stat bonuses.

<style>
#definitions div.part-block {
    flex-basis: calc(20% - 10px);
}
</style>
{% include parts.html
    id="definitions"
    parts=site.data.shotguns.definitions
    meta=site.data.shotguns.meta
    simple_bonuses=true
%}

Definitions are also very important if you're trying to calculate exact stats.

<details>
    <summary>Expand</summary>

To start with, they define the base values used by all stats stored on the weapon.

{% include definition_base_table.html meta=site.data.shotguns.meta %}

They also define all grade bonuses, and how exactly they get converted into standard bonuses.

{% include definition_grade_table.html meta=site.data.shotguns.meta %}

</details>
