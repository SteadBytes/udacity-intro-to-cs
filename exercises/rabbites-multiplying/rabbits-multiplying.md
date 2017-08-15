# Rabbits Multiplying
A more realistic model of [Fibonacci's Rabbit's](http://www.oxfordmathcenter.com/drupal7/node/487) model would assume that rabbits **are not immortal**. For this exercise, assume some rabbits die from **month 6** onward.

## Rabbit Population Model
### Base Cases:
* `rabbits(1) = 1`
    * There is one pair of immature rabbits in Month 1
* `rabbits(2) = 1`
    * There is one pair of mature rabbits in Month 2
### For months 3-5:
* `rabbits(n) = rabbits(n - 1) + rabbits(n - 2)`
* Same as Fibonacci model as no rabbits dying yet.
### For months > 5:
* `rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)`
* All the rabbits that are over 5 months old die along with a few others
so that the number that die is equal to the number alive 5 months ago.
* Before dying, the bunnies reproduce.


This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...

## Problem
Define a procedure, *rabbits*, to calculate the population of rabbits after **n** years using the model above.

### Input
* n - Int, number of months to calculate population for.

### Output
* Returns the population of rabbits after **n** months, i.e. that value of the n<sup>th</sup> number in the rabbit sequence.

### Example
```python
print rabbits(10)
#>>> 35
```

## Method
**Recursive** solution
* Bases cases:
    * `rabbits(1) = 1`
        * There is one pair of immature rabbits in Month 1
    * `rabbits(2) = 1`
        * There is one pair of mature rabbits in Month 2
    * `n < 0`
        * return 0, used when n < 5 so rabbits(n-5) just returns 0.
* When n > 2:
    * `return rabbits(n - 1) + rabbits(n - 2) - rabbits(n-5)`


### Pseudocode
```python
def rabbits(n):
    if n < 0:
    # when n < 5, (n-5) is negative
        return 0
    if n == 1 or n == 2:
        return 1
    else:
    # rabbits(n-5) = 0 when n < 5
        return rabbits(n - 1) + rabbits(n - 2) - rabbits(n-5)
```
