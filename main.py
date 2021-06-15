from git import *
from time import (time, altzone)
import datetime
from cStringIO import StringIO
from gitdb import IStream

repo = git.Repo("/home/minpeter/instagram_github_contribution")

commits = list(repo.iter_commits("main", max_count=5))

dir(commits[0])


repo = Repo('path/to/repo')

message = 'Commit message'

tree = repo.index.write_tree()
parents = [ repo.head.commit ]

# Committer and Author
cr = repo.config_reader()
committer = Actor.committer(cr)
author = Actor.author(cr)

# Custom Date
time = int(datetime.date(2013, 1, 1).strftime('%s'))
offset = altzone
author_time, author_offset = time, offset
committer_time, committer_offset = time, offset

# UTF-8 Default
conf_encoding = 'UTF-8'

comm = Commit(repo, Commit.NULL_BIN_SHA, tree, 
      author, author_time, author_offset, 
      committer, committer_time, committer_offset,
      message, parents, conf_encoding)