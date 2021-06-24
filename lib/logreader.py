import git
import datetime


def gitlog(path):
    repo = git.Repo(path)
    commitlog = commitreader(repo)
    filename = bestfilebrowser(path)

    return commitlog, filename


def commitreader(repo):
    commits = list(repo.iter_commits("main", max_count=3))

    commitlog = """"""

    for i in commits:
        dd = i.committed_datetime.date() #하루에불러오는 10개의 커밋중 날짜만
        nd = datetime.datetime.now().date() #현제 날짜만
        if nd == dd:
            commitlog += str(i.message)
    
    return commitlog

def bestfilebrowser(path):
    g = git.Git(path)
    loginfo=g.log("--pretty=format:","--name-only --since '1 month ago'")
    filename = "main.py"
    print(loginfo)
    return filename

bestfilebrowser("/workspaces/instagram_github_contribution")