---
latex: true
---

# A Note on Calculation Order

If you've tried manually calculating item stats before, you might have noticed you start having
issues if you try include other bonuses. In fact, you'll probably have noticed only item/weapon
parts seem to work as stated. Why is this? Because the game actually changes the base value of these
stats inbetween applying the bonuses.

At the start of item/weapon initalization, each attribute will have a certain base value, which
you'll find listed in all the part guides. The game applies all bonuses from the parts, finding the
value that displays on the item card. It then sets the base value to this calculated value, and
removes all the part bonuses so they don't apply twice. Any bonus applied after item initalization
will work off of this new base value instead.

Note that this does not affect all attributes, testing shows that it's only those stored on the
weapon/item. Unfortuantly the functions controlling this do not decompile, so this can't be 100%
confirmed.

## Example
The Fibber is a great example of how this works. The barrel gives many large bonuses, which are
incorporated into the new base value that is shown on the card. A BPD then enables extra bonuses
after item initalization to give it it's actual stats.

To make things easy in this example, we'll look at the mag size on a Maliwan grip Crit Fibber, with
no accessory. In game this gives 1970 mag size on the card, but 15 in reality.

{% comment %} TODO: pull these numbers from part data files? {% endcomment %}
The relevant numbers here are:
- Hyperion Pistols have 15 base mag size
- Mag size Grades on Hyperion Pistols are *0 +0.07*{:.scale.per-grade}
- Blue Hyperion Body gives *+5*{:.grade}
- The Crit Fibber's Barrel gives *+130*{:.scale}
- The Crit Fibber's BPD gives *-128*{:.scale}, which is applied after initalization
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
