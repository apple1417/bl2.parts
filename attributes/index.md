---
description: All attributes that item parts boost, and their effects.
---

# Attribute Reference
This page lists all the attributes that the various part pages refer to, what they control, and what
exactly happens when a bonus makes their value larger (more positive). You can assume all attributes
use positive values unless stated otherwise.

Any attributes which are said affect something "multiplicatively" have a base value of 1, and
directly multiply the relevant stat.

Note that this list is not exhaustive, but should cover everything present in the current guides.

Also see the following pages for more detailed overviews of their relevant attributes:

{% assign subpages = site.data.nav.misc
                     | where: "title", "Attribute Reference"
                     | first
                     | map: "sub"
                     | sort_natural: "title" %}
{%- for subpage in subpages -%}
- [{{ subpage.title }}]({{ subpage.url }})
{% endfor %}

{% include attributes.html table_classes="border-x" %}
