# Version 0.1a

# Contributors
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

citr0modsFile = citr0modsPath+'/citr0modsBase.conf'
# Create Files
os.system(f"mkdir -p '{citr0modsPath}'")
os.system(f'echo > "{citr0modsFile}"')

os.system('clear')

def printTitle():
    print()
    print('''
      _ _         ___                      _              _           _        _ _           
  ___(_) |_ _ __ / _ \ _ __ ___   ___   __| |___         (_)_ __  ___| |_ __ _| | | ___ _ __ 
 / __| | __| '__| | | | '_ ` _ \ / _ \ / _` / __|        | | '_ \/ __| __/ _` | | |/ _ \ '__|
| (__| | |_| |  | |_| | | | | | | (_) | (_| \__ \        | | | | \__ \ || (_| | | |  __/ |   
 \___|_|\__|_|   \___/|_| |_| |_|\___/ \__,_|___/        |_|_| |_|___/\__\__,_|_|_|\___|_|   
                                                                                                                                                
    ''')
    print()


whatToAddToCitr0mods = [
    '''
#          _ _         ___                      _     
#      ___(_) |_ _ __ / _ \ _ __ ___   ___   __| |___ 
#     / __| | __| '__| | | | '_ ` _ \ / _ \ / _` / __|
#    | (__| | |_| |  | |_| | | | | | | (_) | (_| \__ \
#     \___|_|\__|_|   \___/|_| |_| |_|\___/ \__,_|___/
#    
    ''',

]

whatToAddToCustomKeybinds = [

]

def fileOverwrite(filePath, toRewrite, replacementText):
    # FIX: Always print every line so the file is not truncated
    if not os.path.exists(filePath):
        return

    with fileinput.input(files=[filePath], inplace=True, backup='.bak') as file:
        for line in file:
            if toRewrite in line:
                # Replace only the matching part
                line = line.replace(toRewrite, replacementText)
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
    while isValidChoice == 0:
        optionDiscordClient = int(input('''
What do you have installed:
1: Discord
2: Vesktop

Please type the coresponding number: '''))
        if optionDiscordClient == 1:
            isValidChoice == 1
            return 'Discord_clientTypeDiscord'
        elif optionDiscordClient == 2:
            isValidChoice = 1
            return 'Vesktop_clientTypeDiscord'
        else:
            isValidChoice = 0

def lookInFile(filePath, line):
    with open(filePath, 'r') as f:
        if line in f.read():
            return True
        else:
            return False

def chromiumBrowserFix():
    # Suggested by citr0net
    chromiumKeybindsDescription = '''
    \033[93mChromium Based Browser Crash Fix\033[00m
    If you use a chromium based browser, you might have noticed that the browser
    crashes when moving the browser to a different workspace. This patch will force
    all chromium based browsers (the ones under the keybinds file) to use X11 (or XWayland) 
    instead of Wayland, which fixes the issue at 0 compromise. This will also
    disable any firefox based browsers from being opened to the keybind, which
    is especially useful if you don't want to delete firefox, but it is preinstalled.

    Reccomended: Yes

    '''
    print(chromiumKeybindsDescription)
    toAddToCustom = 'bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave --ozone-platform=x11" "google-chrome-stable --ozone-platform=x11" "chromium --ozone-platform=x11" "microsoft-edge-stable --ozone-platform=x11" "opera --ozone-platform=x11" # Chromium Browser Patches'
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        fileOverwrite(keybindsConf, 
        'bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser',
        '# bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave" "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser -- Overwritten by citr0mods')
        print('Removed existing browser keybind')
        if not lookInFile(keybindsCustomConf, toAddToCustom):
            whatToAddToCustomKeybinds.append(key)
        else:
            print('Keybind already detected')


def applicationSpecialWorkspaces():
    # From citr0mods V1-3
    specialWorkspacesDescription = '''
    \033[93mSpecific Special Workspaces\033[00m
    If you've used the caelestia shell then you are very famillar with this one.
    It will give applications such as Discord / Vesktop and Spotify their own special
    workspace. Keybinds are overwriten and with 99% of updates, you will need to
    reinstall this script as keybinds can get overwritten. This will replace the built in
    special workspace function (Super + S). This will also autostart these applications

    Requires:
    - Spotify
    - Discord OR Vesktop

    Reccomended: Depends
    '''
    print(specialWorkspacesDescription)
    userInput = input('Would you like this patch? (y/N): ')
    if userInput.lower() == 'y':
        print(specialWorkspacesDescription)
        conflictingKeybinds = {
        'bind = Super, D, fullscreen, 1 # Maximize': '# Feature conflicts with Discord / Vesktop - citr0mods', # Conflicts with Discord
        'bind = Super+Alt, S, movetoworkspacesilent, special # Send to scratchpad': '# Feature conflicts with Spotify - citr0mods', # Conflicts with spotify
        'bind = Ctrl+Super, S, togglespecialworkspace, # [hidden]': '# Feature conflicts with Spotify - citr0mods', # Conflicts with spotify
        'bind = Super, S, togglespecialworkspace, # Toggle scratchpad': '# Feature conflicts with Spotify - citr0mods' # Conflicts with spotify
        }

        for key, newKey in conflictingKeybinds.items():
            if not lookInFile(keybindsCustomConf, key):
                fileOverwrite(keybindsConf, key, newKey)
                print('Rewriten Line that contains "',key+'" with "',newKey+'"')

        newKeybinds = [
            'bind = Super, S, togglespecialworkspace, spotify # Spotify Window',
            'bind = Super, D, togglespecialworkspace, discord # Discord Window'
        ]
        for key in newKeybinds:
            if not lookInFile(keybindsCustomConf, key):
                whatToAddToCustomKeybinds.append(key)

        if getDiscordClientChoice() == 'Discord_clientTypeDiscord':
            whatToAddToCitr0mods.append('''
                ## Discord (Discord Client)
                windowrulev2 = workspace special:discord, class:^(discord)$
                workspace = special:discord, gapsout:30, on-startup:hide
                exec-once = discord
                ''')
        else:
            whatToAddToCitr0mods.append('''
                ## Discord (Discord Client)
                windowrulev2 = workspace special:discord, class:^(vesktop)$
                workspace = special:discord, gapsout:30, on-startup:hide
                exec-once = vesktop
                ''')
    else:
        print('Skipped!')

def autoSizedApplications():
    autoSizedAppsDescription = '''
    \033[93mAutomanic Sized Applications\033[00m
    This will automanically size and float applications like Calculator Apps and Clock Apps.
    Useful as end-4 dot files do not do this by default.

    Supports:
    - Kcalc
    - Gnome Calculator
    - Gnome Clocks

    Reccomended: Yes
    '''
    userInput = input('Would you like this patch (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        newEntries = '''
        ## Floating Calculators
        windowrulev2 = float, class:^(org.kde.kcalc)
        windowrulev2 = float, class:^(org.gnome.Calculator)

        ## Auto Size Calculators:
        windowrulev2 = size 472 473, class:^(org.kde.kcalc)
        windowrulev2 = size 360 616, class:^(org.gnome.Calculator)

        # Clocks
        windowrulev2 = float, class:^(org.gnome.clocks)
        windowrulev2 = size 457 545, class:^(org.gnome.clocks)
        '''

        whatToAddToCitr0mods.append(newEntries)

def autoStartSteam():
    autoStartSteamDescription = '''
    \033[93mAuto-Start Steam\033[00m
    Self Explanitory. This starts steam on startup in the background.

    Requires:
    - Steam

    Reccomended: Yes

    '''
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        whatToAddToCitr0mods.append('exec-once = steam -silent')

def mouseAcceleration():
    autoStartSteamDescription = '''
    \033[93mDisable Mouse Acceleration\033[00m
    Self Explanitory. Disables mouse acceleration.
    Useful for gaming.

    Reccomended: Yes

    '''
    userInput = input('Would you like this patch? (Y/n): ')
    if userInput.lower() == 'n':
        print('Skipped!')
    else:
        whatToAddToCitr0mods.append('''
        ## Disable Mouse Acceleration
        input {
            sensitivity = 0
            accel_profile = flat
        }
        ''')

def monitorPatches():
    monitorPatchesDescription = '''
    \033[93mMonitor Patches\033[00m
    This adds workspaces for every monitor. Especially useful for
    people with multiple monitors.

    Requires:
    - 2 or more displays

    Issues:
    - If you have ran this before, don't run it again.
      It will break things

    Reccomended: Depends

    '''
    userChoice = input('Would you like this patch y/N? ')
    if userChoice.lower() == 'y':
        result = subprocess.run(['hyprctl', 'monitors'], capture_output=True, text=True)
        monitors = [line.split()[1].strip("'") for line in result.stdout.splitlines() if 'connected' in line]

        monitorsFile = citr0modsPath+'/monitorAdditions.conf'
        fileAppend('~/.config/hypr/hyprland.conf', 'source='+monitorsFile)

        workspace_count = 1
        with open(monitorsFile, "w") as f:
            for i, monitor in enumerate(monitors):
                start_workspace = workspace_count
                end_workspace = workspace_count + 9

                f.write(f"# --- Bind workspaces {start_workspace}-{end_workspace} (group {i+1}) to {monitor} ---\n")
                
                for workspace in range(start_workspace, end_workspace + 1):
                    f.write(f"workspace = {workspace}, monitor:{monitor}, default:true\n")

                workspace_count = end_workspace + 1

def addNewKeybinds():
    for key in whatToAddToCustomKeybinds:
        fileAppend(keybindsCustomConf, key)

    for key in whatToAddToCitr0mods:
        fileAppend(citr0modsFile, key)

printTitle()
checkEnd4()

entryAdditions = '''
# citr0mods
source=citr0_end4_mods/citr0modsBase.conf
'''
fileAppend(userHomeDir+'.config/hypr/hyprland.conf', entryAdditions)

chromiumBrowserFix()
applicationSpecialWorkspaces()
autoSizedApplications()
autoStartSteam()
mouseAcceleration()
monitorPatches()

# Write to Disk
addNewKeybinds()