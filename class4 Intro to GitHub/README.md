## VERSION CONTROL SYSTEM 

Version control allows you to keep track of your work and helps you to easily explore the changes you have made, be it data, coding scripts, notes, etc. You are probably already doing some type of version control, if you save multiple files, such as Dissertation_script_25thFeb.py, Dissertation_script_26thFeb.py, etc. This approach will leave you with tens or hundreds of similar files, making it rather cumbersome to directly compare different versions, and is not easy to share among collaborators. With version control software such as Git, version control is much smoother and easier to implement. Using an online platform like [Github](https://github.com/) to store your files means that you have an online back up of your work, which is beneficial for both you and your collaborators. Git uses the command line to perform more advanced actions and we encourage you to look through the extra resources we have added at the end of the tutorial later, to get more comfortable with Git.

1. [Signing up for a new GitHub account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)
2. [Downloading GiHub Bash (CLI)](https://git-scm.com/downloads)

    ***NOTE:*** when you're intalling Git Bash make sure to download only the CLI only **NOT** the GUI (Uncheck where it ask for GUI)

3. Creating repository

![create repo](01 create repo.png)

3. [Setting your username in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git)

- `$ git config --global user.name “aiwithqasim”` (To set Username)
- `$ git config --global user.email “qasimhassan@saylani.org”` (To set UserEmail)

4. [Hello World to GitHub (Version Control System)](https://docs.github.com/en/get-started/quickstart/hello-world)

- `$ git clone <reo link>` (To clone data from GitHUb)
- `$ git status` (To check status of Track & untrack files i:e Stangging area)

Let's Follow now the traditional way again
- `$ git add fileName` (To add specific file)
- `$ git add -A <b>OR</b> $ git add . <b>OR</b>` (To add all files) 
- `$ git commit -m “first commit”` (To Commit your changes)
- `$ git push -u origin <branchName>` (To push data to GitHub)

5. Few more important commands that are recomended. I'll suggest you to try these commends on [Vislazing git simulator](https://git-school.github.io/visualizing-git/#free)
- `$ git branch -m master <branchName: main>` (To rename the branch name from **master** to **main**. Sometimes this step is not required)
- `$ git branch -vva` (work same as "$ git remote -va" by giving somr more details )
- `$ git branch -d <branchName>` (To delete branch )
- `$ git branch -dr origin/<branchName>` (to delete branch from Origin/ base repository)

We had tried to cover a lot major commands as much as we can. if you till feel hesitation feel free to explore by yourself through below given Resources.

- [BOOK: Learn version Control System using Git](https://github.com/aiwithqasim/Saylani-AI-Batch2/blob/main/02%20Version%20control%20System/learn%20version%20control%20with%20Git.pdf)
- [CHEATSHEET: Github cheatsheat](https://github.com/aiwithqasim/Saylani-AI-Batch2/blob/main/02%20Version%20control%20System/Git-Cheatsheet.pdf)
-  All below commands are concluded to get to know most of the important commands in the [book (Learn version Control System using Git)](https://github.com/aiwithqasim/Saylani-AI-Batch2/blob/main/02%20Version%20control%20System/learn%20version%20control%20with%20Git.pdf)


### Chapter # 01:
- $ git clone https://github.com/gittower/git-crash-course.git (To clone data from GitHUb)
- $ git status (To check status of Track & untrack files i:e Stangging area)
- $ git config --global user.name “John Doe” (To set Username)
- $ git config --global user.email “john@doe.org” (To set UserEmail)
- $ git config --global color.ui auto (To autoamte the coloue Scheme)
- $ cd <path/to/project/folder> (To change the directory)
- $ git init (To initialize the repository)
- $ git init --bare (inittialize Git without making .git folder and place its files outside)
- $ ls -la (To list down all the contect in your Working Directory)
- $ git add -A <b>OR</b> $ git add . <b>OR</b> $ git add fileName (To add changes to git)
- $ git commit -m “Initial commit" (To Commit your changes)
- $ cd your/development/folder/ (To change your directory)
- $ git add new-page.html index.html css/*  (To add Specified name to Git )
- $ git commit -m “Implement the new login box” (To Commit your changes)
- $ git log (To check you activity History)

### Chapter # 02:
- $ git branch contact-form (To create branch by name of Contact-form)
- $ git branch -v (to list down number of branches with little detail)
- $ git status (To check status of Track & untrack files i:e Stangging area)
- $ git stash (To add files as temporary file to clipborad without uploading it into Github)
- $ git status (To check status of Track & untrack files i:e Stangging area)
- $ git stash list (To list down all stash that you added in clipborad)
- $ git checkout contact-form (To move from one brach to another)
- $ git add contact.html (To add files to Git)
- $ git commit -m "Add new contact form" (To Commit your changes)
- $ git log (To check you activity History)
- $ git checkout master (To move from one brach to another)
- $ git merge contact-form (To merge files of contact-form NOTE:To merge files you must have to ib the specified branch in master if to add contact branch to master)
- $ git log(To check you activity History)

### Chapter # 03:

- $ git remote add origin https://github.com/EnggQasim/test1.git (To set origin where you want to push your dat)
- $ git remote -v (Show number of remote repositories connected to your Working directory)
- $ git branch -va (work same as "$ git remote -v" by giving somr more details )
- $ git fetch origin master (To fetch the changes from main repository)
- $ git fetch origin (To fetch file from origin NOTE: origin is the main master directory the store by github in orgin)
- $ git log origin/master  (To check you activity History of master branch)
- $ git pull (To pull file from origin NOTE: origin is the main master directory the store by github in orgin)
- $ git checkout <branchName> (To move from one brach to another)
- $ git push -u origin <branchName> (To push data to GitHub)
- $ git branch -vva (work same as "$ git remote -va" by giving somr more details )
- $ git branch -d <branchName> (To delete branch )
- $ git branch -dr origin/<branchName> (to delete branch from Origin/ base repository)
  </br>
- $ git remote add origin <link> (To set origin where you want to push your data)
- $ git remote add origin <"clone"> -f
- $ git push origin master(To push data to GitHub) <b>OR</b> git push origin master -f(To push data to GitHub forefully NOTE: we always try to aviod use of this branch)
- $ git clone <repoName> (To clone data from GitHUb)
- $ git pull origin master (To pull file from origin NOTE: origin is the main master directory the store by github in orgin)
  </br>
- $ git push -u origin <branch> -f (push local brach on server)
- $ git push --all -u (push all things on remote server)
- $ git pull --all (pull all data from server)

if you have local colne you can remane by following steps:
- git branch -m master main
- git fetch origin
- git branch -u origin/main main

BY: Qasim Hassan(SMIT04588)