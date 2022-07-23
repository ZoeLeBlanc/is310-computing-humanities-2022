---
title: "Python Advanced Assignments"
permalink: /materials/advanced-python/04-python-assignment
toc: true
---

Working in pairs or small groups, one person types and the other(s) tell them what to write.

## Assignment 1

This is the first few lines from Project Gutenberg version of Jane Austen, which you can find [here](https://www.gutenberg.org/files/1342/1342-0.txt).

```python
"The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 ***START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE*** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
```

We want to use this text, but we need to get rid of some of the metadata at the beginning and we want to replace some of the data. Create a script called `jane_austen_data_munging.py`

1. First save this text into a variable called `jane`

2. Figure out how to get rid of everything before `Produced by Anonymous Volunteers` and save everything after in a variable called `jane_cleaned` (**hint: check out the string method [split()](https://www.w3schools.com/python/ref_string_split.asp), it splits strings on certain characters and returns a list *** )

3. If you haven't already, replace all instances of `man` with `person`, and `wife` with `parther` in `jane_cleaned` (**hint: check out the string method [replace()](https://www.w3schools.com/python/ref_string_replace.asp)**)

4. Change your script so that you can give an input, and replace any word in the text with any other word. Output the changed text.

## Assignment 2

Using the DH Tools data from last week, rewrite your code so that we could add a few more entries in a new script called `dh_tools.py`.

1. Download and save the [`tools_dh_proceedings.csv`]({{site.baseurl}}/assets/files/tools_dh_proceedings.csv) file.
   
2. Read in the csv file using the Python [`csv` module](https://docs.python.org/3/library/csv.html). This is a little trickier than working with text files because the csv file is a comma-separated value file. For more information on how to do that check out our [introduction to file formats]({{site.baseurl}}/materials/getting-data/03-file-formats) and this tutorial <https://realpython.com/python-csv/>.

3. Now try and recreate the functionality from our first script ~~but instead of just printing everything out try and get the top ten tools based on the 2019 ratings~~. Try printing out again the 2015, 2019, and overall counts for each tool.

4. Now let's try reworking your code into a function. 
   - First step is write a function that takes your DH tools data and a tool name.
   - Then in your function print out *only* the data for that particular tool. 

**BONUS** Using the built-in input method, let a user input a tool name from the terminal, and then have your function print out the data for that tool.

~~5. Finally, create a secondary function to input any year and return the top tool.~~

Once you're finished, upload your scripts to your Github assignments folder or repository, and post a link in our `#coding-assignments` channel on Discord. 
