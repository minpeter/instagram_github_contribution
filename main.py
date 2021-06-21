from lib import logreader, fileopener, imaging, upload

filename, commitlog = logreader.commitRead()
msg = fileopener.fileopen(filename)
imaging.imageMaker(msg)
upload.upLoad(commitlog)