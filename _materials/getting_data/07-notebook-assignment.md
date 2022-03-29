---
title: "Notebook Assignment"
permalink: /materials/getting-data/07-notebook-assignment
toc: true
---

## First Assignment

In class, we worked on getting the text from the *Humanist* listserv through web scraping.

The final piece of this assignment is to take the data from the plain text files and save it to a dataframe in Pandas. Going forward we'll be using this dataset to do some initial text analysis.

If you feel comfortable with assignment, feel free to go ahead and use either scripts, notebooks, or a combination of both.


1. With our existing code (available <a href="{{site.baseurl}}/assets/files/humanist_scraping.py" download> here</a>), we have access to each of the html and text from each of the emails of the first volume. Try reworking your code to work with this url `https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/` to get all the volumes without having to scrape each volume individually. Think about what data you want to get and what you don't need to keep. Do we want to keep the html? Or do we just want the text? (*hint* try googling for the`get_text()` or `.text` methods in Beautiful Soup)
2. Now that we have the data from the webpage, we need to decide what other metadata we want to include with it. What information can we get from the `url` variable? How would you get the years for each volume? (*hint* checkout the `split()` method in Python)
3. Finally we have all the data we want to store, so now we have to decide how to persist it? If we have metadata and data for each volume what data structure would be best suited? A list or a dictionary? What about a list of dictionaries? How would we add data from each volume to a variable that lived outside of the two for loops?
4. Say we got our metadata and data saved to a new variable, the final piece is to save this to a new dataframe. Read this Stack Overflow answer for how to save our variable to a dataframe [https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756](https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756). Try and find the reference to `from_records()`, `from_dict()`, and `orient=columns` in the answer, and try to save our variable to new a dataframe called `humanist_vols`.
5. Finally, so we don't have to web scrape every time, try using the following code:

```python
humanist_vols.to_csv('web_scraped_humanist_listserv.csv')
```

What does this do to our data? You can read about the `to_csv()` method here [https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv).

## Second Assignment

Let's take a deeper dive into the datasets underlying *The Pudding* "Film Dialogue" article [https://pudding.cool/2017/03/film-dialogue/](https://pudding.cool/2017/03/film-dialogue/). So far we have worked with the film scripts and now we will bringing in additional data from the *The Pudding* website.

1. Create a new jupyter notebook and read in the three datasets from the Github repository [https://github.com/matthewfdaniels/scripts/](https://github.com/matthewfdaniels/scripts/). Take a look at the documentation in the repository and discuss what you think each file contains.
2. Once you've loaded in the data into the notebook, discuss what data you think the columns contain and check if there's any missing data.
3. Try to answer the following questions:
   1. How could we tell if the amount of dialogue was increasing over time in movies? How might this influence the assessment about the breakdown of gender dialogue?
   2. How could test if there was any relationship between the film's gross value and the amount of dialogue in the film?

To answer these questions you'll need to merge, aggregate, and calculate some basic stats for these datasets.

*As a bonus, try creating a plot of visualize the answer to each of these questions.*
