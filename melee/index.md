---
latex: true
---

# Melee Damage
Melee Damage depends on 4 values: the Melee Definition; the Attacker's Level; and the Melee Damage
and Roid Damage bonuses.

Like with weapons or items, the Melee Definition defines the exact formula used to get the final
melee damage. Most of these have the same standard formula, but some are slightly different.

{% comment %} Fitting all this into a markdown table would be hell {% endcomment %}
<style>
#melee_formula_table mjx-container {
    display: table-cell;
}
#melee_formula_table .latex-content {
    color: #ddd;
    margin-top: 0.2em;
}
</style>
<table id="melee_formula_table" class="left"><tr>
    <th>Standard {%- include footnote.html id="accessory" %}</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 2.5 &times; (8 &times; &beta; + Roid Bonus)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 2.5 \times \left(8 \times \beta + \text{Roid Bonus}\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Krieg</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times;
                (16 &times; &beta; &times; (0.02 &times; Level + 1)
                + (2.5 &times; Roid Bonus))
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times
                \left(16 \times \beta \times \left(0.02 \times \text{Level} + 1\right)
                + \left(2.5 \times \text{Roid Bonus}\right)\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Nisha {%- include footnote.html id="thunder_crackdown" %}</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 1.875 &times; (8 &times; &beta; + Roid Bonus)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 1.875 \times \left(8 \times \beta + \text{Roid Bonus}\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Buzz Axe Rampage</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times;
                (80 &times; &beta; &times; (0.02 &times; Level + 1)
                + (2.5 &times; Roid Bonus))
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times
                \left(80 \times \beta \times \left(0.02 \times \text{Level} + 1\right)
                + \left(2.5 \times \text{Roid Bonus}\right)\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Deathtrap</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times;
                (8 &times; &beta; + (3.5 &times; Roid Bonus))
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times
                \left(8 \times \beta + \left(3.5 \times \text{Roid Bonus}\right)\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Deathtrap Frenzy{%- include footnote.html id="frenzy_end" %}</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 0.62 &times;
                (8 &times; &beta; + (3.5 &times; Roid Bonus))
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 0.62 \times
                \left(8 \times \beta + \left(3.5 \times \text{Roid Bonus}\right)\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Execute</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 5 &times; (8 &times; &beta; + Roid Bonus)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 5 \times \left(8 \times \beta + \text{Roid Bonus}\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Fist Full of Hurt</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 10 &times; (8 &times; &beta; + Roid Bonus)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 10 \times \left(8 \times \beta + \text{Roid Bonus}\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Backhand to Remember</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 96 &times; &beta; &times;
                (0.02 &times; Level + 1)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 96 \times \beta \times
                \left(0.02 \times \text{Level} + 1\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Blood Rush</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 3.75 &times; (8 &times; &beta; + Roid Bonus)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 3.75 \times \left(8 \times \beta + \text{Roid Bonus}\right)
            $$
        </div>
    </td>
</tr><tr>
    <th>Power Fist</th>
    <td>
        <code class="latex-fallback">
            Melee Bonus &times; 80 &times; &beta; &times;
                (0.02 &times; Level + 1)
        </code>
        <div class="latex-content" hidden>
            $$
            \text{Melee Bonus} \times 80 \times \beta \times
                \left(0.02 \times \text{Level} + 1\right)
            $$
        </div>
    </td>
</tr></table>


{% include footnote_end.html
    accessory="Melee weapon accessories force using this definition even if the character has
               others."
    thunder_crackdown="Does not include Thunder Crackdown, which uses the standard formula."
    frenzy_end="Does not include the \"Frenzy End\" Melee Definition, which uses the standard
                Deathtrap formula."
%}

## A Note on Roid Shields
When following these formulas, it would make sense to plug in the value straight from your shield's
item cards right? Well this is Gearbox we're talking about.

These formulas use the *calculated* roid damage, not the *displayed* damage. The displayed
roid damage is 2.5&times; the calculated damage.

In practice, these formulas almost always end up also multiplying the calculated damage by 2.5, so
it is possible to rearrange them to take the displayed value instead. Roid Shields are the only
vanilla items to give this bonus type, so this should always still line up.
