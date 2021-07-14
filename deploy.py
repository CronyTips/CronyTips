import os, git, subprocess

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
    subprocess.call("git add --all")
    subprocess.call('git commit -m "Rebuilding website" ')
    subprocess.call('git push origin master')
else:
    print('no changes')

# going back
os.chdir("..")

repo = git.Repo(os.getcwd())

# checking for new content and pushing it
if repo.is_dirty(untracked_files=True):
    print("\033[0;32mPushing new content...\033[0m\n")
    subprocess.call("git add *")
    subprocess.call('git commit -m "New content added" ')
    subprocess.call('git push origin master')
else:
    print('no changes')

print("\033[0;32mDeployment finished...\033[0m\n")
