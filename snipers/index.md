---
part_reference:
  - name: Accessory
    src: /snipers/^images/parts/accessory.png
  - name: Barrel
    src: /snipers/^images/parts/barrel.png
  - name: Body
    src: /snipers/^images/parts/body.png
  - name: Grip
    src: /snipers/^images/parts/grip.png
  - name: Sight
    src: /snipers/^images/parts/sight.png
  - name: Stock
    src: /snipers/^images/parts/stock.png

barrel_overrides:
  - idx: 5
    bonus_block:
      - group_idx: 2
        overrides:
          # Matching maliwan barrel has two separate damage bonuses, which we can combine into one
          - idx: 2
            ignore: true
          - idx: 3
            replace:
              from: "&times;1.1"
              to: "&times;1.2"

bodies:
  names:
    - GD_Weap_SniperRifles.Body.SR_Body_Dahl
    - GD_Weap_SniperRifles.Body.SR_Body_Hyperion
    - GD_Weap_SniperRifles.Body.SR_Body_Jakobs
    - GD_Weap_SniperRifles.Body.SR_Body_Maliwan
    - GD_Weap_SniperRifles.Body.SR_Body_Vladof
  overrides:
    - idx: 1
      name: Dahl
    - idx: 2
      name: Hyperion
    - idx: 3
      name: Jakobs
    - idx: 4
      name: Maliwan
    - idx: 5
      name: Vladof
  special:
    - GD_Weap_SniperRifles.Body.SR_Body_Jakobs
    - GD_Weap_SniperRifles.Body.SR_Body_Jakobs_3
  special_overrides:
    - idx: 2
      bonus_block:
        - group_idx: 1
          overrides:
            # The grade and bolt action damage bonuses are both scales we can combine
            - idx: 3
              ignore: true
            - idx: 4
              replace:
                from: "&times;1.48"
                to: "&times;1.63"

definition_stat_overrides:
  - idx: 6
    footnote: "hot_mama_definition"
---


# Sniper Parts Guide
Snipers are made out of 6 main visible parts.

{% include part_reference.html parts=page.part_reference image_class="massive" %}

## Accessories
There are 8 non-unique accessories, including a "no accessory" part with no model.

<style>
#accessories_table img {
    min-height: var(--img-size-standard);
}
#accessories_table > div.part-block {
    padding: revert;
}
#accessories_table > div:nth-child(6) > img {
    max-height: var(--img-size-standard);
}
</style>
{% include parts.html
    id="accessories_table"
    parts=site.data.snipers.accessories
    meta=site.data.snipers.meta
    image_class="big"
    mesh_image=true
    simple_bonuses=true
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has.

{% include prefixes.html parts=site.data.snipers.accessories %}

## Barrels
There are 6 non-unique barrels.

{% include parts.html
    parts=site.data.snipers.barrels
    meta=site.data.snipers.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.barrel_overrides
%}


## Bodies
There are 20 non-unique bodies, one for each rarity-manufacturer combination. All bodies of the
same rarity share the same stats.

<style>
#bodies_table img {
    min-height: var(--img-size-standard);
    max-width: var(--img-size-big);
    margin: -1em;
}
#bodies_table div:nth-child(1) img {
    width: var(--img-size-standard);
}
#bodies_table div:nth-child(4) img {
    object-fit: cover;
    width: calc(var(--img-size-massive));
}
</style>
{% assign bodies = site.data.snipers.bodies
                   | where_exp: "body", "page.bodies.names contains body._obj_name" %}
{% include parts.html
    id="bodies_table"
    parts=bodies
    meta=site.data.snipers.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.bodies.overrides
%}

{% include body_table.html 
    body_list=site.data.snipers.bodies
    meta=site.data.snipers.meta
    common="GD_Weap_SniperRifles.Body.SR_Body_Dahl"
    uncommon="GD_Weap_SniperRifles.Body.SR_Body_Dahl_2"
    rare="GD_Weap_SniperRifles.Body.SR_Body_Dahl_3"
    very_rare="GD_Weap_SniperRifles.Body.SR_Body_Dahl_4"
    simple_bonuses=true
%}

The *Common*{:.common} and *Rare*{:.rare} Jakobs bodies break this pattern. They both have extra
bonuses to convert them to bolt-action.

{% assign bodies = site.data.snipers.bodies
                   | where_exp: "body", "page.bodies.special contains body._obj_name" %}
{% include parts.html
    parts=bodies
    meta=site.data.snipers.meta
    simple_bonuses=true
    overrides=page.bodies.special_overrides
%}

## Grips
There are 5 non-unique grips.

{% include parts.html 
    parts=site.data.snipers.grips
    meta=site.data.snipers.meta
    mesh_image=true
    simple_bonuses=true
%}

## Sights
There are 5 non-unique sights. Some sight bonuses are only applied while aiming.

{% include parts.html 
    parts=site.data.snipers.sights
    meta=site.data.snipers.meta
    mesh_image=true
    simple_bonuses=true
%}

Click [here](/snipers/zoom/) for a comparison of the zoom level of each sight.

## Stocks
There are 5 non-unique stocks.
{% include parts.html 
    parts=site.data.snipers.stocks
    meta=site.data.snipers.meta
    mesh_image=true
    simple_bonuses=true
%}

## Elements
The element parts have no model, but instead add lights over the weapon in their relevant colours.
There are six non-unique element parts, one for each element, and one for no element.

{% include parts.html 
    parts=site.data.snipers.elements
    meta=site.data.snipers.meta
    simple_bonuses=true
%}

## Materials
The material parts also have no model, instead defining the actual textures applied on top of all
the other models.

There are 29 non-unique material parts. Like with bodies, there's one for each rarity-manufacturer
combination. In Tina DLC, each manufacturer gets an additional gemstone material, and in TPS,
Hyperion has an additional "Old Hyperion" material per rarity.

Most materials provide no stat bonuses. The exceptions are listed below.
{% assign bonus_materials = site.data.snipers.materials | where_exp: "part", "part.bonuses" %}
{% include parts.html
    parts=bonus_materials
    meta=site.data.snipers.meta
    simple_bonuses=true
%}

## Weapon Balances
The Weapon Balance defines what parts a certain weapon can have. Balances themselves do not affect
stats, but are they very important for the actual generation of weapons.

## Weapon Type Definitions
Like the name might suggest, the definition essentially defines all the unique properties of each
weapon type. There are 5 non-unique definitions, one per manufacturer.

{% include parts.html
    parts=site.data.snipers.definitions
    meta=site.data.snipers.meta
    simple_bonuses=true
%}

Definitions are also very important if you're trying to calculate exact stats.

<details>
    <summary>Expand</summary>

To start with, they define the base values used by all stats stored on the weapon.

{% include definition_base_table.html
    meta=site.data.snipers.meta
    overrides=page.definition_stat_overrides
%}

They also define all grade bonuses, and how exactly they get converted into standard bonuses.

{% include definition_grade_table.html
    meta=site.data.snipers.meta
    overrides=page.definition_stat_overrides
%}

<br>
{% include footnote_end.html
    hot_mama_definition="The Hot Mama uses it's own unique definition, listed in this section to help you calculate it's stats."
%}

</details>
