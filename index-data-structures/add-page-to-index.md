# Add Page to Index
Define a procedure, **add_page_to_index** that will update the index to include all of the word occurences found in the page content by adding the url to the word's associated url list.

## Inputs
* index
* url (string)
* content (string)

## Example
```
index = []
add_page_to_index(index, 'fake.test', "This is a test")
print(index)
>>> [['This', ['fake.test']], ['is', ['fake.test']],['a', ['fake.test']],
['test', ['fake.test']]]

print index[0]
>>> ['This', ['fake.test']]

print index[1]
>>> ['is', ['fake.test']]

```

## Method
* Parse content string into list of individual keywords.
* Use add_to_index() function created previously for each keyword -> passing in keyword and url.
