#WRITE A SCRIPT THAT MODIFIES THE SETTINGS.XML OR .JSON FILE
# SO THE PROGRAM’S UI HAS SPECIFIC DIMENSIONS.


import xml.etree.ElementTree as ET
import time

#PARSE THE XML FILE

try:
    tree=ET.parse('Settings.xml')
    root=tree.getroot()

except:
    print('File not found.')
    time.sleep(4)
    exit()

#USE A DICTIONARY TO FIND THE SELECTED TAGS AND REWRITE ALL THEIR CORRESPONDING VALUES


TagRewrite = {'LayoutSizes':'483,374,849',
              'LayoutNumber':'0',
              'ListViewNumberWidth':'43',
              'ListViewStartWidth':'98',
              'ListViewEndWidth':'82',
              'ListViewDurationWidth':'47',
              'ListViewCpsWidth':'70',
              'ListViewWpmWidth':'0',
              'ListViewGapWidth':'47',
              'ListViewActorWidth':'0',
              'ListViewRegionWidth':'0',
              'ListViewTextWidth':'438',
              'ListViewNumberDisplayIndex':'0',
              'ListViewStartDisplayIndex':'1',
              'ListViewEndDisplayIndex':'2',
              'ListViewDurationDisplayIndex':'3',
              'ListViewCpsDisplayIndex':'4',
              'ListViewWpmDisplayIndex':'-1',
              'ListViewGapDisplayIndex':'5',
              'ListViewActorDisplayIndex':'-1',
              'ListViewRegionDisplayIndex':'-1',
              'ListViewTextDisplayIndex':'6'}

for key, value in TagRewrite.items():
    layout_val=root.find('General/'+key)
    layout_val.text=value

#SAVE THE MODIFIED FILE
tree.write('Settings.xml')

print('Reset successful.')
