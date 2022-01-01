# Status Effect Chance

Status Effect Chance isn't just made of a single modifier like the other attributes.

There are 4 values that contribute to the final chance, which all get multiplied together.
- Status Chance Base
- Status Chance Modifier
- Surface Chance Modifier
- Target's Status Chance Resistance

The Surface Chance Modifier is hardcoded, based on element.

Surface Type | *Fire*{:.no-i.fire} | *Shock*{:.no-i.shock} | *Corrosive*{:.no-i.corrosive} | *Slag*{:.no-i.slag} | *Cryo*{:.no-i.cryo}
---|---|---|---|---|---
Generic | 20% | 20% | 20% | 30% | 15%
Flesh   | 30% | 15% | 15% | 30% | 15%
Armor   | 15% | 15% | 30% | 30% | 15%
Shield  | 15% | 75% | 15% | 30% |  5%

Item cards use the Generic value, along with a Target Status Chance Resistance of 1.
