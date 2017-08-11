# Inverted Index
The goal of an index is to map a keyword and where that keyword is found.

Inverted Index stores a list of occurrences of each atomic search criterion, typically in the form of a hash table or binary tree.
```
[[<keyword1>, [<url1,1>, <url2,1>]]
[<keyword2>, [<url2,1>]...]
```

## Problem
Define a procedure, **add_to_index**, that takes *three inputs*:
* an index - `[[<keyword1>, [<url1,1>, <url2,1>]]`
* a keyword string - 'udacity'
* a url string - 'https://udacity.com'

If the keyword is already in the index, add the url to the list of urls associated with that keyword.

If the keyword is **not** in the index, add en entry to the index: `[keyword,[url]]`

### Example
```
index = []
add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'programming', 'https://stackoverflow.com')
```

The index is initially empty. After the two lines above, the empty list will contain **two lists** beginning with the keywords *udacity* and *computing*.

Adding another entry with an existing keyword:
```
add_to_index(index, 'udacity', 'http://npr.org')
```
Since **udacity** is already in the index, the url `'http://nmr.org'` is appended to the existing url list for the keyword udacity.

![](images/2017-08-11-13-46-48.png)