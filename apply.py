import os
import sys
import subprocess

username = os.getlogin()
userHomeDir = '/home/'+username+'/'
hyprlandDir = userHomeDir+'.config/hypr'
downloadedFilesDir = userHomeDir+'Downloads/downloadedFiles'

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

def downloadFiles():
    os.system('rm -rf'+' '+downloadedFilesDir)
    os.system('mkdir'+' '+downloadedFilesDir)
    os.system('curl -o'+downloadedFilesDir+'/keybinds.conf https://raw.githubusercontent.com/citr0net/citr0_end4_keybinds/refs/heads/main/hypr/keybinds.conf')
    os.system('curl -o'+downloadedFilesDir+'/keybindsCustom.conf https://raw.githubusercontent.com/citr0net/citr0_end4_keybinds/refs/heads/main/hypr/custom/keybinds.conf')

def copyFiles():
    cmd1 = 'rm'+' '+hyprlandDir+'/hyprland/keybinds.conf'
    cmd2 = 'cp'+' '+downloadedFilesDir+'/keybinds.conf'+' '+hyprlandDir+'/hyprland/keybinds.conf'
    cmd3 = 'rm'+' '+hyprlandDir+'/custom/keybinds.conf'
    cmd4 = 'cp'+' '+downloadedFilesDir+'/keybindsCustom.conf'+' '+hyprlandDir+'/custom/keybinds.conf'
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    os.system(cmd4)

checkEnd4()
downloadFiles()
copyFiles()
