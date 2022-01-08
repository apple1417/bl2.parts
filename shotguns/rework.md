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
    image_class="small"
    parts=site.data.shotguns.sights
    meta=site.data.shotguns_meta
    mesh_image=true
    simple_bonuses=true
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
The element parts have no model, but instead add lights over the weapon in their relevant colours.
There are six non-unique element parts, one for each element, and one for no element. None of them
give any stat bonuses, good or bad. 

### Material
The material parts also have no model, instead defining the actual textures applied ontop of all the
other models.

There are 29 non-unique material parts. Like with bodies, there's one for each rarity-manufacturer
combination. In Tina DLC, each manufactuer gets an additional gemstone material, and in TPS,
Hyperion has an additional "Old Hyperion" material per rarity.

Most materials provide no stat bonuses. The exceptions are listed below.
{% assign bonus_materials = site.data.shotguns.materials | where_exp: "part", "part.bonuses" %}
{% include parts.html
    parts=bonus_materials
    meta=site.data.shotguns_meta
    simple_bonuses=true
    uniques=true
%}

### Weapon Balance
The Weapon Balance defines what parts a certain weapon can have. Balances themselves do not affect
stats, but are they very important for the actual generation of weapons.

### Weapon Type Definition
Like the name might suggest, the definition basically defines each weapon type. It defines all the
base values of each stat, how exactly certain bonuses affect those stats, as well as several other
properties relating to how exactly the weapon behaves. There is one weapon type per manufactuerer.

On top of everything else, weapon definitions can also provide bonuses of their own.

{% include parts.html
    parts=site.data.shotguns.definitions
    meta=site.data.shotguns_meta
    simple_bonuses=true
%}
