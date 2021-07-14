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


## Basic Python

python file extension -- .py
jupyter notebook file extension -- .ipynb


Jupyter notebook shortcuts
- Insert new cell - B
- Insert new cell above - A
- Convert cell to markdown - M
- Convert cell to code - Y
- Run cell - Shift+ Enter


# Questions to solve

Q1. Create a function that takes a number and return the number of digits in the number

example ---> number = 10 number of digits = 2

Q2. Create a program that takes temperature asks user to convert in which scale (celsius, kelvin, farenhait) and print the converted value.

Q3 . Create a function that converts a date formatted as mm//dd/yyyy to yyyyddmm.
example ----> input 07/09/2020 to 20200907

Q 4. Ask user to enter three numbers 
x = 1
y = 2
z = 1
 create a list like this:
 [[0,0,0],[0,1,0],[0,0,1],[1,0,0],[1,1,1],[0,2,0],[1,2,0],[1,2,1],[0,2,1]]
 

## Exerices
- Write a Python program to convert a given list of strings into list of lists using map function. 
Input
['Red', 'Green', 'Black', 'Orange']

Output:
[['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

- Write a python program to filter prime numbers only from a given list of numbers

- Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.

- Use list comprehension to contruct a new list but add 6 to each item.

input = [44,54,64,74,104]
output = [446,546,646,746,1046]


- Inbuilt python modules
 example: sys, os, random, math

 - Third party libraries
 example: geopy, opencv, nltk, flask, tensorflow,facebook_scrapper


 - Flask
 - Django
 - FastAPI


 ## Project 1:
 Develop a wikipedia search engine web application using Python, Flask, HTML, CSS, JS.
 Step 1:
 - Develop a python module in OOP style which can get search results from wikipedia given any search queries.
-  wikipedia.py module retieve_search_results() get_wiki_pages()
- Give wiki search results
- Give users summary about something from wikipedia
Step 2:
- HTML, CSS, JS use garera templates haru ready garne
Step 3:
_ Flask use garera api.py banaune 

Functionalities 
- User le wiki search garna paunu paryo
- User le deko query ko summary generate garera dekhaidinu paryo
- User le language select garna paunu paryo

Learning objectives
- use of python modules (third party library)
- OOP
- Flask
- Simple web page design