# Version 0.1.0b

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
hyprDir = userHomeDir+'.config/hypr'
keybindsConf = '/home/'+username+'/.config/hypr/hyprland/keybinds.conf'
keybindsCustomConf = '/home/'+username+'/.config/hypr/custom/keybinds.conf'
citr0modsPath = '/home/'+username+'/.config/hypr/citr0_end4_mods'
hypridleConf ='/home/'+username+'/.config/hypr/hypridle.conf'

ADDITIONS_ALREADY_INSTALLED = False

def printTitle():
    os.system('clear')
    print()
    print('''
      _ _         ___                      _         _       _     _ _ _   _                 
  ___(_) |_ _ __ / _ \\ _ __ ___   ___   __| |___    /_\\   __| | __| (_) |_(_) ___  _ __  ___ 
 / __| | __| '__| | | | '_ ` _ \\ / _ \\ / _` / __|  //_\\\\ / _` |/ _` | | __| |/ _ \\| '_ \\/ __|
| (__| | |_| |  | |_| | | | | | | (_) | (_| \\__ \\ /  _  \\ (_| | (_| | | |_| | (_) | | | \\__ \\
 \\___|_|\\__|_|   \\___/|_| |_| |_|\\___/ \\__,_|___/ \\_/ \\_/\\__,_|\\__,_|_|\\__|_|\\___/|_| |_|___/
                                                                                                                                                                                                                                   
    ''')
    print()

def getInstalledBase():
    global ADDITIONS_ALREADY_INSTALLED
    checkerTmp = subprocess.run(['ls', '/home/'+username+'/.config/hypr/citr0_end4_mods'], capture_output=True)
    if checkerTmp == 'ls: cannot access /home/'+username+'/.config/hypr/citr0_end4_mods: No such file or directory':
        ADDITIONS_ALREADY_INSTALLED = False
        print('The script has determined you have not installed the base modifications, it is reccomended to install them first.')
        print('What you do from here is unsupported, any errors you get will not be resolved and you will be ignored!')
        userChoice = input('Would you like to continue (N/y)')
        if userChoice.lower() != 'y':
            quit()

def addIndex():
    IndexAdded = False
    index = '##! citr0mods -- Additions'

    with open(keybindsCustomConf, 'r') as file:
            if index in file.read():
                IndexAdded = True

    with open(keybindsCustomConf, 'a') as file:
        if IndexAdded == False:
            file.write('\n')
            file.write('##! citr0mods -- Additions\n')

def chromiumBrowserFix():
    # Suggested by citr0net
    chromiumKeybindsDescription = '''
    \033[93mChromium Based Browser Crash Fix\033[00m
    If you use a chromium based browser, you might have noticed that the browser
    crashes when moving the browser to a different workspace. This patch will force
    all chromium based browsers (the ones under the keybinds file) to use X11 (or XWayland) 
    instead of Wayland, which fixes the issue at 0 compromise.

    Reccomended: Yes

    '''
    print(chromiumKeybindsDescription)
    userInput = input('Would you like to patch the chromium based browser keybinds? (Y/n): ')
    if userInput.lower() == 'y':
        original = 'bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser'
        new = '# bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave" "google-chrome-stable" "zen-browser" "firefox" "brave" "chromium" "microsoft-edge-stable" "opera" "librewolf" # Browser -- Overwritten by citr0mods'
        alreadyPatched = False
        patchedKeybind = 'bind = Super, W, exec, ~/.config/hypr/hyprland/scripts/launch_first_available.sh "brave --ozone-platform=x11" "google-chrome-stable --ozone-platform=x11" "chromium --ozone-platform=x11" "microsoft-edge-stable --ozone-platform=x11" "opera --ozone-platform=x11" # Chromium Browser Patches'
        patched = False

        with open(keybindsCustomConf, 'r') as file:
            if patchedKeybind in file.read():
                print('This modification has already been installed and therefore skipped!')
                alreadyPatched = True

            if alreadyPatched == False:
                with fileinput.input(files=keybindsConf, inplace=True) as file:
                    for line in file:
                        if original in line and patched == False:
                                line = line.replace(original, new)
                                patched == True
                        print(line, end='')
                print('Removed existing browser keybind')
                with open(keybindsCustomConf, 'a') as file:
                    file.write(patchedKeybind)
                print('Added custom keybinds')
        print('Passed chromiumBrowserFix')
    else:
        print('Skipped!')

printTitle()
getInstalledBase()
addIndex()
chromiumBrowserFix()