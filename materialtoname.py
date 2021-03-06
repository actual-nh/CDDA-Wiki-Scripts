import json
import pywikibot

#documentation
#Usage: python [location of pywikibotinstall]\pwb.py materialtoname.py
#   Then input your password, and wait for the page to be updated.

with open('data/json/materials.json') as data_file:
    data = json.load(data_file)

output = [ "<includeonly>{{#switch:{{lc:{{{1}}}}}\n" ]
for it in range(0, len(data)):
    output.append("  |")
    output.append(data[it]['ident'])
    output.append(" = ")
    output.append(data[it]['name'])
    output.append("\n")
output.append('''  |#default={{{1|Unknown}}}
}}</includeonly><noinclude>
Template for converting materials to their associated names.

* Source: [https://raw.github.com/CleverRaven/Cataclysm-DDA/master/data/json/materials.json materials.json]
* Automatically generated by [https://github.com/Soyweiser/CDDA-Wiki-Scripts/blob/master/materialtoname.py script]. Any edits made to this can and will be overwritten. Please contact [[User:Soyweiser|Soyweiser]] if you want make changes to this page. Especially as any changes made here probably also means there have been changes in other pages. And there are tools to update those a little bit quicker.

* Usage: ''<nowiki>{{Materialtoname|foo}}</nowiki>'' For example ''<nowiki>{{Materialtoname|iron}}</nowiki>'' outputs ''Iron''

[[Category:Templates|{{PAGENAME}}]]
</noinclude>
''')

text = "".join(output)
text.replace("\n", "\\n")

site = pywikibot.Site('en', 'cddawiki')
page = pywikibot.Page(site, 'Template:Materialtoname')
page.text = text
page.save('Updated text automatically via the https://github.com/Soyweiser/CDDA-Wiki-Scripts materialtoname.py script')
exit()