---
description: How status effect chance, and the various status chance attributes, work.
latex: true

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
fact 7 different attributes and 2 hardcoded tables that all contribute to the final chance.

The first hardcoded table is the Surface Chance Modifier. This is essentially the base value, it
sets a base status chance depending on the surface type being attacked.

Surface Type | *Corrosive*{:.corrosive} | *Cryo*{:.cryo} | *Fire*{:.fire} | *Shock*{:.shock} | *Slag*{:.slag} 
--------|-----|-----|-----|-----|-----
Generic | 20% | 15% | 20% | 20% | 30%
Flesh   | 15% | 15% | 30% | 15% | 30%
Armour  | 30% | 15% | 15% | 15% | 30%
Shield  | 15% |  5% | 15% | 75% | 30%

<small>
Item cards use the Generic value.
</small>

Then the two main attributes which modify status chance are the following:

{% include attributes.html filter=page.chance_attributes %}

The Target's Status Chance Resistance also plays a role.

{% include attributes.html filter=page.resistance_attributes %}

<small>
Item cards assume a Target Status Chance Resistance of 1.
</small>

Finally, the other hardcoded table is the Playthrough 3 Scalar. This only applies in BL2, only in
UVHM, and only when the world level is 73 or above. This was intended to apply only in OP levels,
but was never updated after Fight For Sancturary - so mods often move it back up to 81 or above. It
scales based on the level difference between the attacker and target - making it harder to apply
status effects to higher level targets.

`Target Level - Attacker Level` | Scalar
------|-------
 >= 7 | x0.6
 5, 6 | x0.7
 3, 4 | x0.8
 1, 2 | x0.9
 <= 0 | x1.0

<small>
Item cards ignore this, and always use x1.0.
</small>

## Combining Modifiers
So how do we combine all these values? For once, it's simple, they're just all multiplied together.

Let's work through an example. Let's say we have a full-Maliwan Fire Laser. The relevant values are:
- Maliwan Lasers have 1.0 base Status Chance Base.
- Status Chance Modifier is a multiplicative attribute, with a base value of 1.0.
- Maliwan Definition gives *+0.2*{:.pre-add} Status Chance Modifier.
- Maliwan Barrel gives *&minus;2.0*{:.scale} Status Chance Modifier, and on Maliwan weapons also gives *+0.15*{:.scale} Status Chance Base.
- Maliwan Grip gives *+0.15*{:.scale} Status Chance Modifier.
- Fire on Generic uses a Surface Chance Modifier of 0.2.

Firstly, we can calculate the final values of the two attributes.

<code markdown="span" class="latex-fallback">
Status Chance Base = (1.0 + *[0]*{:.pre-add})
                     &times; (1 + *[0.15]*{:.scale})
                     &divide; (1 &minus; *[0]*{:.scale})
                     + *[0]*{:.post-add}
<br>
Status Chance Base = 1.0 &times; *1.15*{:.scale}
<br>
Status Chance Base = 1.15
<br>
Status Chance Modifier = (1.0 + *[0.2]*{:.pre-add})
                         &times; (1 + *[0.15]*{:.scale})
                         &divide; (1 &minus; *[&minus;2.0]*{:.scale})
                         + *[0]*{:.post-add}
<br>
Status Chance Modifier = (1.0 + *0.2*{:.pre-add}) &times; *1.15*{:.scale} &divide; *3.0*{:.scale}
<br>
Status Chance Modifier = 0.46
</code>

$$
\begin{align}
\text{Status Chance Base} &=
\left(
  \left(
    1.0 + \sum \class{pre-add}{\left\{\right\}}
  \right)
  \times \frac{
    1 + \sum \class{scale}{\left\{ 0.15 \right\}}
  }{
    1 - \sum \class{scale}{\left\{\right\}}
  }
\right)
+ \sum \class{post-add}{\left\{\right\}}
\\
\text{Status Chance Base} &= 1.0 \times \class{scale}{1.15}
\\
\text{Status Chance Base} &= 1.15
\\
\text{Status Chance Modifier} &=
\left(
  \left(
    1.0 + \sum \class{pre-add}{\left\{ 0.2 \right\}}
  \right)
  \times \frac{
    1 + \sum \class{scale}{\left\{ 0.15 \right\}}
  }{
    1 - \sum \class{scale}{\left\{ -2.0 \right\}}
  }
\right)
+ \sum \class{post-add}{\left\{\right\}}
\\
\text{Status Chance Modifier} &= \left(
  1.0 + \class{pre-add}{0.2}
\right)
\times \frac{\class{scale}{ 1.15 }}{\class{scale}{3.0}}
\\
\text{Status Chance Modifier} &= 0.46
\end{align}
$$
{:hidden="1" .latex-content}

<small>
Since item cards ignore the Target Status Chance Resistance, we don't need to calculate it.
</small>

Then we can combine these to get the value on the card:

<code markdown="span" class="latex-fallback">
Card = *Fire*{:.fire}-Generic Surface Chance Modifier
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&times; Status Chance Base
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&times; Status Chance Modifier
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&times; Target Status Chance Resistance (*Fire*{:.fire})
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&times; Playthrough3 Scalar
<br>
Card = 0.2 &times; 1.15 &times; 0.46 &times; 1.0 &times; 1.0
<br>
Card = 0.1058 = 10.58%
</code>

$$
\begin{align}
\text{Card} &= \class{fire}{\text{Fire}}\text{-Generic Surface Chance Modifier}
\\
  &\phantom{=} \times \text{Status Chance Base}
\\
  &\phantom{=} \times \text{Status Chance Modifier}
\\
  &\phantom{=} \times \text{Target Status Chance Resistance (}\class{fire}{\text{Fire}}\text{)}
\\
  &\phantom{=} \times \text{Playthrough 3 Scalar}
\\
\text{Card} &= 0.2 \times 1.15 \times 0.46 \times 1.0 \times 1.0
\\
\text{Card} &= 0.1058 \approx 10.6\%
\end{align}
$$
{:hidden="1" .latex-content}

Of course in practice, the actual chance will vary slightly based on the actual surface type and
target resistances (and the Playthrough 3 Scalar, if this were BL2).
