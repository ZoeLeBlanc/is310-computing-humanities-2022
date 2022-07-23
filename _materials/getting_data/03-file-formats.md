---
title: "File Formats"
permalink: /materials/getting-data/03-file-formats
toc: true
---

<div class="notice--info">⚡️ This lesson has been adapted from Shane Lin's CodeLab syllabus <a href="https://github.com/scholarslab/CodeLab">https://github.com/scholarslab/CodeLab</a></div>

We covered some basic file input and output in Python previously. It's pretty easy to work with text data, either all at once or line by line.

To review, we can read some text from a file like so:

```python
infile = open('file.txt', "r"):
text = infile.read()
infile.close()
```

or, equivalently, using the with-open-as idiom:

```python
with open('file.txt', "r") as infile:
    text = infile.read()
```

and we can write back to files just as easily:

```python
outfile = open('file.txt', "w"):
outfile.write("Hello World!")
outfile.close()
```

(If you need a refresher, we learned all of this back in [Advanced Python Part 2]({{site.baseurl}}/materials/advanced-python/03-complex-python#file-input-and-output))

But while we've worked with simple text and numerical data like strings and ints plenty, we've also used lists and dictionaries and more structured data too. How do we read and write those more complicated kinds of data?

Let's revisit the way that we read in numbers. Recall that when we use the `read()` method on a file object like we did above, the data that we get back is a string. So, if we had a file named file.text that just contained the number `12345`, we'll get back the string "12345" rather than the integer 12345.

```python
with open('file.txt', "r") as infile:
    text = infile.read()
    text += 43210 #this line results in "TypeError: must be str, not int"
```

The "12345" in the text file is, after all, text. Underneath it all, it's being represented by a text encoding, which means that if you look under the hood, "12345" isn't actually 12345. These days, this kind of text is usually UTF-8/ASCII encoded numbers, which means "12345" is actually 049 050 051 052 053. To turn the text "12345" into the number 12345 in Python, we have to explicitly tell Python to make this conversion.

```python
with open('file.txt', "r") as infile:
    text = infile.read()
    number = int(text)
    number += 43210 #this works just fine now
```

Here, we're calling the integer constructor method that takes in a string argument and builds us a new integer object based on that string.

I bring this up to suggest that there's difference between the static text representation of an object and the "live" Python objects that live in computer memory and can be manipulated. Python objects are useful because we can easily manipulate them, but they don't persist beyond the lifespan of a program. Static files persist data, but have to be read and interpreted explicitly in the way that we want them to be.

## Let's talk about Data Formats

So, strings and even numbers are simple enough. How do we represent, say, a list of things in a file?

A really simple way to do this is to just write them out as a list, separated by some delimiter. Following English convention, let's use commas. An easy way to do this in Python is to use the string method `join()`, which is kind of like a reverse split. It lets you join together a list of strings with a delimiter (you can also just mush together the list of strings if you call it on an empty string).

```python
dh_tools1 = ["Gephi", "HathiTrust", "BeautifulSoup"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dh_tools1))
with open('file.txt', "r") as infile:
    text = infile.read()
dh_tools2 = text.split(",")
print(dh_tools1 == dh_tools2)
```

So, we can see that (hopefully) the two lists are the same. This is easy enough for simple data, but we can probably see that there are some complications here...

```python
dh_tools1 = ["Gephi, a tool for network analysis", "HathiTrust, the Digital Library", "BeautifulSoup, A Python Library"]
with open('file.txt', "w") as outfile:
    outfile.write(",".join(dh_tools1))
with open('file.txt', "r") as infile:
    text = infile.read()
dh_tools2 = text.split(",")
print(dh_tools1 == dh_tools2)
```

So, there's one basic problem with using text to store structured text. Whatever delimiters or special characters we use to indicate the structure of the data can also exist in the data itself. ASCII, the archaic way of encoding text, solved this by setting aside special non-text characters. There were characters for things like "Start of Heading", "End of Transmission", "Acknowledgement", and even "Bell" to get a computer operator's attention. These days, that method is hopelessly outmoded, not just because we want to be have more flexibility in the ways that we define our structures.

So how do we get by this? We can wrap individual elements in quotes and that works well enough if we don't also use quotes. We can also use escape characters to tell Python when we do and don't mean business. An escape character is just a character that means "interpret the next thing as text, without any special meaning." Although sometimes it means "interpret the next thing as a special thing and not just as regular text." Commonly, many systems use the backslash (`\`) as an escape character. This works when we define a string in Python, for example:

```python
 text = "here are some quotation marks inside of a string: \"\'\'\""
 print(text)
```

But all these rules are starting to add up. It's getting kind of complicated. We don't want to spend our time writing out the special logic to distinguish between real quotations marks and commas and fake ones. And what if we didn't think of some non-obvious, uncommon edge case? Happily, this whole exercise is a pretty common problem and there are a few standard ways to do it.

We can impart super-textual meaning to text data (like the structure of a list) using data formats, which are standard ways to write out and read data, that typically have standard software tools to accomplish those tasks.

## CSV

One of the simplest data formats is CSV, which stands for, simply enough, Comma Separated Values. Strangely enough, it doesn't actually have to be commas that do the separating. Typically, we can choose our own delimiter. CSVs are used for tabular data and is a commonly used to exchange data between different spreadsheet applications or to produce data that is easily ingested by those applications. In a CSV, each column entry is separated by the delimiter and each new line contains a new row.

Let's try out a simple example with some familiar data.

```python
hathi_trust = ["HathiTrust",2008,"Digital Library"]
gephi = ["Gephi", 2008, "Network Analysis"]
beautifulsoup = ["BeautifulSoup", 2004, "Python Library for Web Scraping"]
tools = [hathitrust, gephi, beautifulsoup]

with open('dh_tools.csv', "w") as outfile:
    outfile.write(",".join(["Tool","Year Released","Type of Tool"]))
    for tool in tools:
        outfile.write("\n"+",".join(tool))
```

If you want, you can import that into your preferred spreadsheet application to to see what comes out.

But this still leaves us with the problem of how to handle tricky data. Since CSV is so widely used, there is actually a [built-in Python module](https://docs.python.org/3/library/csv.html) to handle it. 

We just create a file object with `open()` like before, but we pass that file object into a special CSV writer.

Let's try it out.

```python
import csv

hathi_trust = ["HathiTrust",2008,"Digital Library"]
gephi = ["Gephi", 2008, "Network Analysis"]
beautifulsoup = ["BeautifulSoup", 2004, "Python Library for Web Scraping"]
tools = [hathitrust, gephi, beautifulsoup]

with open('dh_tools.csv', "w", newline='') as csvfile:
    toolwriter = csv.writer(csvfile, delimiter=',')
    toolwriter.writerow(["Tool","Year Released","Type of Tool"])
    for tool in tools:
        toolwriter.writerow(tool)
```

Which produces the output csv file...

```csv
Tool,Year Released,Type of Tool
"HathiTrust",2008,"Digital Library"
"Gephi",2008,"Network Analysis"
"BeautifulSoup",2004,"Python Library for Web Scraping"
```

Easy!

Actually, this is still a little too much work. We have to manually define headers and make sure that everything is in the right order. What if we didn't even have to do that?

If start with a dictionary instead of a list, we have a way to associate values with keys rather than just depending on their indices. We can use the `DictWriter` class inside of the csv module to automatically take care of things for us.

```python
import csv

hathitrust = {"tool_name":"HathiTrust","year_released":2008,"type_of_tool":"Digital Library"}
gephi = {"tool_name": "Maple", "year_released":2008, "type_of_tool": "Network Analysis"}
beautifulsoup = {"tool_name": "Bofur", "year_released":2004, "type_of_tool": "Python Library for Web Scraping"}

with open('dh_tools.csv', 'w', newline='') as csvfile:
    fieldnames = hathitrust.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(hathitrust)
    writer.writerow(gephi)
    writer.writerow(beautifulsoup)
```

This produces the same kind of CSV file. Note that the field names are consistent, so I just used the keys for `hathitrust`. We'd have to do this a bit differently if the data wasn't structured homogeneously.

To read CSV files, we can use analogous Reader and DictReader objects in the csv module:

```python
import csv

with open('dh_tools.csv', newline='') as csvfile:
    toolreader = csv.DictReader(csvfile)
    for tool in toolreader:
        print(tool["tool_name"],"and",tool["year_released"])
```

## JSON

CSV is good for tabular data, but not great to encapsulate data with more complex relationships. CSVs don't really support variable-length lists of things inside of rows. We can store our own format to store lists within a single CSV element, but that just puts us back at step one. And, I cannot emphasize this enough, storing different arbitrary text data formats inside of each other is a *real bad idea*. Don't do it. Oh my god, no, just don't do it.

One popular, good way to do this is JSON. Sometimes it's pronounced "Jay Song", but it's really "Jason". JSON stands for "Javascript Object Notation" and was originally designed to allow websites to pass data back and forth between the browser and the server. But it's become a really popular generic format for all sorts of things and all sorts of languages.

We don't have to go too much into the particular details of how JSON is structured. It's enough to just glance at what it looks like. Here's an example:

```json
[
  {
    "tool_name": "HathiTrust",
    "year_released": 2008,
    "type_of_tool": "Digital Library",
    "user_communities": [
      "scholars",
      "cultural heritage practionners",
      "libraries",
      "data scientists"
    ]
  },
  {
    "tool_name": "Gephi",
    "year_released": 2008,
    "type_of_tool": "Network Analysis",
    "user_communities": [
      "humanists",
      "network scientists",
      "data visualization experts"
    ]
  },
  {
    "tool_name": "BeauitfulSoup",
    "year_released": 2004,
    "type_of_tool": "Python Library for Web Scraping",
    "user_communities": [
      "python developers",
      "digital humanists",
      "data scientists"
    ]
  }
]
```

Happily, there is also an easy to use [JSON module for Python](https://docs.python.org/3/library/json.html).

One of the most useful mechanisms it provides is the ability to "dump" and "load" arbitrary built-in Python data structures into and out of JSON. It makes it super easy to throw a complex python object into a file and get it back out again.

There are `dump` and `load` methods, which write and read directly to files, but also `dumps` and `loads` methods which write and read to a string object. I like using the latter because it makes it easier to check them during debugging.

```python
import json

hathitrust = {"tool_name":"HathiTrust","year_released":2008,"type_of_tool":"Digital Library"}
gephi = {"tool_name": "Maple", "year_released":2008, "type_of_tool": "Network Analysis"}
beautifulsoup = {"tool_name": "Bofur", "year_released":2004, "type_of_tool": "Python Library for Web Scraping"}
dh_tools = [hathitrust, gephi, beautifulsoup]

with open('dh_tools.json', mode="w") as jsonfile:
    jsonfile.write(json.dumps(dh_tools))

with open('dh_tools.json', mode="r") as jsonfile:
    dh_tools_load = json.loads(jsonfile.read())
    for tool in dh_tools_load:
        print(tool["tool_name"],"and",tool["year_released"])
```

## Other Data Formats

There are a ton of other text data formats. The other big one is SGML/XML/HTML, which are structurally similar and related. HTML is, of course, the language that websites are written in. We'll revisit that in the future when we talk about building websites.

These are all different from binary data formats like the jpg and gif images but that's a whole different kettle of fish.
