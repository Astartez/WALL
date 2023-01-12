from os import listdir
from os.path import isfile, join
PATH = "../"
filelist = ["http://127.0.0.1:8000/" + file.replace(" ", "%20") for file in listdir(path=PATH) if isfile(join(PATH, file))]
print(*filelist, sep="\n")