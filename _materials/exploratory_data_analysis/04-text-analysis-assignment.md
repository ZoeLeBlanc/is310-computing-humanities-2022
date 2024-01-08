---
title: "Text Analysis Assignment"
permalink: /materials/exploratory-data-analysis/04-text-analysis-assignment
toc: true
---

## Main Assignment

In the Unstructured Data lesson, we learned and experimented with a few diffent approaches for analyzing textual data. For this assingment you will dig in a bit deeper.

   1. First, make sure you have the humanist listserv datasets and the code for running TF-IDF. The goal for this assignment is to try and compare words that are common in the datasets vs words that are most distinctive of the early internet era vs the web 2.0 era. To do this you will need to:
      1.  Write code to identify the top ten unique words across the entire listserv dataset.
      2.  Write code to identify the top ten words that are distinctive of these two time periods (up to you to define the exact periodization).
      3.  The final step is to create a function that will take one of these terms and plot it's frequency over time. 

Some things to consider:
- How much will you clean your datasets? Will you stem or lemmatize the words? Will you try to remove stop words or punctuation?
- What parameters will you use for TF-IDF?
- How will your organize your code and data? Would recommend creating a new notebook for this assignment.

You can either do this assignment as a script or Jupyter notebook, but would highly recommend initially working in a notebook. Once completed, push up your work to GitHub.

If you are having issues working the humanist listserv dataset, you can also use *The Pudding Film Dialogue* datasets through scraping the script text using the URLs.