---
title: "Python Fundamentals 🐍"
permalink: /materials/intro-python-git/04-python-fundamentals
toc: true
---

Python interpreter is great, but why might we not want to write all our code in the interpreter? What happens every time you quit?

SOLUTION:

1. Open your terminal directory in Visual Studio Code or your favorite code editor, and create a new file:

```sh
touch first_script.py
```

You should see this file in Visual Studio Code. We're going to write your first code script! Feel free to enter some of what you wrote for the exercise, or copy this below:

```python
tools = [
    {
        'name':'HathiTrust',
        'projects': ['Bookworm', 'Google Ngram Viewer']
    },{
        'name': 'Gephi',
        'founded_year': 2008
    }
]
```

1. Now try running the file from your terminal
Make sure you are not in the python interpreter. Type:

```sh
python3 first_script.py
```

What happens?

![https://media.giphy.com/media/3KCOFfdqmptLi/giphy.gif](https://media.giphy.com/media/3KCOFfdqmptLi/giphy.gif)

Because we aren't in the interpreter any more, unless we tell the computer to output a value it won't show us any message (unless there's an error.)

One solution is the **print** method.

In first_script.py, add the line to the bottom of the script:

```python
print(tools)
```

This time you should see the list of tools.

Now try moving that line to the top of first_script.py and running the script again.

![https://media.giphy.com/media/qQI16x8tgp7nW/giphy.gif](https://media.giphy.com/media/qQI16x8tgp7nW/giphy.gif)

We've hit a problem. Let's break down what happened here. If the print statement was at the bottom of the script it worked, but if it was at the top it didn't.

That's because the print statement within it's parentheses references the variable `tools`, but we haven't defined that variable yet.

**Computers read code from top to bottom**

### So what's the print statement?

Print is a *built-in Python method*, which means it comes installed with Python and we can use it whenever we are writing Python.

Print is used to literally print out values to the terminal, and it's one of many ways to find out the output of a Python script.

## Built-In Methods

Print is one of many methods. Let's take a look at a few more.

1. `Len()`
In first_script.py, move the print statement back to the bottom of the script. Then above the print statement type:

```python
tools_numbers = len(tools)
print('how many DH tools do we have?', tools_numbers)
```

Then try running the code. You should first see our question followed by a number and then the list of projects.

The **len** method can return the length of any list, dictionary, or string in Python.

2. `Type()`
You might also want to know the **type** of your variable, whether it's a data type or a data structure. In first_script.py, add to the bottom of the script:

```python
print(type(tools), type(tools[0]))
```

Once you run the script you should see that we have both a list and a dictionary. With print statements you can add multiple items as long as they are separated by commas, and you can use built-in methods inside the print statement, instead of assigning them to a variable first.

3. `Input()`
You can also get input from the terminal using the **input** method. In first_script.py, type the following at the bottom of the script:

```python
print('Enter your name:')
name = input()
print('Hello, ' + name)
```

![https://media.giphy.com/media/3o7buirYcmV5nSwIRW/giphy.gif](https://media.giphy.com/media/3o7buirYcmV5nSwIRW/giphy.gif)

*What did we just do?*
First we printed out a prompt. Then we assigned the input method to a variable, and then we printed out hello concatenated with the value of name.

You've now used built-in methods before for both dictionaries and lists. But they exist for data types too.

### Built-In Methods for Strings

1. `Split()`
The **split** method lets us split up a string and turn it into a list. In first_script.py, add the following:

```python
definition_of_dh = 'DH is 1) using new digital tools to do humanistic research and 2) using humanistic methods to analyze new digital tools.'
print(definition_of_dh)
print(definition_of_dh.split(''))
```

![dh definition]({{site.baseurl}}/assets/images/def_dh.png)

1. `Join()`
The **join** method lets us take a list and join all the values together.

```python
split_definition = definition_of_dh.split(' ')
joined_definition = '_'.join(split_definition)
print(joined_definition)
```

1. `Replace()`
The **replace** method lets us find a string and replace it with another string. You can also specify how many times you want to replace a string.

```python
edited_definition_of_dh = definition_of_dh.replace('tools', 'people') 
print(edited_definition_of_dh)
```

1. `Upper()` and `Lower()`
The **upper** and **lower** methods return the entire string capitalized or lowercased respectively.

```python
print(definition_of_dh.upper(), definition_of_dh.lower())
```

You can find more information about string methods here
[https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)

### Inline Commenting

Comments are especially useful--necessary!--for collaboration. Python is open source and its community of millions of coders often share in its permissive approach to intellectual property. Python as a whole is a giant collaborative project of which you are now members.

When you write particularly complicated logic or whenever you write new classes or functions (more on this later!), you should write a comment to explain yourself.

```python
edited_definition_of_dh = definition_of_dh.replace('tools', 'people') 
print(edited_definition_of_dh)
```

### Documentation

Python, as with virtually all other languages and complex codes, contains extensive documentation that covers all aspects of its use. This documentation is [easily accessible via the Internet](assets/MissionImpossible.m4v?raw=true).

[Python 3 Documentation](https://docs.python.org/3/)

Let's take a look at the specific documentation for strings:

[Python 3 Docs: Built-in Types: Strings](https://docs.python.org/3/library/stdtypes.html#string-methods)

Learning to read documentation is a critical skill for succeeding as a programmer. Happily, most of you, as graduate students, should already be literate.

### The Zen of Python

#### What's the deal with Python?

Type this into the Python interpreter:

```python
import this
```

Here's [one interpretation of Z of P](https://inventwithpython.com/blog/2018/08/17/the-zen-of-python-explained/).

Also, a DH answer: lots of DH projects are written in Python because of its simplicity and robust community and it's especially popular in areas like text analysis and machine learning.
