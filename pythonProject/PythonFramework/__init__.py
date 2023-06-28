#here we are creating a new project pythonframeworks
#and we created 2 packages pythonframework and utilities
#pythonframework will have the test cases and utilities we are using to store any class where
#reusable components are there



#page object design- in this design we will keep the objects in respective pages which is nothing but
#keeping the webelements of a particular page in the respective python files

#in base class we are keeping the utilities like which is reusable components like
#for the main fixture setup, just inherit the class and setup will be done, then logger method,
#explicit wait method and select method for dropdown
#base class things we need everytime hence we keep here so once we inherit we can use directly

#in conftest we are keeping all the fixtures- setup, hooks-parser- for options on runtime browser selection
#hooks for taking screenshot on failure
#these things we are keeping here coz like setup we need to do it for all the test class once
# and no need in other time similarly and other things like option at runtime and screenshot code those
#also we dont know when its needed it depends on the code


#page objects is in separate files as we need to create objects for accesing the webelements only when they are needed



#now we will use jenkins CI tool and integrate our Framework into jenkins Continous integration tool, its
#like automatically running the suite at a scheduled time

#first from google download jenkins , this will run on our local server
#after downloading open cmd and go to the path where its downloaded and write this command-
#java -jar jenkins.war -httpPort=8080
#this means invoke a jar file and open jenkins in local server 8080
#now go to browser and open localhost:8080, username password already set for Test/Test
#new item-freestyle project
#go to project from dashboard and click on configure>Advanced >check custom work space>
#project path paste here>build steps>select execute windows batch command>put the cmd commands here
#now check this project is parameterized>choose choice parameter and enter the choices and the variable name
#we can use this for URL selection as well
#cd PythonFramework
#cmd command-
#py.test --browsername "%browsername%" -v --html=$WORKSPACE/reports/reports.html -v --junitxml="results.xml"
#cd PythonFramework
#py.test --browsername "%browsername%"(parameterization in jenkins )
# --html=$WORKSPACE/reports/reports.html(WORKSPACE will store the custom project directory)
# -v --junitxml="results.xml"(junit results xml plugin)


#Git and Github
#Github is a version control tool like a central repositary
#Git is used to communicate to Guthub
#first install git  from-https://git-scm.com/
#then create a account in git hub-https://github.com/ already created an account-TestJeet12/TestJeet12
#create a repository- already created- PythonLearnings
#basic commands of git can be found in https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html#:~:text=%20%20%20%20Git%20task%20%20,clone%20username%40host%3A%2Fpath%2Fto%2Freposit%20...%20%2021%20more%20rows%20
#now open command promt and navigate to location where the project is present using cd command
#first we have to tell as whom we are logging in
#commands-git config --global user.name "Sam Smith"
#next we have to give the mail id
#commands-git config --global user.email "sam@example.com"
#now we have to initialize the git local repository
#commands-git init, this will create a hidden .git file which will have all the info for push and
#pull from repository
#there are 3 stages , first initialize the local repository , then add to staging and then commit and then
#push to github
#staging command- git add *, * for adding all the things , or we can specify any particular file as well
#now confirm the files by command git status
#now commit- git commit -m(for message) "first commit"
#now first mention the repository details- git remote add origin <server>(server link we can get from the
# github repository) ex-git remote add origin https://github.com/TestJeet12/PythonLearnings.git
#now push to github- git push origin master(at first we will have only master branch)
#in case of any certificate issue execute this command-git config --global http.sslbackend schannel
#in general practice we cannot commit/push in main branch we have to create clone of the master branch
#and then work on it and then work on it then merge to master branch
#create a new branch-git checkout -b <branchname>
#to check the branches- git branch
#to switch to any branch-git checkout <branchname>

#now first time if we need the project from git then we need to clone it-
#Create a working copy of a local repository:
#git clone /path/to/repository
#For a remote server, use:
#git clone username@host:/path/to/repository
#ex-git clone https://github.com/TestJeet12/PythonLearnings.git
#now next time we can pull the latest changes-
#git pull
#Update from the remote repository	Fetch and merge changes on the remote server to your working directory:	git pull
#to merge changes of any branch to master-
#To merge a different branch into your active branch:
#git merge <branchname>
#merge conflict- occurs if someone is working on master branch and made some changes but didnt push
#another person working on same project and made some changes in another branch but on same file and pushed
#now while merging both there will be conflict that time we have to resolve personally and then make the
#same changes to file and then merge again.


