"""
2.1

Define or describe the following phrases and commands as comments:
1. Git vs. GitHub
Git is a versiom control system that tracks changes to files
GitHub is an online platform that stores Git repositories and allows for collaboration on projects
2. Terminal vs. Command Line
Terminal is a program that lets you interact with respositories on your computer using text commands
The command line is the interface within the terminal where you type and execute commands
3. Local vs. Remote Repository
A local repository is stored on your own computer
A remote repository is stored on an online platform like GitHub
4. Version Control
Version control tracks changes to files over time, allowing you to revert to previous versions and collaborate with others
5. Staging Area
 The staging area holds changes that you have selected to include in the next commit.
6. git add
The git add command adds changes from the working directory to the staging area, preparing them to be committed.
7. git commit
The git commit command saves changes from the staging area to the local repository.
8. git push
The git push command uploads changes from the local repository to a remote repository, such as GitHub.
9. git status
The git status command shows the current state of the working directory and staging area, including which files have been modified, added, or deleted.
10. git pull
Downloads changes from the remote repository and updates your local repository.
11. pwd
Prints the current working directory, showing the full path to where you are in the file system.
12. ls
Lists the contents of the current directory.
13. cd
Changes the current directory to a specified directory.
14. nano
A simple text editor that allows you to create and edit files directly from the command line.
15. touch
Creates a new empty file.
16. mv
Moves or renames files or directories.
17. rm
Removes files or directories.
18. cat
Displays the contents of a file.
"""


"""
2.2

Questions:
• You have been plopped into Judy’s directory system. What command will tell you what your
current working directory is?
pwd
• The terminal responds by saying you are in ∼/python decal/judy decal. What command
will list all the files in your current working directory?
ls
• Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
You will need to pull the brianna repo repository to find the updated file. What command(s)
will let you move to the correct repository and pull the latest changes?
cd ../brianna_repo
git pull 
• How would you move this new homework.py to the homework/ folder in your personal repos-
itory?
mv homework.py ../judy_decal/homework/
• How would you move yourself to the same repository as homework.py?
cd ../judy_decal/homework/
• You want to see the contents of homework.py in your terminal, how would you do this?
cat homework.py
• Great job! You just finished the homework for this week. What command(s) allow you to
save the changes and push from your local repository to your remote repository?
git add homework.py
git commit -m "fixed typo in homework.py"
git push
• Oh no! Git gave you the following error. What commands should you call to resolve this
error and push your homework properly? What does the error mean? (i.e. what did “Judy”
do wrong when trying to push?)
! [rejected] main -> main (fetch first)
error: failed to push some refs to ’https://github.com
/judy/judy_decal.git’
hint: Updates were rejected because the remote contains
work that you do
hint: not have locally. This is usually caused by another
repository pushing
hint: to the same ref. You may want to first integrate
the remote changes
hint: (e.g., ’git pull ...’) before pushing again.
hint: See the ’Note about fast-forwards’ in ’git push
--help’ for details.
git pull origin main 
git push origin main
She tried to push her local changes without first pulling the changes that were already on the remote repository.
• What absolute path will allow you to move to Recents/?
csd /Users/username/Recents
"""

#3.1
def checkDataType(data):
    """
    This function takes in a variable and returns the data type of that variable.
    """
    return type(data)

#3.2
def evenOrOdd(num):
    """
    This function takes in a number and returns "Even" if the number is even, and "Odd" if the number is odd.
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#4

numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    """
    This function takes in a list of numbers and returns the sum of those numbers using a loop.
    """
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers))  # Output: 15   

#5.1
list = ['a', 'b', 'c']
def duplicateList(list):
    new_list = []
    for item in list:
        new_list.append(item)
        new_list.append(item)
    return new_list
print(duplicateList(list))  # Output: ['a', 'b', 'c', 'a', 'b', 'c']

#5.2
# wait im sorry can't see why this doesnt work...
def square(num):
    return num * num
print(square(5))  # Output: 25
