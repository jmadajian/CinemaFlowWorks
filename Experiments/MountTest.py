import subprocess
import sys
import os.path

if os.path.isdir('D:') :
    drive_mount_state="Drive_Mounted"
else:
    drive_mount_state="Nothing"
print(drive_mount_state)
#if __name__ == '__main__':
 #   MountTest().run()
