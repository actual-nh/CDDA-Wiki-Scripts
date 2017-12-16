# CDDA-Wiki-Scripts
Collection of scripts used to convert the Cataclysm-DDA json files to media wiki content.

CDDA main repository: https://github.com/CleverRaven/Cataclysm-DDA

CDDA Wiki: http://cddawiki.chezzo.com/cdda_wiki/index.php?title=Main_Page

Uses python 2.7
Does not directly add content to the wiki. Only converts the json files. Need to be manually copy pasted in.

# Install
Get python 2.7
Copy the most recent json files into data/json

Get 
Windows:
Download and install https://www.microsoft.com/en-in/download/details.aspx?id=44266
pip install --upgrade setuptools
pip install ez_setup

pip install requests
If it's still not working, maybe pip didn't install/upgrade setup_tools properly so you might want to try
easy_install -U setuptools
pip install --upgrade setuptools

pip install requests (again)

pip.exe install -U requests[security] 

Configure pywikibot:
Copy the pywikibot_config\cddawiki_family.py to [location of pywikibotinstall]\pywikibot\families
In the [location of pywikibotinstall] run 'python .\pwb.py generate_user_files' setup your userfiles, and the account used by the bot to connect to the wiki.

# Documentation of scripts

## bionics.py

Data is copied to clipboard, used for the Bionics, does not work on faulty bionics, or bionics without a CBM. Those are different (as they lack an item equivalent).

## bionicsFaulty.py

Data is copied to clipboard, used for the Faulty Bionics, or bionics without a CBM item, which means they cannot be directly installed, do not use on normal bionics (with a direct CBM).

## bionicsList.py

Data is copied to clipboard, used for the http://cddawiki.chezzo.com/cdda_wiki/index.php?title=Bionics generates the non faulty bionics list, if used without a command line argument, and if the command True is given, will list the faulty bionics.

### Note
'Microreactor Upgrade CBM' is an exception here, will need to be manually fixed.

## materialresistances.py

Data is copied to clipboard, used for the Template:Matbashres, Matfireres, Matcutres, Matelecres, Matacidres, takes a command line argument, must be the json data field you are interested in. for example 'acid_resist'

## materials.py

Data is copied to clipboard, used for the http://cddawiki.chezzo.com/cdda_wiki/index.php?title=Materials page

## materialtoname.py

Data is copied to clipboard, used for the Template:Materialtoname

## mutationtable.py

Data is copied to clipboard, used for the Template:Mutationtable

## mutationthresholds.py

Data is copied to clipboard, Used to create the various lists for the threshold pages.
After executing, select the window running python again. And input a number. This creates a list of mutations copied into the clipboard. Copy and paste into the wiki. For the mapping between the input number and the page created look at the list_categories list. Start counting at zero.

## trait.py

This script generates the individual pages for the traits/mutations. Works via command line. You need to give the index number of the trait/mutation for the text to generate. Generated text is automaticly placed in the clipboard. Use the mutation/trait id value (for example 'SHELL2') as a command line argument to get the index of that mutation.

## Automated scripts
The following scripts simply use pywikibot to upload content to the pages automatically.
navbar_trait.py -> Template:Navbar/traits
ComestiblesList.py -> Template:Comestibles/food, Template:Comestibles/Drinks, Template:Comestibles/Meds, Template:Comestibles/Mutagen

#Troubleshooting

## Pywikibot can't connect to the site. Error mentions that 'http' is not a valid protocol return value.

Seems they fixed the bug. (According to the documentation the 'http' protocol value is not allowed).
