---
title: "EDA In-Class Exercise"
permalink: /materials/exploratory-data-analysis/02-eda-inclass-exercise
toc: true
---

*In Breakout Groups*, you will first make sure that everyone has completed the [Notebook Assignment]({{site.baseurl}}/materials/getting-data/07-notebook-assignment) and if everyone has yet to complete the assignment, then you will collectively work together to help them answer any questions they have so that they can complete the assignment. Feel free to share code but make sure everyone understands the solution. Also make sure you discuss alternative solutions and consider how you might refactor your code!

If everyone has completed that assignment, then you can move on to the EDA In Class Assignment.

---

With the film dialogue article <https://pudding.cool/2017/03/film-dialogue/> and the gendered descriptions, we have been talking a lot about the difficulties in using gender as a categorical data. One way we can understand better *The Pudding*'s analysis is be doing some more exploratory data analysis, and specifically thinking about what sorts of patterns and outliers might be in the data.

As a group, try and answer the following questions:

1. For the three datasets, do some initial exploratory data analysis. What are the differences between the three datasets?
2. Try thinking of a question of the data you might have after looking at these datasets and also recalling our discussion of the article (I now it's been some time now but feel free to skim hypothesis as well). What might be a question you might ask with this data? Would there be some relationship between columns that you could explore further? Some columns of interest include `age`, `year`, `gross`, `title`, `words`, and `lines_of_data`. Discuss what might be an interesting pattern you might observe across these columns.
3. Now try and implement some of those ideas in code! Think about how you need to transform the datasets to answer your question (maybe merge or groupby, or maybe you need to do some calculations).
4. Finally to visualize your findings, try using the built-in `plot` method in Pandas. 
