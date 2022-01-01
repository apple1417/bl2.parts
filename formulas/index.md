---
latex: true
---

# General Formulas
There are three general formulas used all over the game.

### Base Scaling Formula
As you level up, most numbers in the game tend to get bigger. The base values for all these numbers
are just multiples of the Base Scaling Formula.

For convience, other pages refer to this formula by &beta;.

{% comment %}
This looks a little awkward, but it's better than trying to squish everything into one line in a
markdown table.
{% endcomment %}
<style>
#base_scaling_table mjx-container {
    margin: 0;
}
</style>
<table id="base_scaling_table"><thead><tr>
    <th>BL2</th><th>TPS</th>
</tr></thead><tbody><tr>
<td markdown="1">
<code markdown="span" class="latex-fallback">&beta; = 1.13 ^ Level</code>

$$\beta = 1.13 ^ \text{Level}$${:hidden="1" .latex-content}
</td><td markdown="1">
<code markdown="span" class="latex-fallback">&beta; = 1.10 ^ Level</code>

$$\beta = 1.10 ^ \text{Level}$${:hidden="1" .latex-content}
</td>
</tr></tbody></table>

### Attribute Bonus Formula
Any attribute in the game uses this formula to calculate it's final value from it's various bonuses.
Some stats are comprised of multiple attributes, this is not always the final value.

<code markdown="span" class="latex-fallback">
Final = [(Base + *PreAdd*{:.pre-add}) &times;
(1 + *Positive Scale*{:.scale})&divide;(1 - *Negative Scale*{:.scale})]
\+ *PostAdd*{:.post-add})
</code>

$$
\text{Final} = 
\left(
\left(\text{Base} + \sum \class{pre-add}{\text{PreAdd}}\right)
\times \frac{
    1 + \sum \class{scale}{\text{Positive Scale}}
}{
    1 - \sum \class{scale}{\text{Negative Scale}}
}
\right)
+ \sum \class{post-add}{\text{PostAdd}}
$$
{:hidden="1" .latex-content}

Any bonus falls into one of these four modifier types, and all bonuses of a type are summed together
before being applied. The detailed calculation pages colour code bonuses based on their modifier
type.

Note that the game only distingishes between positive and negative scale values based on the final
value of the bonus. This means that if a scale bonus is based on some complex formula, it will be
treated differently if the formula resolves to a positive value than if it resolves to a negative.

### Grade Bonus Formula
Weapons and Items use a concept called Grades. Each part can add or remove grades of a particular
name, and if the weapon or item has defined a grade bonus using that name, it gets converted into a
standard bonus.

Grades are defined by three things: their modifier type, their base value, and a per-grade multiplier.

<code markdown="span" class="latex-fallback">
Bonus = Base + (PerGrade &times; *Grades*{:.grade})
</code>

$$
\text{Bonus} = \text{Base} + \left(\text{PerGrade} \times \sum \class{grade}{\text{Grades}}\right)
$$
{:hidden="1" .latex-content}

The detailed calculation pages again colour code grade bonuses.
