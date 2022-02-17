---
title: "Web Scraping Assignment"
permalink: /materials/getting-data/02-webscraping-assignment
toc: true
---

## First Assignment

1. Finish our first exercise by figuring out to scrape the text from at least five of the volumes on the Humanist Listserv.
2. Save each volume's text in a file.
3. Push up your code and data to your Github repository.

## Second Assignment

Building from Melanie Walsh's example in <https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/02-Web-Scraping-Part1.html#why-do-we-need-to-scrape-at-all>, try using `requests` and `BeautifulSoup` to get the data from the Pudding Movie Dialogue article we read.

1. You'll need to go to the Cornell Movie Corpus website to get the data for the Pudding Movie Dialogue article <http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html>. Once you download and unzip that folder you should see two files in it: `README.txt` and `raw_script_urls.txt`.

- First, read how the data is organized in the README.txt file.
- Then using that as a guideline read in the raw_script_urls.txt file and save the URLs for the Pudding Movie Dialogue article to a variable.

2. Now that you have the URL for the Pudding Movie Dialogue article, you can use `requests` to get the text of each of the scripts. Write code that will loop through the script urls and save the only the script's text to a file.
3. Push up your code and data to Github once you've completed it.

*Have any questions or issues? Either post it to Discord or message the instructor.*
