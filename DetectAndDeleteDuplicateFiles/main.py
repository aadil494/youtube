# created by Aadil Matloob jan
# youtube: https://www.youtube.com/channel/UCTXiHVtLmYCRr_xGoWeefqg
from tkinter.filedialog import askdirectory
from tkinter import Tk
import os , hashlib
from pathlib import Path
Tk().withdraw()
path =  askdirectory(title="Select a folder")

file_list = os.walk(path)

unique = dict()
for root,folders,files in file_list:
    for file in files:
        path = Path(os.path.join(root,file))
        fileHash = hashlib.md5(open(path,'rb').read()).hexdigest()
        print(len(fileHash))
        if fileHash not in unique:
            unique[fileHash] = path
            
        else:
            os.remove(path)
            print(f"{path} has been deleted")
