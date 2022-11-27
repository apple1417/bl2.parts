---
description: How continuous damage, and the various continuous damage attributes, work.

latex: true

attributes:
  - D_Attributes.Weapon.WeaponContinuousDamageScale
  - D_Attributes.WeaponContinuousDamageResourcePool.ContinuousDamage_MaxValue
  - D_Attributes.WeaponContinuousDamageResourcePool.ContinuousDamage_OnIdleRegenerationRate
  - D_Attributes.WeaponContinuousDamageResourcePool.ContinuousDamage_OnIdleRegenerationDelay
---
# Continuous Damage 
Some weapon definitions in TPS support continuous damage bonuses - the longer you shoot, the more
damage you deal. If the weapon definition does not support continuous damage, any bonuses do
nothing.

Continuous damage uses a hit counter - each time you hit an enemy, it grows a little, and after an
idle period it starts decaying. The continuous damage attributes only affect this counter.

{% include attributes.html filter=page.attributes %}

It's worth noting that the hit counter is *not* an integer value. Different guns can add vastly
different amounts on hit due to different Continuous Damage Impulse bonuses.

Continuous Damage Delay defaults to 0.5s, and Continuous Damage Regen defaults to -0.5/s. The other
attributes all default to zero.

On each shot, the value of the hit counter is fed through the following formula to get the final
continuous damage bonus.

<code class="latex-fallback">
    Final Damage = Card Damage &times; (0.8 + 0.8 &times; Hit Counter)
</code>
<div class="latex-content" hidden>
    $$
    \text{Final Damage} = \text{Card Damage} \times (0.8 + 0.8 \times \text{Hit Counter})
    $$
</div>

As the formula suggests, weapons which support continuous damage actually start out at below their
listed damage, and only reach it once the hit counter passes 0.25.
