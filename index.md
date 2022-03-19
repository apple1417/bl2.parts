---
hide_sidebar: true
title: Home
---

# BL2/TPS Parts Guides

<style>
    #parts {
        display: grid;
        margin: 0 auto;
        max-width: calc(2*var(--img-size-standard));
        grid-template-columns: repeat(4, minmax(var(--img-size-standard)/2, 0.5fr));
        grid-gap: 1px;
    }
    #parts a {
        display: flex;
        justify-content: center;
        align-items: center;
        border: var(--border-format);
        border-style: hidden;
        margin: -1px;
    }
    #parts .L { border-left-style: solid; margin-left: -1px; }
    #parts .T { border-top-style: solid; margin-top: -1px; }
    #parts .R { border-right-style: solid; margin-right: -1px; }
    #parts .B { border-bottom-style: solid; margin-bottom: -1px; }

    #misc {
        width: 21em;
        border-top: var(--border-format);
        margin: 0 auto;
        text-align: center;
        margin-top: 1em;
    }
    #misc a {
        color: var(--text-colour);
        font-size: 1.75em;
        display: block;
        margin-top: 0.25em;
        margin-bottom: 0.25em;
    }

    #footer {
        color: var(--footnote-colour);
        font-size: 0.75em;
        margin: 1em auto;
        text-align: center;
    }
</style>
<div id="parts">
    <a style="grid-area: 1/1/2/3;" class="R B" href="/pistols">
        <img class="med" src="/^images/pistols.png" alt="Pistol Parts Guide">
    </a>
    <a style="grid-area: 1/3/2/5;" class="B" href="/shotguns">
        <img class="med" src="/^images/shotguns.png" alt="Shotgun Parts Guide">
    </a>
    <a style="grid-area: 2/1/3/3;" class="R" href="/shields">
        <img class="med" src="/^images/shields.png" alt="Shield Parts Guide">
    </a>
    <a style="grid-area: 2/3/3/5;" href="/grenades">
        <img class="med" src="/^images/grenades.png" alt="Grenade Parts Guide">
    </a>
</div>
<div id="misc">
    {% assign sorted_items = site.data.nav.misc | sort_natural: "title" %}
    {% for item in sorted_items %}
        <a href="{{ item.url }}">{{ item.title }}</a>
    {% endfor %}
</div>
<div id="footer">
    Think you've found an error? Ask me on Discord, apple#7804
</div>
