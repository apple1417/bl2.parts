# Data Formats

## `attributes.yml`
This entire file is an array of attribute data entries.

```yml
- obj: D_Attributes.Weapon.WeaponDamage
  name: Weapon Damage
  description: Increases the damage your weapon deals.
  percent: false
  add_good: true
  multi_good: true
  invalid: false
```

Field | Usage
:---|:---
`obj` | The attribute's object name.
`name` | The attribute's display name.
`description` | A description of the attribute, and what happens when it gets more positive. Use the word "Multiplicatively" when an attribute has a base value of 1, and directly multiplies it's stat.
`percent` | If to display simple addition bonuses as a percentage.
`add_good` | If adding to the value gives a good outcome.
`multi_good` | If multiplying the value gives a good outcome.
`invalid` | If this attribute definition is invalid, and doesn't even resolve to a field. Ignores all bonuses to this attribute.

Attributes which resolve to a valid field but don't appear to do anything should still be defined normally, don't set invalid on them - it's always possible they actually do something minor, and mods can use them as input to something else.

## `nav.yml`
This file contains two arrays of navbar entries. The `parts` array is displayed at the top of the navbar, and the `misc` array is displayed below, below a `<hr>`.

Each entry uses the following format:
```yml
- title: Grenades
  url: /grenades/
  sub: []
```

Field | Usage
:---|:---
`title` | The title to display on the navbar.
`url` | The url to link to.
`sub` | A recursive list of other navbar entries to display under this one.

## Item Type Files
The remaining files define all the data for a certain item type. Each file consists of a mapping of slots to a list of parts for that slot. The special key `meta` is an exception, instead holding metadata on the item type.

### Formulas
The part data is filled with numbers. In a most cases, these will be constant. If this is not the case, an additional formula block is used, named using the base field with `_formula` suffixed.

```yml
my_value: 123
my_value_formula:
  multiplier_str: &beta;
  offset: 4.56
```

All fields within the formula object are optional, but at least one must exist if the formula field is defined. If the formula field is not defined, the base value is simply taken as constant.

Field | Usage
:---|:---
`multiplier_str` | A string to display as a multiplier of the value, mostly intended for bonuses which scale with the base scaling constant.
`offset` | A constant offset to add to the end of the base value. Is not multiplied by `multiplier_str`.

The above example defines the formula `(123 * &beta;) + 4.56`.

`multiplier_str` Value | Meaning
:---|:---
`&beta;` | The base scaling constant.
`[Shield Level]` | The level of the shield this bonus is on.

### Part Data
```yml
- _obj_name: GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_2
  bonuses:
  - attribute: D_Attributes.DamageSourceModifiers.InstigatedMeleeDamageModifier
    type: pre-add
    value: 0.5
  mesh: Acc_Barrel_Blade2
  name: Bayonet 2
  prefixes:
  - name: Baynaneted
    restrict: Bandit
  unique: false
```

Field | Usage
:---|:---
`_obj_name` | The part's object name - not actually used on the site, more for internal reference.
`bonuses` | An array of bonuses entries the part gives. Optional.
`mesh` | The mesh the part uses. Optional.
`name` | The part's display name.
`prefixes` | An array of prefixes the part can spawn with. Optional, should only really be used for non-unique accessories.
`unique` | If the part is a unique part, which generic items can't spawn with.

### Bonus Entries
Field | Usage
:---|:---
`attribute` | The object name for the attribute this bonus affects. Optional.
`slot` | The name of the grade slot this bonus affects. Optional.
`type` | The type of the bonus (using the css class names).
`restrict` | A restriction object holding restrictions on this bonus. Optional, no restrictions if not defined.
`value` | The value of the bonus.
`value_formula` | An additional formula object, used to work out the actual value. Optional.

If a bonus' `type` is `grade`, `slot` must be defined and `attribute` must not, otherwise `attribute` must be and `slot` must not.

### Bonus Restrictions
```yml
restrict:
  manu: Dahl
  zoom: true
```

As with formulas, all fields are optional, but at least one must exist.

Field | Usage
:---|:---
`manu` | A string holding the manufacturer this bonus applies on. 
`post_init` | If true, this bonus only applies after item initialization (and doesn't show on the item card).
`zoom` | If true, this bonus only applies while zoomed.

### Prefix Entries
Field | Usage
:---|:---
`name` | The prefix's display name.
`restrict` | The restriction (i.e. manufacturer) under which this prefix is used.

### Item Metadata
Field | Usage
:---|:---
`definitions` | An array of definitions. Note that there is generally also a part slot called `definitions`, but it contains the bonuses the definitions give, while this one contains what they defines.
`grade_overrides` | A mapping of grade slot names to custom data which overwrites looking up the attribute in the definition.
`meshes` | A mapping of mesh names to their display names and images.
`standard_definition_idx` | An index into the definitions array to use as the "standard definition", used when converting grade bonuses.

### Grade Override Entries
```yml
grade_overrides:
  Special01:
    name: Special 01
    add_good: true
    hide: false
```

Field | Usage
:---|:---
`attr` | The object name of the attribute this grade slot should be assigned to. To be used if it doesn't exist in the standard definition. Optional.
`name` | The grade slot's display name.
`add_good` | If adding to the value gives a good outcome.
`hide` | If to hide the grade slot - to be used if it doesn't actually exist. Optional.

If `attr` is defined (and points to a valid object), the other fields are ignored.

When displaying simple bonuses, any grades defined using these won't get their values converted, they'll show the raw grade bonus.

### Mesh Entries
```yml
meshes:
  Acc_Barrel_Blade1:
    name: Bayonet 1
    src: /pistols/^images/accessories/bayonet_1.png
  Acc_Barrel_Blade2:
    name: Bayonet 2
    src: /pistols/^images/accessories/bayonet_2.png
  Acc_Barrel_Elemental1:
    invalid: true
```

Field | Usage
:---|:---
`name` | The mesh's display name.
`src` | The url of the image for the mesh.
`invalid` | If this mesh doesn't actually exist, used to act as if there's no mesh assigned. Optional, other options are not required if this is defined.

### Definition Entries
```yml
  - _obj_name: GD_Weap_Pistol.A_Weapons.WeaponType_Bandit_Pistol
    base:
    - attribute: D_Attributes.Weapon.WeaponDamage
      scale: '&beta;'
      value: 11.36
    grades:
    - attribute: D_Attributes.Weapon.WeaponDamage
      base: 0
      per_grade: 0.03
      slot: WeaponDamage
      type: scale
    name: Bandit
    unique: false
```

Field | Usage
:---|:---
`_obj_name` | The definition's object name - not actually used on the site, more for internal reference.
`base` | An array of base values for various stats that the definition defines.
`grades` | An array of grades the definition defines.
`name` | The definition's display name.
`unique` | If the part is a unique part, which generic items can't spawn with.

### Definition Base Entries
Field | Usage
:---|:---
`attribute` | The object name for the attribute this entry sets the base value of.
`value` | The base value.
`value_formula` | An additional formula object, used to work out the actual value. Optional.

### Definition Grade Entries
```yml
- attribute: D_Attributes.Shield.PercentChanceToAbsorbLaser
  base: 0.00108
  base_formula:
    multiplier_str: '[Shield Level]'
    offset: 0.12
  per_grade: 0.000135
  per_grade_formula:
    multiplier_str: '[Shield Level]'
    offset: 0.12
  slot: Special01
  type: pre-add
```

Field | Usage
:---|:---
`attribute` | The object name for the attribute this grade affects.
`base` | The base value of the grade, which is always applied.
`base_formula` | An additional formula object, used to work out the actual base value. Optional.
`per_grade` | The per-grade value of the grade.
`per_grade_formula` | An additional formula object, used to work out the actual per-grade value. Optional.
`slot` | The grade's slot name.
`type` | The type of the bonus the grade maps to.
