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

ALREADY_INSTALLED = False

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

citr0modsText = '''
#          _ _         ___                      _     
#      ___(_) |_ _ __ / _ \\ _ __ ___   ___   __| |___ 
#     / __| | __| '__| | | | '_ ` _ \\ / _ \\ / _` / __|
#    | (__| | |_| |  | |_| | | | | | | (_) | (_| \\__ \\
#     \\___|_|\\__|_|   \\___/|_| |_| |_|\\___/ \\__,_|___/
#    
'''

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

## For disabling the existing, conflicting keybinds

lineOriginal1 = 'bind = Super, S, togglespecialworkspace, # Toggle scratchpad'
lineNew1 = '# bind = Super, S, togglespecialworkspace, # Toggle scratchpad -- Overritten by citr0_mods'

lineOriginal2 = 'bind = Ctrl+Super, S, togglespecialworkspace, # [hidden]'
lineNew2 = '# bind = Ctrl+Super, S, togglespecialworkspace, # [hidden] -- Overritten by citr0_mods'

lineOriginal3 = 'bind = Super, D, fullscreen, 1 # Maximize'
lineNew3 = '# bind = Super, D, fullscreen, 1 # Maximize, # [hidden] -- Overritten by citr0_mods'

## For disabling sleep
lineOriginal4 = '''
listener {
    timeout = 900 # 15mins
    on-timeout = $suspend_cmd
}
'''

lineNew4 = '''
#listener {
#    timeout = 900 # 15mins
#    on-timeout = $suspend_cmd
#}
'''

# For adding a new section to Super+/

lineAppendKeybinds = '''
##! citr0mods
bind = Super, S, togglespecialworkspace, spotify # Spotify Window
bind = Super, D, togglespecialworkspace, discord # Discord Window
'''

discordClient = '''
## Discord (Discord Client)
windowrulev2 = workspace special:discord, class:^(discord)$
workspace = special:discord, gapsout:30, on-startup:hide
exec-once = discord
'''

vesktopClient = '''
## Vesktop (Discord Client)
windowrulev2 = workspace special:discord, class:^(vesktop)$
workspace = special:discord, gapsout:30, on-startup:hide
exec-once = vesktop
'''

spotifyClient = '''
## Spotify
windowrulev2 = workspace special:spotify, class:^(Spotify)$
workspace = special:spotify, gapsout:30, on-startup:hide
exec-once = spotify
'''

floatingCalc = '''
## Floating Calculators
windowrulev2 = float, class:^(org.kde.kcalc)
windowrulev2 = float, class:^(org.gnome.Calculator)

## Auto Size Calculators:
windowrulev2 = size 472 473, class:^(org.kde.kcalc)
windowrulev2 = size 360 616, class:^(org.gnome.Calculator)
'''

inputModification = '''
## Removes mouse accelerated
input {
  sensitivity = 0
  accel_profile = flat
}
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

def addUserDiscordAndBase():
    global ALREADY_INSTALLED
    if os.path.exists(citr0modsPath):
        print('citr0mods already installed, updating')
        os.system('rm -rf '+citr0modsPath+'/specialWindows.conf')
        ALREADY_INSTALLED = True # Global warning (Future Reference)
        os.makedirs(citr0modsPath, exist_ok=True)
    choice = getDiscordClientChoice()
    os.makedirs(citr0modsPath, exist_ok=True)
    with open(citr0modsPath+'/specialWindows.conf', 'w') as file:
        file.write(citr0modsText)
        print('\n')
        print('\n')
        if choice == 'Discord_clientTypeDiscord':
           file.write(discordClient)
        if choice == 'Vesktop_clientTypeDiscord':
            file.write(vesktopClient)

def addSpotify():
    with open(citr0modsPath+'/specialWindows.conf', 'a') as file :
        print('\n')
        file.write(spotifyClient)

def addFloatingCalc():
    with open(citr0modsPath+'/specialWindows.conf', 'a') as file :
        print('\n')
        file.write(floatingCalc)

def rewriteStock():
    replacements = {
        lineOriginal1: lineNew1,
        lineOriginal2: lineNew2,
        lineOriginal3: lineNew3
    }
    with fileinput.input(files=keybindsConf, inplace=True) as file:
        for line in file:
            for original, new in replacements.items():
                if original in line:
                    line = line.replace(original, new)
            print(line, end='')
    print('Keybind Files Overwritten!')

def appendNewInformation():
    with open(keybindsCustomConf, 'a') as file:
        file.write(lineAppendKeybinds)
    with open(hyprDir+'/hyprland.conf', 'a') as file:
        file.write('\n')
        file.write('##! citr0mods\n')
        file.write('source=citr0_end4_mods/specialWindows.conf')
    print('New Information added')

def restartFunction():
    restart = input('Would you like to restart now? (y/N): ')
    if restart == 'y':
        os.system('reboot')
    else:
        print('Enjoy your mods :) -citr0')

def mouseAccelerationModificaiton():
    checkerTmp = input('Would you like to disable mouse acceleration as well (Y/n): ')
    if checkerTmp != 'n':
        with open(citr0modsPath+'/specialWindows.conf', 'a') as file:
            file.write(inputModification)

def rewriteHypride():
    checkerTmp = input('Would you like to disable sleep mode (y/N): ')
    if checkerTmp != 'y':
        return
    else:
        with open(hypridleConf, 'r+') as file:
            content = file.read()
            content = content.replace(lineOriginal4.strip(), lineNew4.strip())
            file.seek(0)
            file.write(content)
            file.truncate()

        print('Hypride Files Overwritten!')

addUserDiscordAndBase()
addSpotify()
addFloatingCalc()
rewriteStock()
if ALREADY_INSTALLED == False:
    appendNewInformation()
mouseAccelerationModificaiton()
rewriteHypride()
restartFunction()
# print(ALREADY_INSTALLED)  -- Used for Debuging Purposes. If asked, please uncomment this line!
