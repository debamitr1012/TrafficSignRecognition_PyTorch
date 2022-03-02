Contributing Guidelines:
This documentation contains a set of guidelines to help you during the contribution process.
We are happy to welcome all the contributions from anyone willing to improve/add new scripts to this project.
Thank you for helping out and remember, no contribution is too small.

Submitting Contributions:
Below you will find the process and workflow used to review and merge your changes.

Step 1 : Find an issue
Take a look at the Existing Issues or create your own Issues!
Wait for the Issue to be assigned to you after which you can start working on it.
Note : Every change in this project should/must have an associated issue

Step 2 : Fork the Project
Fork this Repository. This will create a Local Copy of this Repository on your Github Profile. Keep a reference to the original project in upstream remote.
$ git clone https://github.com/rimsha-salahuddin/TrafficSignRecognition_PyTorch.git
$ cd TrafficSignRecognition_PyTorch.git
$ git remote add upstream https://github.com/rimsha-salahuddin/TrafficSignRecognition_PyTorch.git

-If you have already forked the project, update your copy before working.
$ git remote update
$ git checkout <branch-name>
$ git rebase upstream/<branch-name>

Step 3 : Branch
Create a new branch. Use its name to identify the issue your addressing.

# It will create a new branch with name Branch_Name and switch to that branch
$ git checkout -b branch_name

Step 4 : Work on the issue assigned
-Work on the issue(s) assigned to you.
-Add all the files/folders needed.
-After you've made changes or made your contribution to the project add changes to the branch you've just created by:
# To add all new files to branch Branch_Name
$ git add .

Step 5 : Commit
Before submitting an issue please find the correct folder where your program will go , You can discuss about it in the discussion.

-To commit give a descriptive message for the convenience of reveiwer by:
# This message get associated with all files you have changed
$ git commit -m "message"
NOTE: A PR should have only one commit. Multiple commits should be squashed.

Step 6 : Work Remotely
Now you are ready to your work to the remote repository.
When your work is ready and complies with the project conventions, upload your changes to your fork:
# To push your work to your remote repository
$ git push -u origin Branch_Name

Step 7 : Pull Request
Go to your repository in browser and click on compare and pull requests. Then add a title and description to your pull request that explains your contribution.

Your Pull Request has been submitted and will be reviewed by the moderators and merged.
