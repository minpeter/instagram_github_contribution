import git
import os
import datetime

def commitRead():
    filename = "main.py" #임시

    #path = os.path.abspath(__file__)
    path = "/workspaces/instagram_github_contribution"
    repo = git.Repo(path)

    commits = list(repo.iter_commits("main", max_count=3))

    commitlog = """"""

    for i in commits:
        dd = i.committed_datetime.date() #하루에불러오는 10개의 커밋중 날짜만
        nd = datetime.datetime.now().date() #현제 날짜만
        if nd == dd:
            commitlog += str(i.message)
    return filename, commitlog
