---
title: "Python Cheatsheet"
permalink: /materials/intro-python-git/04-python-cheatsheet
toc: true
---

## Types and Objects

How to test for types in python. Write `type`!

```sh
>>> type(True)
<class 'bool'>
>>> type(1)
<class 'int'>
>>> dictionary = { "color":"blue", "size":9090 }
>>> type(dictionary)
<class 'dict'>
>>> atuple = ( "blue", 9090 )
>>> type(atuple)
<class 'tuple'>
>>> reindeer = ["dasher", "dancer", "prancer", "vixen", "olive"]
>>> type(reindeer)
<class 'list'>
>>> boy_bands = { "nsync", "one direction", "boyz II men" }
>>> type(boy_bands)
<class 'set'>
```

## Lists

A [Python list](https://docs.python.org/3.6/tutorial/datastructures.html) is an unordered, untyped collection of any values. The example below is storing strings, an integer, and even another list inside a list.

```python
tools = list()
tools = ['Twitter', 'Gephi', 'HathiTrust', 2019, ['MALLET']]
tools.insert(1, 'Omeka')
tools.extend([True, 'Github'])
tools.append('Python')
print(tools)
```

## Dictionary

A dictionary is a collection of key/value pairs.

```python
tools = dict()
tools = {
    'tool_1': {
        'name':'HathiTrust'
    },
    'tool_2': {
        'name': 'Gephi', 
        'founded_year': 2008
    },
}
tools['tool_1']['founded_year'] = 2008
print(tools)
```

## Set

A set is sort of like a list, except that each item is enforced to be unique. If you try to add an item that already exists in the set, no operation occurs.

```python
tools = set()
tools.add('Python')
print(tools)

tools.add('Python')
print(tools)
```

## Tuple

A tuple is like a list except that it's immutable. You can't add or remove things from it. What makes them useful is that iterating over the elements is faster than a list.

```python
tools = tuple()
tools = ('Python', 'Hathitrust', 'Gephi')
print(tools)
```

Read more here [Python 3 Docs: Built-in Types: Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
