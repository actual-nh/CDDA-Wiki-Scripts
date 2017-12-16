import json
import sys
import pywikibot

#Data is automatically, if you installed pywikibot correctly, to the page.
#Usage: python [location of pywikibotinstall]\pwb.py navbar_trait.py
#   Then input your password, and wait for the page to be updated.

with open('data/json/mutations.json') as data_file:    
    data = json.load(data_file)

output = [ """<noinclude><!--Automatically generated by https://github.com/Soyweiser/CDDA-Wiki-Scripts-->
Automatically generated by [https://github.com/Soyweiser/CDDA-Wiki-Scripts The navbar_trait.py script]. Any edits made to this can and will be overwritten. Please contact [[User:Soyweiser|Soyweiser]] if you want make changes to this page. Especially as any changes made here probably also means there have been changes in the traits and mutations pages. And there are tools to update those a little bit quicker.</noinclude>
{{Navbox
|name       = Traits
|title      = [[Traits]]
|state      = uncollapsed

|bodystyle = background:white; width:100%; vertical-align:middle; border-color: #CCAAAA;
|titlestyle = background:LightGreen; color:darkblue; padding-left:1em; padding-right:1em; text-align:center;
|groupstyle = background:LightGreen; color:black; padding-left:1em; padding-right:1em; text-align:right; font-weight: bold;

  
|group1     = Positive
|list1      = <!--"""]

def ID_To_WikiString(id):
    if id == "Infrared Vision":
        return "Infrared Vision (Mutation)|Infrared Vision"
    return id

Ptraits = list()
Ntraits = list()
Professions = list()

for iterator in range(0, len(data)):
    if("starting_trait" in data[iterator]):
        if(int(data[iterator]['points']) > 0):
            Ptraits.append(data[iterator]['name'])
        elif(int(data[iterator]['points']) < 0):
            Ntraits.append(data[iterator]['name'])
    if("profession" in data[iterator]):
        Professions.append(data[iterator]['name'])

Ptraits = sorted(Ptraits)
Ntraits = sorted(Ntraits)
Professions = sorted(Professions)

for it in range(0, len(Ptraits)):
    output.append("        --> ")
    if it > 0:
        output.append("{{md}}")
    output.append("[[")
    output.append(Ptraits[it])
    output.append("]]<!--\n")
output.append("""	-->

|group2     = Negative
|list2      = <!--\n""")

for it in range(0, len(Ntraits)):
    output.append("        --> ")
    if it > 0:
        output.append("{{md}}")
    output.append("[[")
    output.append(Ntraits[it])
    output.append("]]<!--\n")
output.append("""	-->

|group3     = Professions
|list3      = <!--\n""")

for it in range(0, len(Professions)):
    output.append("        --> ")
    if it > 0:
        output.append("{{md}}")
    output.append("[[")
    output.append(Professions[it])
    output.append("]]<!--\n")
output.append("""	-->

}}<noinclude>
[[Category:Navigational templates]][[Category:Templates]]
</noinclude>""")

text = "".join(output)
text.replace("\n", "\\n")
site = pywikibot.Site('en', 'cddawiki')
page = pywikibot.Page(site, 'Template:Navbar/traits')
page.text = text
page.save('Updated text automatically via the https://github.com/Soyweiser/CDDA-Wiki-Scripts navbar_trait.py script')
exit()