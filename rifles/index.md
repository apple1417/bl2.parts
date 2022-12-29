---
part_reference:
  - name: Accessory
    src: /rifles/^images/parts/accessory.png
  - name: Barrel
    src: /rifles/^images/parts/barrel.png
  - name: Body
    src: /rifles/^images/parts/body.png
  - name: Grip
    src: /rifles/^images/parts/grip.png
  - name: Sight
    src: /rifles/^images/parts/sight.png
  - name: Stock
    src: /rifles/^images/parts/stock.png

accessory_overrides:
- idx: 5
  footnote: same_model
- idx: 7
  bonus_block:
      - group_idx: 1
        overrides:
          - idx: 1
            footnote: different_times
          - idx: 2
            footnote: different_times
- idx: 9
  footnote: same_model

barrel_overrides:
- idx: 3
  footnote: same_etech_model
- idx: 4
  footnote: same_etech_model
  image_src: /rifles/^images/barrels/etech_dahl.png
- idx: 6
  footnote: same_torgue_model
- idx: 7
  footnote: same_torgue_model
- idx: 8
  footnote: same_torgue_model
- idx: 9
  footnote: same_torgue_model
- idx: 10
  footnote: same_torgue_model

bodies:
  common_names:
    - GD_Weap_AssaultRifle.Body.AR_Body_Bandit
    - GD_Weap_AssaultRifle.Body.AR_Body_Dahl
    - GD_Weap_AssaultRifle.Body.AR_Body_Jakobs
    - GD_Weap_AssaultRifle.Body.AR_Body_Torgue
    - GD_Weap_AssaultRifle.Body.AR_Body_Vladof
  overrides:
    - idx: 1
      name: Bandit
    - idx: 2
      name: Dahl
    - idx: 3
      name: Jakobs
    - idx: 4
      name: Torgue
    - idx: 5
      name: Vladof
  extra_stats:
    - GD_Weap_AssaultRifle.Body.AR_Body_Bandit_3
    - GD_Weap_AssaultRifle.Body.AR_Body_Bandit_4
  extra_stats_overrides:
    - idx: 1
      bonus_block:
      - group_idx: 1
        overrides:
          - idx: 1
            footnote: different_times
          - idx: 2
            footnote: different_times
          - idx: 4
            footnote: different_times
          - idx: 5
            footnote: different_times
    - idx: 2
      bonus_block:
      - group_idx: 1
        overrides:
          - idx: 1
            footnote: different_times
          - idx: 2
            footnote: different_times
          - idx: 4
            footnote: different_times
          - idx: 5
            footnote: different_times
---

# Rifle Parts Guide
Rifles are made out of 6 main visible parts.

{% include part_reference.html parts=page.part_reference image_class="massive" %}

Other parts include the element, the material, weapon balance, and the weapon type definition.

## Accessories
There are 9 non-unique accessories, including a "no accessory" part with no model.
<style>
#accessories_table img {
    min-height: var(--img-size-standard);
}
</style>
{% include parts.html
    id="accessories_table"
    parts=site.data.rifles.accessories
    meta=site.data.rifles.meta
    image_class="big"
    mesh_image=true
    simple_bonuses=true
    overrides=page.accessory_overrides
%}

{% include footnote_end.html
    different_times="The two bonuses are applied at different times of the calculation."
    same_model="These all use the same model."
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has.

{% include prefixes.html parts=site.data.rifles.accessories %}

## Barrels
There are 12 non-unique barrels, using 7 different models.

{% include parts.html
    id="barrels_table"
    parts=site.data.rifles.barrels
    meta=site.data.rifles.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.barrel_overrides
%}

{% include footnote_end.html
    same_etech_model="These both use the same model, but (unsurprisingly) the Dahl version only spawns on Dahl guns."
    same_torgue_model="These all use the same model, but only spawn on their relevant manufacturer."
%}

## Bodies
There are 20 non-unique bodies, one for each rarity-manufacturer combination. Most bodies share the
same stats, based on rarity.

{% assign bodies = site.data.rifles.bodies
                   | where_exp: "body", "page.bodies.common_names contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.rifles.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.bodies.overrides
%}

{% include body_table.html 
    body_list=site.data.rifles.bodies
    meta=site.data.rifles.meta
    common="GD_Weap_AssaultRifle.Body.AR_Body_Bandit"
    uncommon="GD_Weap_AssaultRifle.Body.AR_Body_Bandit_2"
    rare="GD_Weap_AssaultRifle.Body.AR_Body_Bandit_3"
    very_rare="GD_Weap_AssaultRifle.Body.AR_Body_Bandit_4"
    simple_bonuses=true
%}

The *Rare*{:.rare} and *Very Rare*{:.very-rare} Bandit bodies break this pattern. These are both
belt-fed with a box mag rather than a stick, and thus have an extra mag size bonus.

{% assign bodies = site.data.rifles.bodies
                   | where_exp: "body", "page.bodies.extra_stats contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.rifles.meta
    simple_bonuses=true
    overrides=page.bodies.extra_stats_overrides
%}

{% include footnote_end.html
    different_times="The bonuses in each pair are applied at different times of the calculation."
%}

## Grips
There are 5 non-unique grips.

{% include parts.html 
    parts=site.data.rifles.grips
    meta=site.data.rifles.meta
    mesh_image=true
    simple_bonuses=true
%}

## Sights
There are 6 non-unique sights, including a "no sight" part with no model. Some sight bonuses are
only applied while aiming.

{% include parts.html 
    parts=site.data.rifles.sights
    meta=site.data.rifles.meta
    image_class="small"
    mesh_image=true
    simple_bonuses=true
%}

Click [here](/rifles/zoom/) for a comparison of the zoom level of each sight.

## Stocks
There are 5 non-unique stocks.

{% include parts.html 
    parts=site.data.rifles.stocks
    meta=site.data.rifles.meta
    mesh_image=true
    simple_bonuses=true
%}

## Elements
The element parts have no model, but instead add lights over the weapon in their relevant colours.
There are six non-unique element parts, one for each element, and one for no element.

{% include parts.html 
    parts=site.data.rifles.elements
    meta=site.data.rifles.meta
    simple_bonuses=true
%}

## Materials
The material parts also have no model, instead defining the actual textures applied on top of all
the other models.

There are 25 non-unique material parts. Like with bodies, there's one for each rarity-manufacturer
combination. In Tina DLC, each manufacturer gets an additional gemstone material.

Most materials provide no stat bonuses. The exceptions are listed below.
{% assign bonus_materials = site.data.rifles.materials | where_exp: "part", "part.bonuses" %}
{% include parts.html
    parts=bonus_materials
    meta=site.data.rifles.meta
    simple_bonuses=true
%}

## Weapon Balances
The Weapon Balance defines what parts a certain weapon can have. Balances themselves do not affect
stats, but are they very important for the actual generation of weapons.

## Weapon Type Definitions
Like the name might suggest, the definition essentially defines all the unique properties of each
weapon type. There are 5 non-unique definitions, one per manufacturer.

{% include parts.html
    parts=site.data.rifles.definitions
    meta=site.data.rifles.meta
    simple_bonuses=true
%}

Definitions are also very important if you're trying to calculate exact stats.

<details>
    <summary>Expand</summary>

To start with, they define the base values used by all stats stored on the weapon.

{% include definition_base_table.html meta=site.data.rifles.meta %}

They also define all grade bonuses, and how exactly they get converted into standard bonuses.

{% include definition_grade_table.html meta=site.data.rifles.meta %}

</details>
