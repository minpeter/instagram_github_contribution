from lib import logreader, fileopener, imaging, upload
import os

path = os.getcwd()
filename, commitlog = logreader.gitlog(path)
msg = fileopener.fileopen(filename)
imaging.imageMaker(msg)
upload.upLoad(commitlog)