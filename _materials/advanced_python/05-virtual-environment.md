---
title: "Python Virtual Environments"
permalink: /materials/advanced-python/05-virtual-environment
toc: true
---

*If you already have experience with virtual environments and have a preferred setup, feel free to keep using what you have*

## What is virtual environment?

This past week we started exploring Python libraries that ship with Python when you install it on your computer, but that still need to be imported so that we can use it (remember Pathlib!). Now we're going to start installing additional libraries that don't ship with Python. However, before we install these libraries, we need to create a virtual environment. A virtual environment is necessary to keep the libraries we install contained to each project.

The Python documentation explains that "Python applications will often use packages and modules that don’t come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library’s interface.

This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages." You can read more here about [virtual environments](https://docs.python.org/3/library/venv.html#venv-def).

Prior to installing our virtual environment, let's make sure that you have the latest version of `pip`, which stands for "Python Installs Packages." Pip comes built-in to Python, but run this code to ensure you have the right version.

![install pip]({{site.baseurl}}/assets/images/install_pip.png)

If you get any errors, you can check if you have pip installed [https://stackoverflow.com/questions/40868345/checking-whether-the-pip-is-installed](https://stackoverflow.com/questions/40868345/checking-whether-the-pip-is-installed)

Now we'll install `venv` (follow instructions) [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html). One thing to note is that there are LOTS of different ways to setup your virtual environment (which lots of people have *very* strong feelings about). I like this answer from Stack Overflow for giving an overview of the differing options [https://stackoverflow.com/a/65854168/7437781](https://stackoverflow.com/a/65854168/7437781). 

*If you get an error message, message the instructor on Discord*

## Try It Out

```sh
python3 -m venv is310-venv
```

Now you need to activate your virtual environment.

```sh
source is310-venv/bin/activate
```
The source command is specific to virtual environments and is essentially telling your terminal to run all your subsequent commands in the virtual environment.

Depending on how you have your terminal configured you'll see the name of your environment in the terminal.

Now try installing the package Beautiful Soup

```sh
pip3 install beautifulsoup4
```

You can test if it worked by starting your python interpreter with the `python3` command and running the following code:

```shell
import bs4
bs4.__version__
```
Which should show the version of Beautiful Soup you have installed.

You can double check that this installation worked by opening up your current directory in your code editor and looking through the folders of your virtual environment. Under `lib`, you should see a folder called `python_version/site-packages` and that will show you all the Python libraries you have installed.

## Virtual Environments in VS Code

<div class="notice--info">⚡️ This information has been adapted from <a href="https://techinscribed.com/python-virtual-environment-in-vscode/">https://techinscribed.com/python-virtual-environment-in-vscode/</a></div>

While you can use the built-in venv module with any IDE, since I've recommended that you use VS Code, I wanted to share instructions specific to that editor.

Rather than only using venv, I would recommend using `virtualenv` instead since VS Code struggles to find virtual environments in the same directory as the project.

To do that first we need to install `virtualenv`, which you'll do globally like so:

```sh
pip3 install virtualenv
```

Then make sure you're in to the home directory of your computer:

```sh
cd ~
```

Then create a directory for all your virtual environments:

```sh
mkdir .virtualenvs
cd .virtualenvs
```

And finally create a new virtual environment:

```sh
virtualenv is310-venv
```

Now we follow similar steps to above where we activate our virtual environment:

```sh
source is310-venv/bin/activate
```

And then try installing libraries:

```sh
pip3 install beautifulsoup4
```

The key difference here is that any time you want to activate your virtual environment, you need to do it from the home directory and specifically in the `.virtualenvs` folder.

*Have any additional questions? Either ask them in our Discord or message the instructor*
