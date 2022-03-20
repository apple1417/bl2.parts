---
description: How status effect chance, and the various status chance attributes, work.

redirect_from:
  - /statuschance/

chance_attributes:
- D_Attributes.Weapon.WeaponBaseStatusEffectChanceModifier
- D_Attributes.Weapon.WeaponStatusEffectChanceModifier
resistance_attributes:
- D_Attributes.StatusEffectModifiers.AmpChanceResistanceModifier
- D_Attributes.StatusEffectModifiers.CorrosiveChanceResistanceModifier
- D_Attributes.StatusEffectModifiers.IgniteChanceResistanceModifier
- D_Attributes.StatusEffectModifiers.ShockChanceResistanceModifier
- D_Cork_Attributes.StatusEffectModifiers.FreezeChanceResistanceModifier
---

# Status Effect Chance

Status Effect Chance isn't just made of a single modifier like the other attributes. There are in
fact 8 different attributes that contribute to the final chance, which all get multiplied together.

{% include attributes.html filter=page.chance_attributes %}

The Target's Status Chance Resistance also plays a role.

{% include attributes.html filter=page.resistance_attributes %}

The final value is the Surface Chance Modifier, which is hardcoded based on element and surface.

Surface Type | *Corrosive*{:.corrosive} | *Cryo*{:.cryo} | *Fire*{:.fire} | *Shock*{:.shock} | *Slag*{:.slag} 
---|---|---|---|---|---
Generic | 20% | 15% | 20% | 20% | 30% 
Flesh   | 15% | 15% | 30% | 15% | 30% 
Armor   | 30% | 15% | 15% | 15% | 30% 
Shield  | 15% |  5% | 15% | 75% | 30% 

Item cards use the Generic value, along with a Target Status Chance Resistance of 1.
