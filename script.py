from io import BytesIO
from zipfile import ZipFile
import urllib.request
#import requests # Alternative using the request library (no header required)
import os
from tqdm import tqdm

# Progress bar class setup
class TqdmUpTo(tqdm):
    # Source: https://gist.github.com/leimao/37ff6e990b3226c2c9670a2cd1e4a6f5
    """Alternative Class-based version of the above.
    Provides `update_to(n)` which uses `tqdm.update(delta_n)`.
    Inspired by [twine#242](https://github.com/pypa/twine/pull/242),
    [here](https://github.com/pypa/twine/commit/42e55e06).
    """

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize

# Where all the actions happens:
if __name__ == '__main__':
    # Setting up the base file
    urlprefix = "https://share.vx-underground.org/Conti/Training%20Material%20Leak/conti.7z."
    # Download file to a new folder within the current working directory, i.e. './'
    filepath = "./TrainingMaterialLeak"
    # Extension of the file
    ext = ".7z"

    # Some servers block bot scripts, so we setup a header identifying ourselves as a browser.
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    # Here we loop from the first file to the last file, i.e. n + 1.
    for i in range(1, 267):
        # We craft our URL
        url = urlprefix + str(i).zfill(3)
        filename = 'conti' + ext + '.' + str(i).zfill(3)
        print(f"Downloading: {url}")
        
        # We declare our save location
        fullfilename = os.path.join(filepath, filename)
        print(f"Saving as: {fullfilename}")
        
        # We start the download
        with TqdmUpTo(unit = 'B', unit_scale = True, unit_divisor = 1024, miniters = 1, desc = filename) as t:
            urllib.request.urlretrieve(url, fullfilename, reporthook = t.update_to)
            #requests.get(url, stream=True) # Alternative using the requests library (no header required)
        
        #zf = ZipFile(BytesIO(data))
        #zf.extractall()
