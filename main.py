from git import *
import datetime

repo = Repo("/home/minpeter/instagram_github_contribution")

commits = list(repo.iter_commits("main", max_count=10))



for i in commits:
    dd = i.committed_datetime.date() #하루에불러오는 10개의 커밋중 날짜만
    nd = datetime.datetime.now().date() #현제 날짜만
    if nd != dd:
        quit()
    print(i.message)