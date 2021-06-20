import os
import git
from datetime import datetime

# print message
print("\033[0;32mBuilding website with hugo...\033[0m\n")

# run hugo
# os.system("hugo")

# changing directory
os.chdir("public")
print (os.getcwd())

repo = git.Repo(os.getcwd())

print(datetime.date(datetime.now()))


if repo.is_dirty(untracked_files=True):
    print('Changes detected.')
    repo.git.add('--all')
    repo.git.commit('-m','Rebuilding site ', print(datetime.date(datetime.now())))
    print(repo.remotes.origin.push('master'))
else:
    print('no changes', print(datetime.date(datetime.now())))

os.chdir("..")
print (os.getcwd())

repo = git.Repo(os.getcwd())

if repo.is_dirty(untracked_files=True):
    print('Changes detected.')
    repo.git.add('--all')
    repo.git.commit('-m', "rebuilding site ", print(datetime.date(datetime.now())))
    print(repo.remotes.origin.push('master'))
else:
    print('no changes', print(datetime.date(datetime.now())))
