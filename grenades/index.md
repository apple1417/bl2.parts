---
part_reference:
  - name: Child Count
    src: /grenades/^images/parts/child.png
  - name: Delivery
    src: /grenades/^images/parts/delivery.png
  - name: Material
    src: /grenades/^images/parts/material.png
  - name: Blast Radius
    src: /grenades/^images/parts/radius.png
  - name: Trigger
    src: /grenades/^images/parts/trigger.png

delivery_overrides:
  - idx: 4
    bonus_block:
    - group_idx: 1
      overrides:
        - idx: 1
          footnote: different_times
        - idx: 2
          footnote: different_times
  - idx: 5
    bonus_block:
    - group_idx: 1
      overrides:
        - idx: 1
          footnote: different_times
        - idx: 2
          footnote: different_times
  - idx: 6
    bonus_block:
    - group_idx: 1
      overrides:
        - idx: 1
          footnote: different_times
        - idx: 2
          footnote: different_times
  - idx: 7
    bonus_block:
    - group_idx: 1
      overrides:
        - idx: 1
          footnote: different_times
        - idx: 2
          footnote: different_times

materials:
  names:
    - GD_GrenadeMods.Material.Material_Bandit_4_VeryRare
    - GD_GrenadeMods.Material.Material_Dahl_4_VeryRare
    - GD_GrenadeMods.Material.Material_Hyperion_4_VeryRare
    - GD_GrenadeMods.Material.Material_Maliwan_4_VeryRare
    - GD_GrenadeMods.Material.Material_Tedior_4_VeryRare
    - GD_GrenadeMods.Material.Material_Torgue_4_VeryRare
    - GD_GrenadeMods.Material.Material_Vladof_4_VeryRare
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
    - idx: 6
      name: Torgue
    - idx: 7
      name: Vladof
  torgue_name: GD_GrenadeMods.Material.Material_Torgue_4_VeryRare
  torgue_overrides:
    - idx: 1
      name: Torgue

accessories:
  cols:
    - "*Corrosive*{:.corrosive}"
    - "*Cryo*{:.cryo}"
    - "*Fire*{:.fire}"
    - "*Shock*{:.shock}"
    - "*Slag*{:.slag}"
  rows:
    - Grade 0
    - Grade 1
    - Grade 2
    - Grade 3
    - Grade 4
  explosive_overrides:
    - idx: 1
      name: "*Explosive*{:.explosive}"

definition_slot_order:
  - DamageRadius
  - ChildCount
  - FuseTime
  - Damage
  - StatusEffectChanceModifier_Corrosive
  - StatusEffectChanceModifier_Ice
  - StatusEffectChanceModifier_Incendiary
  - StatusEffectChanceModifier_Shock
  - StatusEffectChanceModifier_Slag
  - StatusEffectDamage_Corrosive
  - StatusEffectDamage_Ice
  - StatusEffectDamage_Incendiary
  - StatusEffectDamage_Shock
---
# Grenade Parts Guide
Grenades are made up of up to 10 different parts. Unfortunately only 5 of these slots use parts with
models, and even within these it isn't possible to tell between every non unique part visually.

{% include part_reference.html parts=page.part_reference image_class="" %}

## Blast Radius Parts
There are 4 non-unique blast radius parts.

{% include parts.html 
    parts=site.data.grenades.zeta
    meta=site.data.grenades.meta
    mesh_image=true
    simple_bonuses=true
%}

## Child Count Parts
There are 7 non-unique child count parts.

{% include parts.html 
    parts=site.data.grenades.eta
    meta=site.data.grenades.meta
    mesh_image=true
    simple_bonuses=true
%}

These child count bonuses only apply if the payload actually supports child grenades, otherwise they
have no effect.

## Deliveries
There are 7 non-unique delivieries. The delivery changes how your grenade is thrown.

{% include parts.html 
    parts=site.data.grenades.beta
    meta=site.data.grenades.meta
    mesh_image=true
    simple_bonuses=true
    overrides=page.delivery_overrides
%}
{% include footnote_end.html
    different_times="The bonuses in each pair are applied at different times of the calculation."
%}

## Materials
There are 28 non-unique materials, one for each rarity-manufacturer combination. The manufacturer
changes the model, while rarity changes the skin applied to it.

{% assign materials = site.data.grenades.material
                   | where_exp: "mat", "page.materials.names contains mat._obj_name" %}
{% include parts.html 
    parts=materials
    meta=site.data.grenades.meta
    mesh_image=true
    hide_bonuses=true
    overrides=page.materials.overrides
%}

Only Torgue materials provide a bonus, of which all rarities are identical.

{% assign torgue = site.data.grenades.material | where: "_obj_name", page.materials.torgue_name %}
{% include parts.html 
    parts=torgue
    meta=site.data.grenades.meta
    simple_bonuses=true
    overrides=page.materials.torgue_overrides
%}

## Triggers
There are 6 non-unique triggers.

{% include parts.html 
    parts=site.data.grenades.gamma
    meta=site.data.grenades.meta
    mesh_image=true
    simple_bonuses=true
%}

## Accessories
The accessories define both the element of the grenade and it's (unlisted) status chance modifier.

There are 26 non-unique accessories - Each element has 5 parts at different grades, and there's a
single part for explosive.

{% assign explosive_accessory = site.data.grenades.delta | where: "name", "Explosive" %}
{% include parts.html 
    parts=explosive_accessory
    meta=site.data.grenades.meta
    simple_bonuses=true
    overrides=page.accessories.explosive_overrides
%}
<br>
{% assign accessories_table = site.data.grenades.delta
                              | where: "unique", false
                              | where_exp: "acc", "acc.name != 'Explosive'"
                              | group_by_exp: "acc", "acc.name | split: ' ' | last"
                              | map: "items" %}
{% include part_table.html 
    table=accessories_table
    column_headers=page.accessories.cols
    row_headers=page.accessories.rows
    meta=site.data.grenades.meta
    simple_bonuses=true
%}

## Damage
There are 8 non-unique damage parts.

{% include parts.html 
    parts=site.data.grenades.epsilon
    meta=site.data.grenades.meta
    simple_bonuses=true
%}

## Payload
The payload controls what exactly happens when a grenade expodes. Most unique grenades use unique
payloads to implement their behaviour. Payloads also determine if child grenades are supported -
even with several bonuses, none will spawn if the payload is incorrect.

There are 6 standard payload types. In TPS, each of these has a duplicate which can also shatter air
masks, meaning there are to a total of 12 non-unique payload parts.

{% include parts.html 
    parts=site.data.grenades.alpha
    meta=site.data.grenades.meta
    simple_bonuses=true
%}

## Status Damage
There are 6 non-unique status damage parts.

{% include parts.html 
    parts=site.data.grenades.theta
    meta=site.data.grenades.meta
    simple_bonuses=true
%}

## Inventory Balance
The Inventory Balance defines what parts a certain item can have. Balances themselves do not affect
stats, but are they very important for the actual generation of items.

## Grenade Definition
Like the name might suggest, the definition essentialy defines all the unique properties of each
grenade type. There is one standard definition used by all non-unique grenades, while most unique
grenades use their own unique definition.

Definitions are very important if you’re trying to calculate exact stats, but otherwise can be
mostly ignored.

<details markdown="1">
<summary>Expand</summary>

To start with, they define the base values for all stats stored on the grenade. Unlike with
weapons, this is simply done using regular *pre-add*{:.pre-add} bonuses, so see the
[full parts reference](/grenades/all_parts/#definitions) for details.

They also define all grade bonuses, and how exactly they get converted into standard bonuses.
Definitions do not neccessarily define all grade slots, if a slot's undefined then no grade bonuses
will be applied to it.

{%- comment -%}
This is heavily based on the definition table, but there are enough differences that it's easier to
just recreate it here.

To start off, we want a custom header, rather than repeating "grenade status chance modifier" 5x we
can just put that once in a level above it.

We also want one definition per row, rather than per column, cause otherwise the table ends up 3x
wider than the rest of the page.

With the table transposed, we also don't really care about merging identical cells anymore.
{%- endcomment -%}
<style>
    #grades {
        overflow-x: scroll;
    }
    #grades table tbody:first-of-type tr:first-child th,
    #grades table tbody:first-of-type tr:first-child td {
        border-bottom-style: double;
        border-bottom-width: 3px;
    }
</style>
<div id="grades">
<table class="border">
<thead><tr>
  <th rowspan="2"></th>
  <th rowspan="2">Blast Radius</th>
  <th rowspan="2">Child Count</th>
  <th rowspan="2">Fuse Time</th>
  <th rowspan="2">Grenade Damage</th>
  <th colspan="5">Grenade Status Chance Modifier</th>
  <th colspan="4">Grenade Status Effect Damage</th>
</tr><tr>
    <th class="corrosive">Corrosive</th>
    <th class="cryo">Cryo</th>
    <th class="fire">Fire</th>
    <th class="shock">Shock</th>
    <th class="slag">Slag</th>
    <th class="corrosive">Corrosive</th>
    <th class="cryo">Cryo</th>
    <th class="fire">Fire</th>
    <th class="shock">Shock</th>
</tr></thead>
<tbody>

{% assign standard_definition = site.data.grenades.meta.definitions[
                                  site.data.grenades.meta.standard_definition_idx] %}
{% assign sorted_definitions = site.data.grenades.meta.definitions
                               | where_exp: "def", "def != standard_definition"
                               | sort_natural: "name"
                               | unshift: standard_definition %}
{% for definition in sorted_definitions %}
    <tr>
        <th>{{definition.name}}</th>

        {% assign row = "" | split: "" %}
        {% for slot in page.definition_slot_order %}
            {% assign grade_stats = definition.grades | where: "slot", slot | first %}
            {% unless grade_stats %}
                <td>-</td>
                {% continue %}
            {% endunless %}

            <td class="{{grade_stats.type}} per-grade">
                {%- include grade.html grade_stats=grade_stats -%}
            </td>
        {% endfor %}
    </tr>
{% endfor %}
</tbody>
</table>
</div>

</details>
