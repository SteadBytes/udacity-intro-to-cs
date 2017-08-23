# Family Trees
## Recursive Definition of Ancestors
**Ancestor** -> Parent

**Ancestor** -> Parent of **Ancestor**

The Parent is an **Ancestor** and so is the Parent of the Parent of the **Ancestor** and so on.

## Problem
Define a procedure, `ancestors(genealogy, person)`, that takes as its first input
a Dictionary representing parent relationships (example below), and as its second input the name of a
person. It should return a list giving all the known ancestors of the input
person (this should be the empty list if there are none). The order of the list
does not matter and duplicates will be ignored.

## Inputs
* genealogy = dictionary representing parent relationships.
    ```python
    ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }
    ```
* person = string, name of person to find ancestors of.

## Outputs
* List of strings representing all the known ancestors of the input person.
* EMpty list if no ancestors found.

## Method
* Check if genealogy[person]:
    * Base case
    * If person doesn't exist return None
* Find genealogy[person]
* Add contents to result list
* Call ancestor() on each person in list
