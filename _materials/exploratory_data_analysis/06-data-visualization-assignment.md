---
title: "Data Visualization Assignment"
permalink: /materials/exploratory-data-analysis/06-data-visualization-assignment
toc: true
---

So far we have been visualizing fairly structured data (counts mostly), but what if we wanted to explore our data from the Term Frequency-Inverse Document Frequency (TF-IDF) method?

Using the `tfidf_df` from our Introduction to Unstructured Data and Text Analysis Assignment, try and use Altair to create visualizations to answer the following questions:

1. What are the top ten *unique* TFIDF terms across our entire corpus and what score do they each have? 
2. What are the top five TFIDF terms for each volume?

*BONUS*
3. What is the relationship between top TFIDF scores and word frequencies?


Now that you are working with larger datasets one thing you might run into is an error saying `The number of rows in your dataset is greater than the maximum allowed (5000)`. To keep us from making very large graphs that eat up memory, Altair has a built-in limit in how many rows we can visualize as a default. You can read more about the default rationale here in the FAQ <https://altair-viz.github.io/user_guide/faq.html#maxrowserror-how-can-i-plot-large-datasets> but we can essentially disable that error by running this code alt.data_transformers.disable_max_rows().

```python
alt.data_transformers.disable_max_rows()
