import git
import datetime
import imaging
import upload
import os

path = os.path.abspath(__file__)
repo = git.Repo(path)

commits = list(repo.iter_commits("main", max_count=3))

msg = """
===This is Test code====
"""

commitlog = """
++++TEST+++++
"""

f = open("main.py", 'r')
lines = f.readlines()
for line in lines:
    msg += str(line)
f.close()

for i in commits:
    dd = i.committed_datetime.date() #하루에불러오는 10개의 커밋중 날짜만
    nd = datetime.datetime.now().date() #현제 날짜만
    if nd == dd:
        commitlog += str(i.message)

imaging.imageMaker(msg)
upload.upLoad(commitlog)
