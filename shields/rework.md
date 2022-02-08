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
---
# Shield Parts Guide

<style>
    #part-table tr td:nth-child(n+4) {
        font-size: 1.4em;
    }
</style>
{%- comment -%}
This table is unique enough that it's easier to just create it here.
{%- endcomment -%}
<table id="part-table" class="border"><thead><tr>
    <th>Manufacturer</th>
    <th>Accessory</th><th>Battery <br> Body <br> Capacitor</th>
    <th>Capacity</th><th>Recharge Delay</th><th>Recharge Rate</th><th>Special</th>
</tr></thead><tbody>
    {% assign sorted_part_table = page.part_table.entries | sort_natural: "name" %}
    {% for part in sorted_part_table %}
        <tr>
            <td>{{part.name}}</td>
            <td><img class="small" src="/shields/^images/accessories/{{part.img}}"></td>
            <td><img class="small" src="/shields/^images/parts/{{part.img}}"></td>
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

{% include part_reference.html parts=page.part_reference %}

Internally the Accessory and Body were swapped at some point, leading to the misleading names.

Each manufacturer has one non-unique part for each slot. As luck would have it, the bonuses these
parts provide have enough of a pattern that they can be summarised in the above table. No non-unique
Accessories provide bonuses, and within each manufacturer the non-unique Batteries, Bodies, and
Capacitors all share the exact same bonuses.

## Materials
The material parts have no model, instead defining the actual textures applied ontop of all the
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
Like the name might suggest, the definition essentialy defines all the unique properties of each
shield type. These are what create all the different special effects. There is one definition per
shield type.

Definitions are very important if you’re trying to calculate exact stats, but otherwise can be
mostly ignored.

<details open markdown="1">
<summary>Expand</summary>



</details>
