# Version 0.0.2a

import os
import sys
import subprocess
import fileinput
import shutil

username = os.getlogin()
userHomeDir = '/home/'+username+'/'
hyprDir = userHomeDir+'.config/hypr'
keybindsConf = '/home/'+username+'.config/hypr/hyprland/keybinds.conf'
keybindsCustomConf = '/home/'+username+'.config/hypr/custom/keybinds.conf'
citr0modsPath = '/home/'+username+'.config/hypr/citr0_end4_mods'
hypridleConf ='/home/'+username+'.config/hypr/hypridle.conf'

ADDITIONS_ALREADY_INSTALLED = False

def printTitle():
    print()
    print('''
      _ _         ___                      _         _       _     _ _ _   _                 
  ___(_) |_ _ __ / _ \\ _ __ ___   ___   __| |___    /_\\   __| | __| (_) |_(_) ___  _ __  ___ 
 / __| | __| '__| | | | '_ ` _ \\ / _ \\ / _` / __|  //_\\\\ / _` |/ _` | | __| |/ _ \\| '_ \\/ __|
| (__| | |_| |  | |_| | | | | | | (_) | (_| \\__ \\ /  _  \\ (_| | (_| | | |_| | (_) | | | \\__ \\
 \\___|_|\\__|_|   \\___/|_| |_| |_|\\___/ \\__,_|___/ \\_/ \\_/\\__,_|\\__,_|_|\\__|_|\\___/|_| |_|___/
                                                                                                                                                                                                                                   
    ''')
    print()
printTitle()
