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
