import os
import datetime
import shutil

now = datetime.datetime.now()
modified = now - datetime.timedelta(hours=24)
source = 'C:\\Users\\Student\\Desktop\\shutil\\Folder A\\'
dest1 = 'C:\\Users\\Student\\Desktop\\shutil\\Folder B\\'

def modmove(source,dest1):
    for root, dirs,files in os.walk(source):  

        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)    

            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            if mtime > modified:
                shutil.copy(source + fname, dest1)
                print source + fname
modmove(source,dest1)

    
