import os
import sys
import subprocess
import fileinput
import shutil

username = os.getlogin()
userHomeDir = '/home/'+username+'/'
hyprlandDir = userHomeDir+'.config/hypr'
hyprDir = userHomeDir+'.config/hypr'
downloadedFilesDir = userHomeDir+'Downloads/downloadedFiles'
keybindsConf = hyprlandDir+'/hyprland/keybinds.conf'
keybindsCustomConf = hyprlandDir+'/custom/keybinds.conf'
citr0modsPath = hyprlandDir+'/citr0_end4_mods'

## For disabling the existing, conflicting keybinds

lineOriginal1 = 'bind = Super, S, togglespecialworkspace, # Toggle scratchpad'
lineNew1 = '# bind = Super, S, togglespecialworkspace, # Toggle scratchpad -- Overritten by citr0_mods'

lineOriginal2 = 'bind = Ctrl+Super, S, togglespecialworkspace, # [hidden]'
lineNew2 = '# bind = Ctrl+Super, S, togglespecialworkspace, # [hidden] -- Overritten by citr0_mods'

# For adding a new section to Super+/

lineAppendKeybinds = '''
##! citr0mods
bind = Super, S, togglespecialworkspace, Spotify
bind = Super, D, togglespecialworkspace, vesktop
'''

citr0modsBase = '''
## Vesktop (Discord Client)
windowrulev2 = workspace special:vesktop, class:^(vesktop)$
workspace = special:vesktop, gapsout:30, on-startup:hide
exec-once = vesktop

## Spotify
windowrulev2 = workspace special:spotify, class:^(spotify)$
workspace = special:spotify, gapsout:30, on-startup:hide
exec-once = spotify
'''

def checkEnd4():
    checkerTmp = subprocess.run(['cat', '/home/'+username+'/.config/illogical-impulse/config.json'], capture_output=True)
    if checkerTmp != 'cat: /home/'+username+'/.config/illogical-impulse: No such file or directory':
        compatibility = True
        print('Check Completed')
    else:
        compatibility = False
        print('It does not appear you are running end-4 dot files.')
        print('Reason: the config file does not exist')
        input('Press enter to continue...')
        quit()
    return compatibility

def rewriteStock():
    replacements = {
        lineOriginal1: lineNew1,
        lineOriginal2: lineNew2
    }
    with fileinput.input(files=keybindsConf, inplace=True) as file:
        for line in file:
            for original, new in replacements.items():
                if original in line:
                    line = line.replace(original, new)
            print(line, end='')
    print('Files Overwritten!')

def appendNewInformation():
    with open(keybindsCustomConf, 'a') as file:
        file.write(lineAppendKeybinds)
    with open(hyprDir+'/hyprland.conf', 'a') as file:
        file.write('\n')
        file.write('##! citr0mods\n')
        file.write('source=citr0_end4_mods/specialWindows.conf')
    print('New Information added')

def addBase():
    os.makedirs(citr0modsPath, exist_ok=True)
    with open(citr0modsPath+'/specialWindows.conf', 'w') as file:
        file.write(citr0modsBase)

rewriteStock()
appendNewInformation()
addBase()