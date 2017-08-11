# Frequency Analysis
To analyze encrypted messages, to find out information about the possible 
algorithm or even language of the clear text message, one could perform 
frequency analysis. This process could be described as simply counting 
the number of times a certain symbol occurs in the given text. 
For example:
For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.

## Inputs
*  String, lowercase letters a-z

## Outputs
* List of normalized frequency for each letter
    * Normalized frequency = frequency/total characters in input

## Human Method
Go through input letter by letter. Keep count/tally of occurences of each letter.
Normalize frequency of each after.

## Refined
* letter_count array array length 26 to represent each letter a-z.
* Get (ASCII value **-97**) for each char in input to get position in letter_count array
    * Lowercase ASCII starts at 97
* Increment value at position in letter_count
* Divide each element in letter_count by len(input), return.
    * List comprehension
