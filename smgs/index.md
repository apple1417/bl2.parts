---
part_reference:
  - name: Accessory
    src: /smgs/^images/parts/accessory.png
  - name: Barrel
    src: /smgs/^images/parts/barrel.png
  - name: Body
    src: /smgs/^images/parts/body.png
  - name: Grip
    src: /smgs/^images/parts/grip.png
  - name: Sight
    src: /smgs/^images/parts/sight.png
  - name: Stock
    src: /smgs/^images/parts/stock.png

accessory_overrides:
- idx: 2
  footnote: same_model
- idx: 3
  footnote: same_model
  image_src: /smgs/^images/accessories/bayonet_bandit.png

barrel_overrides:
  - idx: 3
    footnote: same_etech_model
  - idx: 4
    footnote: same_etech_model
    image_src: /smgs/^images/barrels/etech_bandit.png

bodies:
  common_names:
    - GD_Weap_SMG.Body.SMG_Body_Bandit
    - GD_Weap_SMG.Body.SMG_Body_Dahl
    - GD_Weap_SMG.Body.SMG_Body_Hyperion
    - GD_Weap_SMG.Body.SMG_Body_Maliwan
    - GD_Weap_SMG.Body.SMG_Body_Tediore
  overrides:
    - idx: 1
      name: Bandit
    - idx: 2
      name: Dahl
    - idx: 3
      name: Hyperion
    - idx: 4
      name: Maliwan
    - idx: 5
      name: Tediore
---

# SMG Parts Guide
SMGs are made out of 6 main visible parts.

{% include part_reference.html parts=page.part_reference image_class="massive" %}

Other parts include the element, the material, weapon balance, and the weapon type definition.

## Accessories
There are 8 non-unique accessories, including a "no accessory" part with no model.

<style>
#accessories_table img {
    min-height: var(--img-size-standard);
}
#accessories_table > div.part-block {
    padding: revert;
}
</style>
{% include parts.html 
    id="accessories_table"
    parts=site.data.smgs.accessories
    meta=site.data.smgs.meta
    image_class="big"
    mesh_image=true
    simple_bonuses=true
    overrides=page.accessory_overrides
%}

{% include footnote_end.html
    same_model="These use the same model, but Bayonet 2 only spawns on Bandit guns."
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has.

{% include prefixes.html parts=site.data.smgs.accessories %}

## Barrels
There are 7 non-unique barrels.

<style>
#barrels_table > div.part-block {
    padding: 0 0.35em;
}
</style>
{% include parts.html
    id="barrels_table"
    parts=site.data.smgs.barrels
    meta=site.data.smgs.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.barrel_overrides
%}
{% include footnote_end.html
    same_etech_model="These both use the same model, but (unsurprisingly) the Bandit version only spawns Bandit guns."
%}

## Bodies
There are 20 non-unique bodies, one for each rarity-manufacturer combination. All bodies of the
same rarity share the same stats.

{% assign bodies = site.data.smgs.bodies
                   | where_exp: "body", "page.bodies.common_names contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.smgs.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.bodies.overrides
%}

{% include body_table.html 
    body_list=site.data.smgs.bodies
    meta=site.data.smgs.meta
    common="GD_Weap_SMG.Body.SMG_Body_Bandit"
    uncommon="GD_Weap_SMG.Body.SMG_Body_Bandit_VarA"
    rare="GD_Weap_SMG.Body.SMG_Body_Bandit_VarB"
    very_rare="GD_Weap_SMG.Body.SMG_Body_Bandit_VarC"
    simple_bonuses=true
%}

## Grips
There are 5 non-unique grips.

{% include parts.html 
    parts=site.data.smgs.grips
    meta=site.data.smgs.meta
    mesh_image=true
    simple_bonuses=true
%}
