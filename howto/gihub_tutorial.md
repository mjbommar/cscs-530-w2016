##Using the GitHub Website

####Create a GitHub Account
1. Using a browser of your preference, navigate to http://www.github.com and create a username and password and then clicking "Sign Up for GitHub"

####Create a New Repository
1. Sign in to your github account at http://www.github.com

2. In the right hand column, next to the label "Your repositories" click the green button with the label "+ New Repository
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6286773/0e0220e8-b8d9-11e4-9d7e-1389ebf1ff53.png" height=100px</img>
</div>

3. Type in a name for your repository in the "Repository Name" box. Here, I use cscs-530-github-tutorial (Note: Avoid spaces and upper case letters, this prevents confusion and more work later!). Hint: Name it something unique so you know what the repository is for, a CSCS530 project, perhaps? Enter a description for the repository if you'd like

4. Click "Initialize this repository with a README" and keep all other default options

5. Click "Create Repository" 

####Editing *.md (markdown) Files
1. In your new repository, click the "README.md" link under the section "Initial commit"

2. Click the pen button at the top of the README.md file, to the left of the trash can button to edit the README.md file
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6286891/7b69e944-b8da-11e4-8887-c4509883fbc3.png" height=50px</img>
</div>

3. Edit the file to your liking, using Github Markdown syntax. See this page for some tips:
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

4. Under the "Commit Changes" box under the markdown page, you can change the "Update README.md" text in the first, shorter (or thinner) box. This is your "commit message" that displays next to your file in the GitHub directory. You can change this commit mesage to anything you'd like, but keep it simple so others know what was changed. Since you are updating the README.md, let's leave it for now. An extended description in the larger text box is optional, so that you can let your collaborators know exactly what you changed into the future

5. Click "Commit changes" to push your changes to your GitHub repository

####Creating *.md (markdown) Files
1. Navigate to the top page of your GitHub repository (where it shows all of the files that you currently have uploaded. For now, it should just be README.md)

2. Click the blue + button next to the name of your GitHub repository
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6287252/35a3c03e-b8de-11e4-9156-6e77f9c4c41e.png" height=50px</img>
</div>

3. At the top of the page, replace "name your file..." with a file name that ends with .md (so GitHub knows that it is a markdwon). Here, I use test.md

4. Follow steps 3 - 5 in the "Editing *.md Files" section above to edit and commit changes to your new markdown file

####Downloading Individual Files
1. In your new repository, at the front page click "README.md"

2. Right click "Raw" in the upper right hand corner of the README.md section and select "Save link as" -- Save the file to anywhere in your machine. This will download the "raw" (i.e., original) version of the file. This technique is most useful on files that you want to open up "locally" on your machine (i.e., not in a web-browser). Examples include: *.docx, *.ppt, or *.ipynb
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6286891/7b69e944-b8da-11e4-8887-c4509883fbc3.png" height=50px</img>
</div>

3. Use this technique only when you want individual files from a repository and are not planning to contribute any changes. For contributing changes to a repository, you should clone the repository. See below. 

##Installing the GitHub Client

###GitHub Client Install for Mac OS X
__Download Github Graphical User Interface Client__

1. Using a browser of your preference, navigate to: https://mac.github.com/

2. Click the blue button "Download GitHub for Mac"
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6279179/1112bda0-b86c-11e4-9786-b5b387f3b851.png" height=40px</img>
</div>

3. Navigate to the folder where you have downloaded the file. In our case, the file that we just downloaded is named: "GitHub for Mac 199.zip" 

4. Double click "GitHub for Mac 199.zip" -- this will automatically create a new file named "GitHub" in the same folder as your zip file. The icon will look like this
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6279530/a08a4814-b870-11e4-8c15-39825a82d327.png" height=80px</img>
</div>

5. Double click the new GitHub icon. You may be prompted with a warning that "GitHub" is an application downloaded from the internet. Click "Open" then select "Do Not Move" when the GitHub client asks if you'd like to move the application to your home applications directory (you can do this yourself later)

6. Once a blank GitHub screen has loaded, navigate to the upper left hand corner of your screen and select GitHub, then select Preferences

7. At the following window, click the "Accounts" icon, and enter your GitHub user credentials, and click "Sign in" 


###GitHub Client Install for Windows
__Download Github Graphical User Interface Client__

1. Using a browser of your preference, navigate to https://windows.github.com/

2. Click the green button "Download GitHub for Windows" 
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6287356/e123e9b6-b8de-11e4-887c-31dcb0f48233.png" height=80px</img>
</div>

3. Navigate to the folder where you have downloaded the file. In our case, the file that we just downloaded is named: "GitHubSetup.exe" -- The icon will look like this
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6279530/a08a4814-b870-11e4-8c15-39825a82d327.png" height=80px</img>
</div>

4. Right click on the icon and select "Run as Administrator" -- When it prompts you about a security warning, click "Install"

5. GitHub will automatically load once the install is finished. Once the program loads, at the welcome screen, it will request that you enter your GitHub user credentials (i.e., username and password). Enter these, and click "Log in" 

6. Next, at the Configure tab, enter your Name (upper text bar) and E-mail (lower text bar), or leave it at the default values that it sets at (should be something that you entered when you signed up for your GitHub account). Click "Continue"

7. At the next screen, it will say that there were no repositories found, click the blue "Dashboard" word link. 

## Using the GitHub Client (for both Windows and OS X)
###Cloning a Repository
1. With the GitHub client loaded, click the + button in the upper left hand corner of the window

2. Select "Clone"

3. In the second screen, you will be able to view all of the GitHub repositories that you have access to or are following. The GitHub repository (cscs-530-github-tutorial) that you created in the previous section will be there. 

4. Select cscs-530-github-tutorial (or whatever you named your repository in the previous section), and click "Clone cscs-530-github-tutorial" -- A new window will appear, prompting you to select a location on your computer where you want to clone the repository to. For now, let's use your Desktop. Note: This will create a new folder on your Desktop named cscs-530-github-tutorial (or whatever you named your repository in the previous section).

IMPORTANT: This folder is NOT your actual GitHub repository. It is a clone of it. Anything you change on your computer will not change in GitHub unless you commit the changes (see below). Therefore, if you delete the folder, nothing will change in the GitHub repository, nor will you lose anything, unless you delete it explicitly from GitHub. If you delete items from the folder, you must push these changes to delete items from the GitHub repository. However, this is easily recoverable (see Recovering Deleted Data from GitHub)

###Adding Files to a Repository
1. With the GitHub Client open in the background, click and drag any item that you want to add to your GitHub repository to the new cscs-530-github-tutorial (or whatever you named your repository in the previous section) folder that was added to your desktop.

2. In OS X: Under the "Changes" tab, you will be able to see the new file that was just added
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6289761/6df15d2c-b8f0-11e4-8f2e-3f753545a236.png" height=120px</img>
</div>
   In Windows: You will see a new "Uncommited changes" section revealed in your GitHub client window. Click the blue button next to "Show" and you should see a panel in the existing window containing the file that was just added
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6289835/f1085512-b8f0-11e4-8dd6-5f49112e3146.PNG" height=180px</img>
</div>

3. Enter a summary and description of the file that you added

4. Click "Commit to master" -- Your file will now be on the GitHub repository

5. Click the "Sync" with the circular arrow icon in the upper right hand corner to sync the changes that you made using GitHub client and the local Desktop folder with your new GitHub Repository 

## Recovering Deleted Data from GitHub
1. If a file has been deleted from a folder, and the GitHub repository was updated without the file, you can recover your data.

2. In the "History" section of GitHub, select the item that you want to "revert" or "roll back" to.

   IMPORTANT: Revert and Rollback are different in Github.
   Revert - Undo the action in the commit that you specify
   Rollback - Delete all committed changes up to the commit that you specify

3. In Mac OS X: Select the commit in the history that you want to revert to, and in the right hand preview panel of the file that you want to revert the deletion of, click the "gear" symbol with the downwards pointing arrow next to it, and select "Revert this Commit" 
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6290306/ea156b52-b8f3-11e4-9522-782aa702dc59.png" height=180px</img>
</div>
   In Windows: Select the commit in the history that you want to revert to, and in the right hand preview panel of the file that you want to revert the deletion of, click the "Revert" icon
<div style = text-align:center;>
<img src="https://cloud.githubusercontent.com/assets/6100156/6294974/854fd544-b8f4-11e4-966a-0b063b6dbfee.PNG" height=80px</img>
</div>

4. The file will return to your local cloned directory and to your GitHub repository. Click "Sync" in the upper right hand corner to sync your changes
