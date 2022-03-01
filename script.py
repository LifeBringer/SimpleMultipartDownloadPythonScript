from io import BytesIO
from zipfile import ZipFile
import urllib.request
import requests
import os
from tqdm import tqdm

urlprefix = "https://share.vx-underground.org/Conti/Training%20Material%20Leak/conti.7z."
filepath = "./TrainingMaterialLeak"
ext = ".7z"

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for i in range(1, 267):
    url = urlprefix + str(i).zfill(3)
    filename = 'conti' + ext + '.' + str(i).zfill(3)
    print("Downloading", url)
    fullfilename = os.path.join(filepath, filename)
    print(fullfilename)
    urllib.request.urlretrieve(url, fullfilename)
    #requests.get(url, stream=True)
    #zf = ZipFile(BytesIO(data))
    #zf.extractall()