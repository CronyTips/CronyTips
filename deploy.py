import os
import git

# print message
print("\033[0;32mBuilding website with hugo...\033[0m\n")

# run hugo
os.system("hugo")

# changing directory
os.chdir("public")

# getting current repo
repo = git.Repo(os.getcwd())

# if any changes for the website push it
if repo.is_dirty(untracked_files=True):
    print("\033[0;32mRebuilding website...\033[0m\n")
    repo.git.add('--all')
    repo.git.commit('-m','rebuilding site')
    print(repo.remotes.origin.push('master'))
else:
    print('no changes')

# going back
os.chdir("..")

repo = git.Repo(os.getcwd())

# checking for new content and pushing it
if repo.is_dirty(untracked_files=True):
    print("\033[0;32mPushing new content...\033[0m\n")
    repo.git.add('--all')
    repo.git.commit('-m', "new content added")
    print(repo.remotes.origin.push('master'))
else:
    print('no changes')

print("\033[0;32mDeployment finished...\033[0m\n")
