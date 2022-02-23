---
title: "Advanced Python In-Class Exercise"
permalink: /materials/advanced-python/02-inclass-exercise
toc: true
---

In class, we discussed different forms of control flow in Python. We also looked at how to use functions and how to use loops, as well as conditionals.

To test out our understanding, we're going to update our first script to try out these concepts.

Here's some sample code from Advanced Python part 1:

```python
tools = {
    'Python': {
        '2015': 9,
        '2016': 22,
        '2017': 27,
        '2018': 32,
        '2019': 35,
    },
    'JavaScript': {
        '2015': 8,
        '2016': 18,
        '2017': 12,
        '2018': 6,
        '2019': 15,
    },
    'Twitter': {
        '2015': 10,
        '2016': 18,
        '2017': 26,
        '2018': 16,
        '2019': 12,
    },
    'GitHub': {
        '2015': 2,
        '2016': 6,
        '2017': 17,
        '2018': 5,
        '2019': 10,
    },
    'Gephi': {
        '2015': 11,
        '2016': 16,
        '2017': 14,
        '2018': 10,
        '2019': 9,
    },
    'GeoNames': {
        '2015': 2,
        '2016': 4,
        '2017': 3,
        '2018': 1,
        '2019': 8,
    },
    'Transkribus': {
        '2015': 0,
        '2016': 1,
        '2017': 2,
        '2018': 1,
        '2019': 8,
    },
    'Excel': {
        '2015': 5,
        '2016': 9,
        '2017': 3,
        '2018': 6,
        '2019': 7,
    },
    'MySQL': {
        '2015': 0,
        '2016': 6,
        '2017': 9,
        '2018': 5,
        '2019': 7,
    },
}

for key, value in tools.items():
    print('key', key)
    print('value', value)
```

1. Try altering the for loop above to print out the overall total for each tool.
2. Try altering the for loop above to only print out values for 2015 or 2019.
3. Try turning the for loop into a function that takes our `tools` dictionary and then a year as input and returns the total for that year for each tool.