import json
import sys
from pprint import pprint
from Tkinter import Tk
root = Tk()
root.withdraw()

#Data is copied to clipboard, Used to create the various lists for the threshold pages.
#After executing, select the window running python again. And input a number. This creates a list of mutations copied into the clipboard. Copy and paste into the wiki.

with open('data/json/mutations.json') as data_file:    
    data = json.load(data_file)

list_categories = [ 'Lizard', 'Bird', 'Fish', 'Beast', 'Feline', 'Lupine', 'Ursine', 'Cattle', 'Insect', 'Plant', 'Slime (Mutation category)|Slime', 'Troglobite_(Mutation_category)|Troglobite', 'Cephalopod', 'Spider', 'Rat', 'Medical', 'Alpha', 'Elf-A', 'Chimera', 'Raptor', 'Mycus (Mutation category)|Mycus', 'Marloss' ]

dict_categories = { 'MUTCAT_LIZARD' : 'Lizard', 'MUTCAT_BIRD' : 'Bird', 'MUTCAT_FISH' : 'Fish', 'MUTCAT_BEAST' : 'Beast', 'MUTCAT_FELINE' : 'Feline', 'MUTCAT_LUPINE' : 'Lupine', 'MUTCAT_URSINE' : 'Ursine', 'MUTCAT_CATTLE' : 'Cattle', 'MUTCAT_INSECT' : 'Insect', 'MUTCAT_PLANT' : 'Plant', 'MUTCAT_SLIME' : 'Slime (Mutation category)|Slime', 'MUTCAT_TROGLOBITE' : 'Troglobite_(Mutation_category)|Troglobite', 'MUTCAT_CEPHALOPOD' : 'Cephalopod', 'MUTCAT_SPIDER' : 'Spider', 'MUTCAT_RAT' : 'Rat', 'MUTCAT_MEDICAL' : 'Medical', 'MUTCAT_ALPHA' : 'Alpha', 'MUTCAT_ELFA' : 'Elf-A', 'MUTCAT_CHIMERA' : 'Chimera', 'MUTCAT_RAPTOR' : 'Raptor', 'MUTCAT_MYCUS' : 'Mycus (Mutation category)|Mycus', 'MUTCAT_MARLOSS' : 'Marloss' }

def ID_To_WikiString(id):
    if id == "Infrared Vision":
        return "Infrared Vision (Mutation)|Infrared Vision"
    return id

mut_trait = dict()
for iterator in range(0, len(list_categories)):
    traits = dict()
    traits['traits'] = list()
    traits['mutations'] = list()
    traits['threshold'] = list()
    mut_trait[list_categories[iterator]] = traits
    
for iterator in range(0, len(data)):
    if("category" in data[iterator]):
        if("starting_trait" in data[iterator]):
            for it in data[iterator]['category']:
                mut_trait[dict_categories[it]]['traits'].append(data[iterator]['name'])
        elif("threshreq" in data[iterator]):
            for it in data[iterator]['category']:
                mut_trait[dict_categories[it]]['threshold'].append(data[iterator]['name'])
        else:
            for it in data[iterator]['category']:
                mut_trait[dict_categories[it]]['mutations'].append(data[iterator]['name'])
    
output = []
var = raw_input(">")
while True:
    while var.isdigit():
        output = [ "<!--Automatically generated using https://github.com/Soyweiser/CDDA-Wiki-Scripts -->\n= Traits = \n"]
        for it in range(0, len(mut_trait[list_categories[int(var)]]['traits'])):
            output.append("{{:")
            output.append(ID_To_WikiString(mut_trait[list_categories[int(var)]]['traits'][it]))
            output.append("}}\n")
        
        output.append("\n= Normal Mutations =\n")
        for it in range(0, len(mut_trait[list_categories[int(var)]]['mutations'])):
            output.append("{{:")
            output.append(ID_To_WikiString(mut_trait[list_categories[int(var)]]['mutations'][it]))
            output.append("}}\n")
            
        output.append("\n= Post-threshold mutations =\n")
        for it in range(0, len(mut_trait[list_categories[int(var)]]['threshold'])):
            output.append("{{:")
            output.append(ID_To_WikiString(mut_trait[list_categories[int(var)]]['threshold'][it]))
            output.append("}}\n")
    
        output.append("<!-- End of automatically generated data -->")
        text = "".join(output)
        text.replace("\n", "\\n")
        print text
        print list_categories[int(var)]
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        var = raw_input(">")
    else:
        if ( var == 'exit' ):
            root.update()
            root.destroy()
            exit()