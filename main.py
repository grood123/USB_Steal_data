import os, string, time
from ctypes import windll
import os
from shutil import copyfile, ignore_patterns
import pathlib


#all print you can delete

def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()  # The GetLogicalDrives function retrieves a bitmask
    # representing the currently available disk drives.
    for label in string.ascii_uppercase : # The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices


def detect_device():
    ext = ["xlsx"]#enter file extension all from small letters , add like new array element
    original = set(get_driveStatus())
    print("Detecting...")
    time.sleep(3)
    add_device = set(get_driveStatus()) - original
    subt_device = original - set(get_driveStatus())
    prompt = "C:/tmp1"#path of folder that will be containing all files
    if (len(add_device)):
        print("There were %d" % (len(add_device)))

        for drive in add_device:
            print("The drives added: %s." % (drive))

        def createFolder(directory):
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory)
            except OSError:
                print('Error: Creating directory. ' + directory)

        createFolder(prompt)
        print("FOLDER CREATED")




        dest = prompt

        path = drive + ':'
        # loop for retrieving all the files and folders for top-down search
        for root, directories, contents in os.walk(path, topdown=False):

            for name in contents:
                lol =os.path.join(root, name)
                print(lol)
                x = name.split('.')
                try:
                    if x[1] in ext:
                        copyfile(root+"/" + name, dest + name)
                        print("COPIED")
                except:
                    print("EROR")








    elif (len(subt_device)):
        print("There were %d" % (len(subt_device)))
        for drive in subt_device:
            print("The drives remove: %s." % (drive))


if __name__ == '__main__':

    while True:
        detect_device()
