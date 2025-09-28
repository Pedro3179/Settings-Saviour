# WRITE A SCRIPT THAT RESTAURES THE UI BACK TO THE LEGACY TOOLBAR
# AND SPECIFIC UI DIMENSIONS AFTER AN UPDATE


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
              'ListViewTextDisplayIndex':'6',
              'ToolbarIconTheme':'Legacy'
              }
changes=[]

for key, value in TagRewrite.items():
    layout_val=root.find('General/'+key)
    if layout_val is not None:
        old_value=layout_val.text
        layout_val.text=value
        changes.append(f'{key}: {old_value} -> {value}')

#SAVE THE MODIFIED FILE
tree.write('Settings.xml')

print('The following changes were applied:\n')
for change in changes:
    print(" - "+change)

print('\nSettings have been successfully restored to legacy toolbar and default UI dimensions.')
print('You may need to restart the application for changes to take effect.\n')
