---
purple_body_names:
 - GD_Weap_Shotgun.Body.SG_Body_Bandit_4
 - GD_Weap_Shotgun.Body.SG_Body_Hyperion_4
 - GD_Weap_Shotgun.Body.SG_Body_Jakobs_4
 - GD_Weap_Shotgun.Body.SG_Body_Tediore_4
 - GD_Weap_Shotgun.Body.SG_Body_Torgue_4
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
{% include part_reference.html id="part_reference" parts=site.data.shotguns_meta.part_reference %}

Other parts include the element, the material, weapon balance, and the weapon type definition.

### Accessory
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
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
%}

All accessories have set prefixes associated with them based on manufacturer, which, assuming they
don't get overwritten, are a simple way to tell which one exactly a weapon has. Click
[here](/shotguns/prefixes/) for a table showing these.

### Barrel
There are 7 non-unique barrels.

{% include parts.html 
    image_class="big"
    parts=site.data.shotguns.barrels
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
%}

### Bodies
There are 20 non-unique bodies, one for each rarity-manufacturer combination. All bodies of the
same rarity share the same stats.

<style>
#bodies > div:nth-child(2) > img {
    max-width: var(--img-size-big);
    min-height: var(--img-size-standard)
}
</style>
{% assign purple_bodies = site.data.shotguns.bodies
                          | where_exp: "body", "page.purple_body_names contains body._obj_name" %}
{% include parts.html
    id="bodies"
    parts=purple_bodies
    meta=site.data.shotguns_meta
    mesh_image=true
    hide_bonuses=true
%}

{% include body_table.html 
    meta=site.data.shotguns_meta
    common="GD_Weap_Shotgun.Body.SG_Body_Bandit"
    uncommon="GD_Weap_Shotgun.Body.SG_Body_Bandit_2"
    rare="GD_Weap_Shotgun.Body.SG_Body_Bandit_3"
    very_rare="GD_Weap_Shotgun.Body.SG_Body_Bandit_4"
    simple_bonuses=true
%}

### Grips
There are 5 non-unique grips.

{% include parts.html 
    parts=site.data.shotguns.grips
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
%}

### Sights
There are 6 non-unique sights, including a "no sight" part with no model. Some sight bonuses are
only applied while aiming.

{% include parts.html 
    parts=site.data.shotguns.sights
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
    allowed_restrictions="Zoom"
%}

Click [here](/shotguns/zoom/) for a comparison of the zoom level of each sight.

### Stocks
There are 5 non-unique stocks.
{% include parts.html 
    parts=site.data.shotguns.stocks
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
%}

### Element
Element is one of the miscellaneous parts. They have no model, but instead add lights over the
weapon in that element's colours. There are six non-unique element parts, one for each element, and
one for no element. None of them give any bonuses. 
