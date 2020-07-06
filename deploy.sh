#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "\033[0;32mBuilding website with hugo...\033[0m\n"

# Build the project.
hugo # if using a theme, replace with `hugo -t <YOURTHEME>`

# Go To Public folder
cd public

printf "\033[0;32mUpdating website repo...\033[0m\n"

# Add changes to git.
git add *

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin master

