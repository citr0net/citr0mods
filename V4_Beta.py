# Version 0.0.1b

# DO NOT USE THIS, THIS IS UNTESTED!!!

# Contributers
# ------------
# citr0net

# Ideas to implement:
# - 

import os
import sys
import subprocess
import fileinput
import shutil

username = os.getlogin()
userHomeDir = '/home/'+username+'/'
hyprlandDir = userHomeDir+'.config/hypr'
hyprDir = userHomeDir+'.config/hypr'
keybindsConf = hyprlandDir+'/hyprland/keybinds.conf'
keybindsCustomConf = hyprlandDir+'/custom/keybinds.conf'
citr0modsPath = hyprlandDir+'/citr0_end4_mods'
hypridleConf = hyprlandDir+'/hypridle.conf'

def fileOverwrite(filePath, toRewrite, replacementText):
    with fileinput.input(files=keybindsConf, inplace=True) as file:
        for line in file:
            if toRewrite in line and patched == False:
                line = line.replace(original, new)
                    patched == True
                print(line, end='')

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

def fileAppend(filePath, appendText):
    with open(filePath, 'a') as file:
        file.write(appendText)

def getDiscordClientChoice():
    isValidChoice = 0
    printTitle()
    while isValidChoice == 0:
        optionDiscordClient = int(input('''
What do you have installed:
1: Discord
2: Vesktop

Please type the coresponding number: '''))
        if optionDiscordClient == 1:
            return 'Discord_clientTypeDiscord'
            isValidChoice == 1
        elif optionDiscordClient == 2:
            return 'Vesktop_clientTypeDiscord'
            isValidChoice = 1
        else:
            isValidChoice = 0

## Disable Conflicting Keybinds
lineDisableScratchpadKeybind = 'bind = Super, S, togglespecialworkspace, # Toggle scratchpad'
newLineDisableScratchpadKeybind = '# bind = Super, S, togglespecialworkspace, # Toggle scratchpad -- Overritten by citr0_mods'

lineDisableSpecialWorkspace = 'bind = Ctrl+Super, S, togglespecialworkspace, # [hidden]'
newLineDisableSpecialWorkspace = '# bind = Ctrl+Super, S, togglespecialworkspace, # [hidden] -- Overritten by citr0_mods'

lineDisableFullscreen = 'bind = Super, D, fullscreen, 1 # Maximize'
newLineDisableFullscreen = '# bind = Super, D, fullscreen, 1 # Maximize, # [hidden] -- Overritten by citr0_mods'

def variables():
    # I use a global here so I can minamize this, as these are proven good
    global lineSleep, newSleep, disableMouseAcceleration, lineAppendKeybindsForCheatsheet, discordClientOption, vesktopClientOption, spotifyClientOption
    ## Disable Sleep (Optional)
    lineSleep = '''
    listener {
        timeout = 900 # 15mins
        on-timeout = $suspend_cmd
    }
    '''

    newSleep = '''
    #listener {
    #    timeout = 900 # 15mins
    #    on-timeout = $suspend_cmd
    #}
    '''

    disableMouseAcceleration = '''
    ## Removes mouse accelerated
    input {
      sensitivity = 0
      accel_profile = flat
    }
    '''

    ## Add new keybinds for the keybinds cheatsheat
    lineAppendKeybindsForCheatsheet = '''
    ##! citr0mods
    bind = Super, S, togglespecialworkspace, spotify # Spotify Window
    bind = Super, D, togglespecialworkspace, discord # Discord Window
    '''

    ## New Window Rules:
    discordClientOption = '''
    ## Discord (Discord Client)
    windowrulev2 = workspace special:discord, class:^(discord)$
    workspace = special:discord, gapsout:30, on-startup:hide
    exec-once = discord
    '''

    vesktopClientOption = '''
    ## Vesktop (Discord Client)
    windowrulev2 = workspace special:discord, class:^(vesktop)$
    workspace = special:discord, gapsout:30, on-startup:hide
    exec-once = vesktop
    '''

    spotifyClientOption = '''
    ## Spotify
    windowrulev2 = workspace special:spotify, class:^(Spotify)$
    workspace = special:spotify, gapsout:30, on-startup:hide
    exec-once = spotify
    '''