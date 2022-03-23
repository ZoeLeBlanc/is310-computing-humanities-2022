---
title: "Web Scraping Assignment"
permalink: /materials/getting-data/02-webscraping-assignment
toc: true
---

## ~~First~~ In-Class Assignment

On Tuesday we finished class by trying out the requests library with beautifulsoup to do webscraping. Today in breakout groups, we will be working on trying out web scraping of the humanist listserv.

In your group, one person should share screen and create a new file called `humanist_scraping.py`.

1. First step is to get the data from the main listserv page using `requests` and `beautifulsoup`. Feel free to use some of our existing code from the lesson for this.
2. Next, try and capture the links to the Volumes of the listerv. Feel free to save that in whatever data structure you prefer, but the goal should be to get both the links and the associated Volume text. 
3. Finally, try and get at least two of the volumes pages (i.e. pass those links to the `requests` library and get the data from the pages). And then also get the text from those pages (sort of web scraping inception if you will).

If you finish this quickly, feel free to try:
4. Saving each volume's text into an associated folder and text file.
5. Push up your code and data to the person who is coding Github repository (Be sure to add all your names as a comment at the top of the script).

## SPRING BREAK Homework Assignment

Building from Melanie Walsh's example in <https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/02-Web-Scraping-Part1.html#why-do-we-need-to-scrape-at-all>, try using `requests` and `BeautifulSoup` to get the data from the Pudding Movie Dialogue article we read.

1. ~~You'll need to go to the Cornell Movie Corpus website to get the data for the Pudding Movie Dialogue article <http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html>. Once you download and unzip that folder you should see two files in it: `README.txt` and `raw_script_urls.txt`.~~

Unfortunately this original file now contains redirects to sites that are nsfw so I've recreated the text file to exclude those URLs. You can download the file by clicking <a href="{{site.baseurl}}/assets/files/updated_raw_text_script_urls.txt" download>here</a>. Be aware that some of these sites will have 400 errors so you may need to test for the response status code.

~~- First, read how the data is organized in the README.txt file.~~
- Then using that as a guideline read in the raw_script_urls.txt file and save the URLs for the Pudding Movie Dialogue article to a variable.

1. Now that you have the URL for the Pudding Movie Dialogue article, you can use `requests` to get the text of each of the scripts. Write code that will loop through the script urls and save the only the script's text to a file.
2. Push up your code and data to Github once you've completed it.

*Have any questions or issues? Either post it to Discord or message the instructor.*
