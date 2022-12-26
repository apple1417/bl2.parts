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
