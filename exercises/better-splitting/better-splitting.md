# Better Splitting
Define a procedure , split_string, to split a string using a given list of possible separators.

## Inputs
* source: String to split
* splitlist: String containing all characters considered separators. 

## Outputs
* List if strings that break the source string up using the splitlist characters.

## Example
```python
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print(out)
>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print(out)
>>> ['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
```

## Method
* Loop through `source`
* If character is in `splitlist`, split the string at that location using **slice**
* Add split string to result array.
* Continue until end of `source` string.
### Pseudocode
```
res = []
prev = 0
for i -> len(source):
    if char in splitlist:
        res.append(source[prev:i])
        # +1 to not include separator char 
        prev = i + 1 
return res
```

## Refine
* Loop through `source`
* If char in `splitlist` set a variable to True
* If not in splitlist
    * When split variable == True, append current char to result array. Set split variable to False. 
    * When split variable == False, concatenate contents of last word in result array with current char.
* return result arr
```Python
def split_string(source,splitlist):
    result = []
    split = True # if at split location
    for ch in source:
        if ch in splitlist:
            split = True
        else:
            if split:
                result.append(ch)
                split = False
            else:
                # Add to last word
                result[-1] = result[-1] + ch
    return result
```