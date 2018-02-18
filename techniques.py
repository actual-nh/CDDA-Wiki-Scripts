import json
import sys
import string
import pywikibot

#Data is automatically copied to the wiki Template:TECtoname page.
#Usage: python [location of pywikibotinstall]\pwb.py techniques.py
#   Then input your password, and wait for the pages to be updated.

with open('data/json/techniques.json') as data_file:
    data = json.load(data_file)

footer = '''
  |#default={{{1}}}
}}</includeonly><noinclude>
Template for converting Technique identifiers to their associated names.

* [https://github.com/CleverRaven/Cataclysm-DDA Cataclysm-DDA/data/json/techniques.json]

<noinclude>Automatically generated by [https://github.com/Soyweiser/CDDA-Wiki-Scripts The techniques.py script]. Any edits made to this can and will be overwritten. Please contact [[User:Soyweiser|Soyweiser]] if you want make changes to this page. Especially as any changes made here probably also means there have been changes in other pages. And there are tools to update those a little bit quicker.\n
{{ver|0.D}}
[[Category:Templates]]
</noinclude>'''

header = '''<includeonly>{{#switch:{{lc:{{{1}}}}}'''



output = [ "" ]
output.append(header)
for iterator in range(0, len(data)):
    if('type' in data[iterator]):
        if('technique' == data[iterator]['type']): #only add techniques.
            output.append("\n  |")
            output.append(data[iterator]["id"].lower())
            output.append(" = ")
            output.append(data[iterator]["name"])
output.append(footer)

text = "".join(output)
text.replace("\n", "\\n")
site = pywikibot.Site('en', 'cddawiki')
page = pywikibot.Page(site, 'Template:TECtoname')
page.text = text
page.save('Updated text automatically via the https://github.com/Soyweiser/CDDA-Wiki-Scripts techniques.py script')
exit()