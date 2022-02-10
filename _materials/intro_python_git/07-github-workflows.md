---
title: "Github Workflows"
permalink: /materials/getting-started/07-github-workflows
toc: true
---

## Authentication

For those that are still having issues using Github locally through their terminal, I would highly recommend that you set up `ssh` authentication. Rather than having to add a personal access token for each repository, SSH is tied to your Github account and authenticates your local computer so that you set it up once and then can access all your remote repositories without having to enter passwords.

The instructions for setting up SSH are available here <https://docs.github.com/en/authentication/connecting-to-github-with-ssh> and the steps essentially breakdown as follows:

1. Check if you already have SSH keys set up <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys>. If you do, but you don't remember your passphrase for using them you'll want to delete them and start over by using `rm -rf ~/.ssh` 
2. Likely though you won't have any keys so you'll need to generate new ones. You can do that by following the steps outlined here <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key>
3. Next you'll add your created key to the ssh-agent <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent>
4. Then you can connect your ssh keys to Github by adding the key to your account with these steps <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>
5. Final step now is making sure that your local repository is connecting to Github via ssh. You can find the SSH url like this: 

![ssh_url]({{site.baseurl}}/assets/images/ssh_repository.png)

Now all you have to do is either add or set your remote url locally.

To add a remote url to your local repository, you can use the following command:
```sh
git remote add origin "your ssh url"
```

To set a remote url to your local repository, you can use the following command:
```sh
git remote set-url origin "your ssh url"
```

Now when you try to push to your local repository, you will be prompted for your password. And once that's done you should be able to access your Github repositories without any problems.

*Have any questions or issues? Either post it to Discord or message the instructor.*

## Github Workflows

### Add, Commit, and Push

So far our Github workflow has involved setting up a git repository locally (so `git init` or `git clone`) and then adding, committing, and pushing to the remote repository.

For reference, these our those commands:
```sh
git add . #Or name of files you want to add
git commit -m "message" #Or name of commit
git push origin main #Or name of branch
```

Seems pretty straightforward right? But what if we make some changes to both our remote and local repositories?

### Pulling

For example, try editing your README.md file in the Github Browser. You can do that by going to your Github repository and clicking on the pencil icon on your README file.

![github_repository]({{site.baseurl}}/assets/images/github_repository.png)

Then you should see a similar page:

![github_edit]({{site.baseurl}}/assets/images/github_edit.png)

Once you add your changes in that box, you commit them in the browser below where it says commit changes.

![github_commit]({{site.baseurl}}/assets/images/github_commit.png)

Now you're README on Github should be updated with your changes and look different than your local repository.

So how can we connect those changes?

With the handy `git pull origin main` command, we can pull down the changes from the remote repository and merge them into our local repository.

Try that command and then open your local README.md file and you should see the changes you made in the browser 🥳.

This workflow of adding, committing, and pushing to the remote repository is our main workflow, but sometimes you might have changes in your repository that you didn't add or that you added through the web interface, which is where pulling can be useful.

## Advanced Github Workflows

### Merge Conflicts
So far we've done a great job of keeping our local repository up to date with the remote repository, and vice versa. However that doesn't always happen. When they get out of sync, you'll often get errors, called `merge conflicts`.

Let's try and create a merge conflict to understand what that means and looks like.

1. Go back to your remote repository in Github and edit your README again. You can add anything but make sure to commit your changes.
2. Go back to your local repository and edit your README.md file as well, but make sure you edit something different than what you did in your remote repository. Add and commit these changes as well.
3. Now try and push your local changes to your remote repository. What happens? You should get an error saying that you cannot push up because there are merge conflicts or that your remote has newer changes.
![git_push_error]({{site.baseurl}}/assets/images/git_push_error.png)

4. To fix this error, you'll need to use `git pull origin main` to pull down the changes from the remote repository and then merge them into your local repository. You should see an error message about the merge conflicts when you pull down.
![git_merge_failed]({{site.baseurl}}/assets/images/git_merge_failed.png)

5. To merge the changes, you'll need to open your README file in your code editor. If you are in VS Code, you'll see something like this:
![git_conflict]({{site.baseurl}}/assets/images/git_conflict.png)

You can select which of the changes you want to keep and which you want to discard (or you can keep both). Then all you need to do is go back to our original workflow of adding, committing, and pushing to the remote repository.

*Have any questions or issues? Either post it to Discord or message the instructor.*

### Branches and Pull Requests

One way to avoid merge conflicts is to create a branch and then merge your changes into that branch.

This workflow is a bit more advanced and we won't be using it very often, but if you want to learn more feel free to check out Shane Lin's <https://shane-et-al.github.io/git_slab/#creatingcloning-a-repository#slightly-more-advanced-concepts> and the Github docs on branches <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches> and pull requests <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>.


