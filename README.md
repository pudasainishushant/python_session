## Setting up vistual environments in anaconda
### List all virtual environments in your system/device
conda info --envs

### Create a new virtual environment in conda
conda create -n name_of_virtual_environment python=3.x.x

### Activate virtual environment
conda activate virtual_environment_ko_name

### View packages in virtual environment
pip list

### Install packages in virtual environment
pip install package_ko_name

### Uninstall packages in virtual environment
pip uninstall package_ko_name


# GIT commands

## Setting git global username and email
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"

## cloning a git repo
git clone url_of_repo

## pulling latest changes from a branch
git pull origin branch_name

## adding files to staging server
- for all file 
    git add .
- for specific file
    git add filename

## commiting files to staging server
git commit -m "commit_message_here


## pusing to git server
git push origin branch_name

# Branching and merging
## View all branches
git branch -a

## Create new branch
git checkout -b branch_name

## Switch to another branch
git checkout branch_name

## Merge another branch from main
git merge branch_name
