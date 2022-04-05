---
title: "Introduction to Unstructured Data"
permalink: /materials/exploratory-data-analysis/03-intro-unstructured-data
toc: true
---

## What is Unstructured Data?

When working with data, you'll often come across the terms "structured" and "unstructured" data. There are lots of definitions online, like this graph below:

![structured vs unstructured](http://intellspot.com/wp-content/uploads/2020/04/Structured-vs-unstructured-data-an-infographic-1024x724.png)

This graph is technically correct, but it is also a bit confusing when you think about it (even highly organized data can be difficult to analyze for example and why can't things like email be analyzed in spreadsheets?).

Let's compare our two datasets that we have been working with so far: the [Film Dialogue](https://pudding.cool/2017/03/film-dialogue/) dataset and the Humanist Listserv dataset.

In our Film Dialogue datasets, we have technically four separate spreadsheets with the following columns:

- `Public Script Sources - public_scripts.csv` with:
  
|`imdb_id` | `script_id` | `title` | `year` | `gross_ia` | `link` |
|---------|-------------|---------|-------|----------|-------|
| tt0019777 |        4031 | The Cocoanuts |   1929 |        nan | <http://www.pages.drexel.edu/~ina22/splaylib/Screenplay-Cocoanuts,_The.pdf>|

- `character_list5.csv` with :

|`script_id` | `imdb_character_name` | `words` | `gender` | `age` | 
|---------|-------------|---------|-------|----------|
|   280 | betty |     311 | f        |    35 |

- `character_mapping.csv` with:
   
|`script_id` | `imdb_id` | `character_from_script` | `closest_character_name_from_imdb_match` | `closest_imdb_character_id` |
|---------|-------------|---------|-------|----------|
|   1 | tt0147800 | bianca | bianca stratford | nm0646351 |

- `meta_data7.csv` with:

|`script_id` | `imdb_id` | `title` | `year` | `gross` | `lines_data` |
|---------|-------------|---------|-------|----------|-------|
|   1534 | tt1022603 | (500) Days of Summer |   2009 |      37 | 743544525677477444334257777565774443444456445674543367553452777734237544553444343334444444467441433777777777777776634344344434244343433435535624644435776576434333377775756764434344466346764533566544444777533356445543543343334444535476332345777777777777776 |

In our Intro to EDA notebook, we discussed how some of the values in these spreadsheets are **categorical** values (like `gender` as a **nominal** category -- that is discrete unordered categories) and how some are **numerical** values (like `gross` or `lines_data`). And finally how some are a bit in between, like `year` which is technically represented as a number and we could treat it as either a **continuous** or **discrete** value, or we could treat it as a categorical value that is **ordinal** (i.e. is a category with an implied order). 

The big thing to takeaway from looking at these datasets though is that all these values are structured. We do not need to do any processes to turn these values into data to analyze. We might group them, we might filter them, we might fill in missing values, and we can plot them -- but essentially this is a dataset ready to be analyzed.

Let's compare that to our Humanist listserv dataset.

With `web_scraped_humanist_listserv.csv` we have:

| `dates` | `text` | `url` |
|---------|--------|-------|
| 1987-1988 | From: MCCARTY@UTOREPAS\nSubject: \nDate: 12 Ma... | <https://humanist.kdl.kcl.ac.uk/Archives/Converted_Text/humanist.1987-1988.txt>|

I've truncated the text file column for visual clarity, but overall this is a much less complex dataset than the Film Dialogue dataset. We could leave the dataset as is and treat it as structured or semi-structured data but our analysis would likely be very limited since we have no numeric data. 

Instead to make our Humanist Listserv dataset into something like the Film Dialogue datasets, we need to go through a process of curating and cleaning the data from unstructured to structured data, similar to this graph below:

![data humanities knowledge continum](https://i.pinimg.com/736x/b0/04/b5/b004b543748ba1350c5d66c16c678607.jpg)

It's worth noting here that this structured vs unstructured divide is very porous and ill defined, and mostly has a lot to do with your goals and your data.

### Structuring our Textual Data

So let's try adding some structure to our Humanist Listserv dataset. Let's start a new notebook called `HumanistListservEDA.ipynb` and import our libraries and data.

Now we need to start thinking about the types of data that we have and exploratory data analysis we might want to undertake.

First we can check our data types:

```python
# Check the data types of our columns
humanist_vols.dtypes
```

We should see the following output:

```shell
dates    object
text     object
url      object
dtype: object
```

In [Intro to Notebooks]({{site.baseurl}}/materials/getting-data/06-intro-notebooks), we learned that Pandas treats `string` data as `object` data (also all mixed numeric or non-numeric values). So now we know that to work with our data we will need to dig into Pandas `string` methods. An in-depth discussion of these methods are available on the Pandas documentation website <https://pandas.pydata.org/docs/user_guide/text.html>, but I've also summarized many of the more popular methods below in this table:

| Pandas String Method | Explanation |
|---------------------|-------------|
| `df[‘column_name’].str.lower()` | lowercase all the values in a column |
| `df[‘column_name’].str.upper()` | uppercase all the values in a column |
| `df[‘column_name’].str.replace(‘old_string’, ‘new_string’)` | replace all instances of ‘old_string’ with ‘new_string’ in a column |
| `df[‘column_name’].str.split(‘delimiter’)` | split a column by ‘delimiter’ like a comma or period, or really anything |
| `df[‘column_name’].str.strip()` | remove leading and trailing whitespace from a column |
| `df[‘column_name’].str.len()` | count the number of characters in a column |
| `df[‘column_name’].str.contains(‘pattern’)` | check if a column contains a particular pattern |
| `df[‘column_name’].str.startswith(‘pattern’)` | check if a column starts with a particular pattern |
| `df[‘column_name’].str.endswith(‘pattern’)` | check if a column ends with a particular pattern |
| `df[‘column_name’].str.find(‘pattern’)` | find the first occurrence of a particular pattern in a column |
| `df[‘column_name’].str.findall(‘pattern’)` | find all occurrences of a particular pattern in a column |
| `df[‘column_name’].str.count(‘pattern’)` | count the number of occurrences of a particular pattern in a column |
| `df[‘column_name’].str.extract(‘pattern’)` | extract the first occurrence of a particular pattern in a column |
| `df[‘column_name’].str.extractall(‘pattern’)` | extract all occurrences of a particular pattern in a column |
| `df[‘column_name’].str.join(list)` |  join a list of strings with a delimiter |

This list is not exhaustive, but it's a good starting point and shows that there are a number of approaches we could take. 

Let's start off with trying to explore the size of each volume over time. First, we need to split our `dates` column into a `year_start` and `year_end` columns.

```python
# Split the dates column into year_start and year_end 
humanist_vols['year_start'] = humanist_vols['dates'].str???
humanist_vols['year_end'] = humanist_vols['dates'].str???
```

Now that we have our years, we need to get the size of each volume. We can do this by using the `count` method and thinking of a pattern that would represent size of the volume (maybe the frequency of new lines `\n` or `FROM` ?).

```python
# Count the number of characters in each volume
humanist_vols['volume_size'] = humanist_vols['text'].str???
```

Final step is to plot our data to explore the pattern we are interested in! 

```python
# Plot the data
humanist_vols.plot(x='year_start', y='volume_size', kind='bar')
```

We should produce a graph that looks like this:

![humanist size]({{site.baseurl}}/assets/images/humanist_size.png)

## What is Text Analysis?

One of the main ways we can structure our Humanist listserv data is by undertaking something called *text analysis*. This is a very broad term for a whole set of practices and overlapping disciplines and fields, some of which are shown in this figure below:

![text analysis](https://miro.medium.com/max/1200/0*ewkxRItArykG27dU.png)

But again this figure has its limits. For example, data mining is something that Library & Information Sciences undertakes, and databases are used across these domains.

Rather than trying to define text analysis as a whole, I find a more helpful distinction is talking about Information Extraction vs Information Retrieval. 

**Information Retrieval (IR):**

![information retrieval](https://i.stack.imgur.com/0GsKI.gif)

- Goal of finding relevant documents for user’s needs/queries (eg. Google)
- Often used for text classification of documents
- Can be done without “understanding” syntax and treating documents as “bag of words”

**Information Extraction (IE)**

![information extraction](https://i.stack.imgur.com/0GsKI.gif)

- Goal of extracting specific features from documents
- Focused on linguistic analysis of textual features
- Requires both syntactic and semantic analysis

Today we will be focusing on the first category of these two categories, Information Retrieval.

### What is Information Retrieval?

According to[Wikipedia](https://en.wikipedia.org/wiki/Information_retrieval), Information Retrieval (or IR) was first theorized in the 1940s:

![origins IR]({{site.baseurl}}/assets/images/origins_ir.png)

### Text Analysis with Python

In Python, there exists a few libraries specifically designed to work with text data.

- NLTK [https://www.nltk.org/](https://www.nltk.org/)

- SPACY [https://spacy.io/](https://spacy.io/)

- SCIKIT-LEARN [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)

Each of these libraries has its own history, and some of what they provide overlaps. Here's a helpful chart outlining some of their pros and cons.

![comparison](https://activewizards.com/content/blog/Comparison_of_Python_NLP_libraries/nlp-librares-python-prs-and-cons01.png)

Ultimately, which library you choose to use depends on what you want to do with your data, but there's some general principles for text analysis that you should consider regardless of method.

### Word Counts and Zipf's Law

The library NLTK has a helpful built in Class called `FreqDist` that takes a list of words and outputs their frequency in a corpus [http://www.nltk.org/api/nltk.html?highlight=freqdist](http://www.nltk.org/api/nltk.html?highlight=freqdist)

Let's try it out with a subset of our data. (Remember to install `nltk`).

```python
from nltk import word_tokenize
from nltk import FreqDist

tokens = FreqDist(sum(humanist_vols[0:2]['text'].map(word_tokenize), []))
tokens.plot(30)
```

We should get a graph that looks like this:
![counts](images/counts.png).

In this graph, if we had used all the words we would see this trend continue, like in the graph below.

![zipf](https://miro.medium.com/max/6072/1*GTpckiHyFLe04pUMeYDYOg.png)

This is “Zipf’s law:” the phenomenon means that the most common word is twice as common as the second most common word, three times as common as the third most common word, four times as common as the fourth most common word, and so forth.

It is named after the linguist George Zipf, who first found the phenomenon while laboriously counting occurrences of individual words in Joyce’s Ulysses in 1935.

This is a core textual phenomenon, and one you must constantly keep in mind: common words are very common indeed, and logarithmic scales are more often appropriate for plotting than linear ones. This pattern results from many dynamic systems where the “rich get richer,” which characterizes all sorts of systems in the humanities.

[https://tedunderwood.com/2013/02/20/wordcounts-are-amazing/](https://tedunderwood.com/2013/02/20/wordcounts-are-amazing/)
![wordcounts](images/wordcounts.png)

### Tokenization

In the field of corpus linguistics, the term “word” is generally dispensed with as too abstract in favor of the idea of a “token” or “type.” Breaking a piece of text into words is thus called “tokenization.”

There are, in fact, at least 7 different choices you can make in a typical tokenization process.

- Should words be lowercased?
- Should punctuation be removed?
- Should numbers be replaced by some placeholder?
- Should words be stemmed (also called lemmatization).
- Should bigrams or other multi-word phrase be used instead of or in addition to single word phrases?
- Should stopwords (the most common words) be removed?
- Should rare words be removed?
Any of these can be combined: there at least a hundred common ways to tokenize even the simplest dataset.

### Lemmatizing/Stemming

![stemming](https://miro.medium.com/max/1400/1*-MTbZK9ha3Kp1Z50o79Tzg.png)

![lemma](https://devopedia.org/images/article/227/6785.1570815200.png)

### Bag of Words

![bag](https://qph.fs.quoracdn.net/main-qimg-4934f0958e121d33717f848230ef664a)



In *Introduction to Cultural Analytics*, Melanie Walsh and Quinn Dombrowski discuss text mining beyond English. They write:

![two texts]({{site.baseurl}}/assets/images/two_types_text_analysis.png)
