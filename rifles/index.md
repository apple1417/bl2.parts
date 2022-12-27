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
