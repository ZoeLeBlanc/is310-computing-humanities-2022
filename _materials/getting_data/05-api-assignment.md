---
title: "In-Class Notebook and API Assignment"
permalink: /materials/getting-data/05-api-assignment
toc: true
---

~~*Reminder this is an optional assignment. But recommend completing it if you plan to work with APIs in your final project.*~~

<div class="notice--info">⚡️ Rather than make this assignment optional, we will now try it out in class collectively. You **do not** need to turn this in but rather should focus on using this as an opportunity to test out your understanding.</div>

### In-Class Notebook and API Assignment

1. Create a new Jupyter Notebook called `FirstNotebook`. In your notebook, install and import any required libraries (could be `requests` or `pandas` or something else...).
2. I'm offering two options depending on whether you've worked through the Intro to APIs lesson or not. 
   - If you have yet to work through that lesson than follow the instructions from the [Introduction to APIs Quick Assignment]({{site.baseurl}}/materials/getting-data/04-intro-apis/#quick-assignment) but complete it in your Jupyter notebook. 
   - Otherwise if you have completed that quick assignment or want to push yourself, then select an API from one of the following resources:
     - <https://github.com/chanonroy/cool-apis>
     - <https://github.com/public-apis/public-apis>
     - <https://apilist.fun/>
     - One of my personal favorites is SWAPI (the Star Wars API) <https://swapi.dev/documentation>.
   After you pick an API, read through the documentation and find a way to get data from it. This could involve using requests to query the API directly or working with a code library and using the correct method.
     - For APIs that require authentication, make sure you authenticate and store your API keys locally.
   Once you have the data, subset the data so that you only have one item, print out the entirety of that item in your Jupyter notebook, and then store it either as a JSON file or as a CSV file (choice is yours) with the filename that includes the API you selected.

Finish both quickly? Feel free to jump back into the [Introduction to Notebooks]({{site.baseurl}}/materials/getting-data/06-intro-notebooks) lesson and complete the [notebook assignment]({{site.basurel}}/materials/getting-data/07-notebook-assignment).

### Original Optional Assignment

1. Create a new script called `first_apis.py`. Now select an API from one of the following resources:
   - <https://github.com/chanonroy/cool-apis>
   - <https://github.com/public-apis/public-apis>
   - <https://apilist.fun/>
   - One of my personal favorites is SWAPI (the Star Wars API) <https://swapi.dev/documentation>.

2. After you pick an API, read through the documentation and find a way to get data from it. This could involve using requests to query the API directly or working with a code library and using the correct method. 
   - For APIs that require authentication, make sure you authenticate and store your API keys locally.

3. Once you have the data, subset the data so that you only have one item, print out the entirety of that item in your script, and then store it either as a JSON file or as a CSV file (choice is yours) with the filename that includes the API you selected.

4. Push both your script and the data to your Github repository.
