---
description: How to calculate item stats from scratch.
latex: true
---
# Calculation Guide
Using the information contained on the various parts pages, you can calculate the exact stats of
your items from scratch.

## Base Scaling Formula
Firstly, one of the most important formulas to know is the Base Scaling Formula. A lot of stats get
bigger as you level up, all of these are eventually based on some multiple of this formula.

For convenience, other pages refer to this formula by &beta;.

<style>
#base_scaling_table mjx-container {
    margin: 0;
}
</style>
<table id="base_scaling_table"><thead><tr>
    <th>BL2</th><th>TPS</th>
</tr></thead><tbody><tr>
    <td>
        <code class="latex-fallback">&beta; = 1.13 ^ Level</code>
        <span class="latex-content" markdown="1" hidden>$$\beta = 1.13 ^ \text{Level}$$</span>
    </td><td>
        <code class="latex-fallback">&beta; = 1.10 ^ Level</code>
        <span class="latex-content" markdown="1" hidden>$$\beta = 1.10 ^ \text{Level}$$</span>
    </td>
</tr></tbody></table>

## Bonus Types
All bonuses in the game fit into one of four modifier types:
 - *PreAdd*{:.pre-add}
 - *Scale*{:.scale}
 - *PostAdd*{:.post-add}
 - *Grade*{:.grade}

If you've checked out the full part reference, or the definition sections at the bottom of the main
part guides, you'll have seen bonuses colour coded into the different types.

## Grade Bonus Formula
Grade bonuses are a little different to the other three, and have to be evaluated first. Weapon and
item definitions can define a set of "grade slots", each of which have a name and a bonus to apply.
Parts can add grades to slot names, and, if that name exists on the relevant definition, it
increases the bonus's value.

Shields are the best example of grades - all shield definitions put their special effect under the
same "Special[n]" slot names, but with different bonuses, meaning a part which boosts special will
correctly boost all the different special effects regardless of shield type.

Grades are defined by three things: their modifier type, their base value, and a per-grade
multiplier. These values are listed under the definitions part in each part guide, in the format
"*&plusmn;Base &plusmn;PerGrade*{:.scale .per-grade}".

<code markdown="span" class="latex-fallback">
Bonus = Base + (PerGrade &times; *Grades*{:.grade})
</code>

$$
\text{Bonus} = \text{Base} + \left(\text{PerGrade} \times \sum \class{grade}{\text{Grades}}\right)
$$
{:hidden="1" .latex-content}

## Attribute Bonus Formula
Once you've converted grades into one of the base modifier types, you can apply the attribute bonus
formula. Every attribute in the game uses this formula to apply it's various bonuses.

<code markdown="span" class="latex-fallback">
Final = [(Base + *PreAdd*{:.pre-add}) &times;
(1 + *Positive Scale*{:.scale})&divide;(1 &minus; *Negative Scale*{:.scale})]
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

This formula makes a distinction between positive and negative scale values, based on the final
value of the bonus. This means that if a scale bonus is based on a formula (e.g. the grade bonus
formula), it will be treated differently if the formula resolves to a positive value than if it
resolves to a negative.

Once you've gathered all the bonuses and put them, through this formula, you have the attribute's
final value. Note that some stats are comprised of multiple attributes, this is not always the final
value of the stat your interested in.

## Base Value Recomputation
So with the above knowledge, you should be able to correctly calculate item stats from their parts.
If you try including other bonuses, from skills or other items, you might have noticed you start
having issues. This is because the game actually changes the base value of all stats stored on the
item during initialization.

At the start of item initialization, each attribute has it's regular base value, which you can find
listed in each of the part guides. The game then applies all bonuses from the parts, finding the
value that displays on the item card. Near the end of initialization, it recomputes the base values
of these stats. It grabs the calculated final value, sets the base value to it, and removes all the
part bonuses so they don't apply twice. Any bonus applied after item initialization will work off of
this new base value instead.

### Fibber Example
The Fibber is a great example of how this works. The barrel gives many large bonuses, which are
incorporated into the new base value that is shown on the card. A BPD then enables extra bonuses
after item initialization to give it it's actual stats.

To make things easy in this example, we'll look at the mag size on a Crit Fibber, with Maliwan grip
and no accessory. In game this gives 1970 mag size on the card, but 15 in reality.

The relevant values here are:
- Hyperion Pistols have 15 base mag size
- Mag size grades on Hyperion Pistols are *0 +0.07*{:.scale.per-grade}
- Blue Hyperion Body gives *+5*{:.grade}
- The Crit Fibber's Barrel gives *+130*{:.scale}
- The Crit Fibber's BPD gives *-128*{:.scale}, which is applied after initialization
- Mag size is stored as an integer, so decimals are truncated.

Using these numbers we can calculate both values we observed earlier as follows:

<code markdown="span" class="latex-fallback">
    Card = floor((15 + *[0]*{:.pre-add})
        &times; (1 + <span class="scale">[130 + (0 + 0.07 &times; *[5]*{:.grade})]</span>)
        &divide; (1 &minus; *[0]*{:.scale})
        + *[0]*{:.post-add})
    <br>
    Card = floor(15 &times; (1 + *130.35*{:.scale}))
    <br>
    Card = floor(1970.25) = 1970
    <br>
    <br>
    Final = floor((1970 + *[0]*{:.pre-add})
        &times; (1 + *[0]*{:.scale})
        &divide; (1 &minus; *[&minus;128]*{:.scale})
        + *[0]*{:.post-add})
    <br>
    Final = floor(1970 &divide; (1 &minus; *&minus;128*{:.scale}))
    <br>
    Final = floor(15.271...) = 15
</code>

$$
\begin{align}
\text{Card} &= 
\left\lfloor\left(
\left(15 + \sum \class{pre-add}{\left\{\right\}}\right)
\times \frac{
    1 + \sum \class{scale}{\left\{
        130, 0 + 0.07 \times \class{grade}{\sum \left\{5\right\}}
    \right\}}
}{
    1 - \sum \class{scale}{\left\{\right\}}
}
\right)
+ \sum \class{post-add}{\left\{\right\}}
\right\rfloor
\\
\text{Card} &= \left\lfloor 15 \times \left(1 + \class{scale}{130.35}\right) \right\rfloor
\\
\text{Card} &= \left\lfloor 1970.25 \right\rfloor = 1970
\\ \\
\text{Final} &= 
\left\lfloor\left(
\left(1970 + \sum \class{pre-add}{\left\{\right\}}\right)
\times \frac{
    1 + \sum \class{scale}{\left\{\right\}}
}{
    1 - \sum \class{scale}{\left\{-128\right\}}
}
\right)
+ \sum \class{post-add}{\left\{\right\}}
\right\rfloor
\\
\text{Final} &= \left\lfloor 1970 \times \frac{1}{1 - \class{scale}{-128}} \right\rfloor
\\
\text{Final} &= \left\lfloor 15.271\dots \right\rfloor = 15
\end{align}
$$
{:hidden="1" .latex-content}
