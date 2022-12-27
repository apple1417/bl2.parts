---
part_table:
  entries:
    - name: Tediore
      img: tediore.png
      body: GD_Shields.Body.Body1_Tediore
    - name: Bandit
      img: bandit.png
      body: GD_Shields.Body.Body2_Bandit
    - name: Vladof
      img: vladof.png
      body: GD_Shields.Body.Body3_Vladof
    - name: Dahl
      img: dahl.png
      body: GD_Shields.Body.Body4_Dahl
    - name: Anshin
      img: anshin.png
      body: GD_Shields.Body.Body5_Anshin
    - name: Maliwan
      img: maliwan.png
      body: GD_Shields.Body.Body5_Maliwan
    - name: Torgue
      img: torgue.png
      body: GD_Shields.Body.Body6_Torgue
    - name: Hyperion
      img: hyperion.png
      body: GD_Shields.Body.Body7_Hyperion
    - name: Pangolin
      img: pangolin.png
      body: GD_Shields.Body.Body8_Pangolin
  grades:
    - Capacity
    - RechargeDelay
    - RechargeRate
    - Special01

part_reference:
  - name: Accessory
    src: /shields/^images/accessory.png
  - name: Battery
    src: /shields/^images/battery.png
  - name: Body
    src: /shields/^images/body.png
  - name: Capacitor
    src: /shields/^images/capacitor.png

materials:
  rarities:
    - "*Common*{:.common}"
    - "*Uncommon*{:.uncommon}"
    - "*Rare*{:.rare}"
    - "*Very Rare*{:.very-rare}"
  main:
    parts:
      - GD_Shields.Material.Material1_Common_Roid
      - GD_Shields.Material.Material2_Uncommon_Roid
      - GD_Shields.Material.Material3_Rare_Roid
      - GD_Shields.Material.Material4_VeryRare_Roid
    grades:
      - Capacity
      - Special01
    column_headers:
      - Rarity
      - Capacity
      - Special
  hyperion:
    parts:
      - GD_Shields.Material.Material1_Common_Impact
      - GD_Shields.Material.Material2_Uncommon_Impact
      - GD_Shields.Material.Material3_Rare_Impact
      - GD_Shields.Material.Material4_VeryRare_Impact
    grades:
      - Capacity
      - RechargeDelay
      - Special01
    column_headers:
      - Rarity
      - Capacity
      - Recharge Delay
      - Special
  tediore:
    parts:
      - GD_Shields.Material.Material1_Common
      - GD_Shields.Material.Material2_Uncommon_NoSpecial
      - GD_Shields.Material.Material3_Rare_NoSpecial
      - GD_Shields.Material.Material4_VeryRare_NoSpecial
    grades:
      - Capacity
      - RechargeRate
      - RechargeDelay
    column_headers:
      - Rarity
      - Capacity
      - Recharge Rate
      - Recharge Delay

definitions:
  main_slot_order:
    - Capacity
    - RechargeRate
    - RechargeDelay
    - Special01
    - Special02
    - Special03
    - Special04
    - CorrosiveResist
    - IceResist
    - FireResist
    - ShockResist
  activate_only:
    - GD_Aster_Shields.A_Item.Aster_Seraph_Antagonist_Shield
    - GD_Aster_Shields.A_Item.Aster_Seraph_Blockade_Shield
---
# Shield Parts Guide

<style>
    #part-table tr td:nth-child(n+4) {
        font-size: 1.4em;
    }
</style>
{% comment %}
This table is unique enough that it's easier to just create it here.
{% endcomment %}
<table id="part-table" class="border"><thead><tr>
    <th>Manufacturer</th>
    <th>Accessory</th><th>Battery <br> Body <br> Capacitor</th>
    <th>Capacity</th><th>Recharge Delay</th><th>Recharge Rate</th><th>Special</th>
</tr></thead><tbody>
    {% assign sorted_part_table = page.part_table.entries | sort_natural: "name" %}
    {% for part in sorted_part_table %}
        <tr>
            <td>{{ part.name }}</td>
            <td><img class="small" src="/shields/^images/accessories/{{ part.img }}" alt="{{ part.name }} Accessory"></td>
            <td><img class="small" src="/shields/^images/parts/{{ part.img }}" alt="{{ part.name }} Parts"></td>
            {% assign body = site.data.shields.alpha | where: "_obj_name", part.body | first %}
            {% include _grade_stat_table_row.html part=body grades=page.part_table.grades %}
        </tr>
    {% endfor %}
</tbody><tfoot><tr>
    <td class="footnotes" colspan="7">
        Accessories provide no bonuses, these stats only apply to the other parts.
    </td>
</tr></tfoot></table>

# More Info
Shields are made out of 4 main visible parts.

{% include part_reference.html parts=page.part_reference image_class="med" %}

Internally the Accessory and Body were swapped at some point, leading to the misleading names.

Each manufacturer has one non-unique part for each slot. As luck would have it, the bonuses these
parts provide have enough of a pattern that they can be summarised in the above table. No non-unique
Accessories provide bonuses, and within each manufacturer the non-unique Batteries, Bodies, and
Capacitors all share the exact same bonuses.

## Materials
The material parts have no model, instead defining the actual textures applied on top of all the
other models.

There are 36 non-unique materials, one for each rarity-manufacturer combination. Most of these
follow the same pattern.

{% assign parts = "" | split: "" %}
{% for obj_name in page.materials.main.parts %}
    {% assign material = site.data.shields.material | where: "_obj_name", obj_name | first %}
    {% assign parts = parts | push: material %}
{% endfor %}

{% include grade_stat_table.html
    parts=parts
    grades=page.materials.main.grades
    row_names=page.materials.rarities
    column_headers=page.materials.main.column_headers
%}

Hyperion materials instead use the following bonuses.

{% assign hyperion_parts = "" | split: "" %}
{% for obj_name in page.materials.hyperion.parts %}
    {% assign material = site.data.shields.material | where: "_obj_name", obj_name | first %}
    {% assign hyperion_parts = hyperion_parts | push: material %}
{% endfor %}

{% include grade_stat_table.html
    parts=hyperion_parts
    grades=page.materials.hyperion.grades
    row_names=page.materials.rarities
    column_headers=page.materials.hyperion.column_headers
%}

Tediore materials instead use the following bonuses.

{% assign tediore_parts = "" | split: "" %}
{% for obj_name in page.materials.tediore.parts %}
    {% assign material = site.data.shields.material | where: "_obj_name", obj_name | first %}
    {% assign tediore_parts = tediore_parts | push: material %}
{% endfor %}

{% include grade_stat_table.html
    parts=tediore_parts
    grades=page.materials.tediore.grades
    row_names=page.materials.rarities
    column_headers=page.materials.tediore.column_headers
%}

## Inventory Balances
The Inventory Balance defines what parts a certain item can have. Balances themselves do not affect
stats, but are they very important for the actual generation of items.

## Shield Definitions
Like the name might suggest, the definition essentially defines all the unique properties of each
shield type. These are what create all the different special effects. There is one definition per
shield type.

Definitions are very important if you’re trying to calculate exact stats, but otherwise can be
mostly ignored.

<details markdown="1">
<summary>Expand</summary>

To start with, they define the base values for all stats stored on the grenade. Unlike with
weapons, this is simply done using regular *pre-add*{:.pre-add} bonuses, so see the
[full parts reference](/shields/all_parts/#definitions) for details.

They also define all grade bonuses, and how exactly they get converted into standard bonuses. Grade
bonuses have a few special uses on shields.

Shield special is perhaps the best use of the grade system. A single generic special slot can have
different effects based on the shield type, so the non unique parts can provide bonuses to any of
them. There are actually 4 special slots, so far this page has simplified them all into one. Most
parts (including all non-uniques) boost Special 01 and 02 equally, and don't touch 03 and 04, though
again, see the [full parts reference](/shields/all_parts/) for exceptions.

Elemental immunities are another interesting use of grades. The immunity is defined entirely by the
base value of the grade bonus, and parts simply *activate* the slot, without adding any grades.
Because of this, a bonus with value 0 actually still has an effect.

<style>
    #grades {
        overflow-x: scroll;
    }
</style>
<div id="grades">
<table class="border"><thead>
  <tr>
    <th rowspan="2"></th>
    <th rowspan="2">Capacity</th>
    <th rowspan="2">Recharge Rate</th>
    <th rowspan="2">Recharge Delay</th>
    <th colspan="4">Special</th>
    <th colspan="4">Status Chance Resistance</th>
  </tr><tr>
    <th>01</th>
    <th>02</th>
    <th>03</th>
    <th>04</th>
    <th>Corrosive</th>
    <th>Cryo</th>
    <th>Fire</th>
    <th>Shock</th>
  </tr>
</thead><tbody>

{%- assign non_unique_definitions = site.data.shields.meta.definitions
                                    | where: "unique", false
                                    | sort_natural: "name" -%}
{%- assign unique_definitions = site.data.shields.meta.definitions
                                | where: "unique", true
                                | sort_natural: "name" -%}
{%- assign ordered_definitions = non_unique_definitions | concat: unique_definitions -%}
{%- for definition in ordered_definitions -%}
    <tr>
        <td>{{- definition.name -}}</td>
            {%- for slot in page.definitions.main_slot_order -%}
                {%- assign grade_stats = definition.grades | where: "slot", slot | first -%}
                {%- unless grade_stats -%}
                    <td>-</td>
                    {%- continue -%}
                {%- endunless -%}

                {%- assign attr = site.data.attributes
                                  | where: "obj", grade_stats.attribute
                                  | first -%}
                {%- if attr -%}
                    {%- assign attr_name = attr.name -%}
                {%- else -%}
                    {%- assign attr_name = '<span style="color: blue">'
                                           | append: grade_stats.attribute
                                           | append: "</span>" -%}
                {%- endif -%}
                {%- if grade_stats.constraint -%}
                    {%- assign attr_name = attr_name
                                           | append: " ("
                                           | append: grade_stats.constraint
                                           | append: ")" -%}
                {%- endif -%}

                <td>
                    <span class="{{- grade_stats.type | append: " " -}} per-grade">
                        {%- include grade.html grade_stats=grade_stats -%}
                    </span>
                    {%- if forloop.index > 3 -%}
                        <br>{{- attr_name | markdownify | remove: "<p>" | remove: "</p>" | strip -}}
                    {%- endif -%}
                </td>
            {%- endfor -%}
    </tr>
{%- endfor -%}

</tbody></table>
</div>

A few shields have some extra unique grade slots, which only get activated by their definitions, but
nothing else, and never have any grades added. These are essentially just extra constant bonuses,
which go through the grade system as an extra step.

{%- assign DEF_GRADES_SEPARATOR = ":^:" -%}
{%- assign GRADES_SEPARATOR = "&|^|&" -%}
{%- assign activate_only_defs = "" | split: "" -%}
{%- for def in page.definitions.activate_only -%}
    {%- assign def_part = site.data.shields.definitions
                          | where: "_obj_name", def
                          | first -%}
    {%- assign def_meta = site.data.shields.meta.definitions
                          | where: "_obj_name", def
                          | first -%}
    {%- assign all_grade_bonuses = "" | split: "" -%}
    {%- for bonus in def_part.bonuses -%}
        {%- if bonus.value != 0 -%}
            {%- continue -%}
        {%- endif -%}
        {%- assign grade_stats = def_meta.grades | where: "slot", bonus.slot | first -%}
        {%- assign attr = site.data.attributes
                         | where: "obj", grade_stats.attribute
                         | first -%}

        {%- capture grade_bonus -%}
            {{- attr.name | markdownify | remove: "<p>" | remove: "</p>" | strip | prepend: " " -}}
            {{- GRADES_SEPARATOR -}}
            <span class="{{- grade_stats.type | append: " " -}} per-grade">
                {%- include grade.html grade_stats=grade_stats -%}
            </span><br>
        {%- endcapture -%}

        {%- assign all_grade_bonuses = all_grade_bonuses | push: grade_bonus -%}
    {%- endfor -%}

    {%- assign all_grade_bonuses = all_grade_bonuses | sort_natural -%}
    {%- assign row = def_part.name | append: DEF_GRADES_SEPARATOR -%}
    {%- for grade_bonus in all_grade_bonuses -%}
        {%- assign grade_data = grade_bonus | split: GRADES_SEPARATOR | reverse | join: "" -%}
        {%- assign row = row | append: grade_data -%}
        {%- unless forloop.last -%}
            {%- assign row = row | append: "<br>" -%}
        {%- endunless -%}
    {%- endfor -%}

    {%- assign activate_only_defs = activate_only_defs | push: row -%}
{%- endfor -%}

{% assign activate_only_defs = activate_only_defs | sort_natural %}
<div class="part-container">
    {%- for def in activate_only_defs -%}
        {%- assign def_data = def | split: DEF_GRADES_SEPARATOR -%}
        <div class="part-block">
            <h4>{{- def_data[0] -}}</h4>
            <div class="part-bonuses">{{- def_data[1] -}}</div>
        </div>
    {%- endfor -%}
</div>

{%- comment -%}
{% assign ignored_slots = "ExplosiveDamageResistance" | split: "," %}
{% for definition in ordered_definitions %}
    {% assign extra_slots = "" | split: "" %}
    {% for stats in definition.grades %}
        {% unless page.definitions.main_slot_order contains stats.slot
                  or ignored_slots contains stats.slot %}
            {% assign extra_slots = extra_slots | push: stats.slot %}
        {% endunless %}
    {% endfor %}
    {% if extra_slots %}
        {{definition.name}} - {{extra_slots | join: " "}}
    {% endif %}
{% endfor %}
{%- endcomment -%}

</details>
