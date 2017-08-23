# Stirling and Bell Numbers
## Stirling Numbers
Stirling numbers *of the second kind* is the number of ways to partition a set of *n* objects into *k* non-empty sets. Denoted by **S(n,k)**.
### Formula
`S(n, k) = k*S(n-1, k) + S(n-1, k-1)`
### Example
Splitting the set [Dave, Sarah, Peter, Andy] into two sets i.e. **S(4,2)**
| Set 1      | Set 2           | 
|:-------------:|:-------------:|
| [Dave, Sarah, Peter] | [Andy] |
| [Dave, Sarah, Andy] | [Peter] |
| [Dave, Andy, Peter] | [Sarah] |
| [Sarah, Andy, Peter] | [Dave] |
| [Dave, Sarah]  | [Andy, Peter] |
| [Dave, Andy] | [Sarah, Peter] |
| [Dave, Peter] | [Andy, Sarah] |

*So* **S(4,2) = 7**

Splitting into one sets has only one way to do it:
|Set 1|
|:-----:|
| [Dave, Sarah, Peter, Andy] |

*So* **S(1,1) = 1**

Splitting into four sets also has only one way to do it:
|Set 1| Set 1| Set 1| Set 1|
|:-----:|:-----:|:-----:|:-----:|
| [Dave] |[Sarah] |[Peter] |[Andy] |
*So* **S(4,4) = 1**

## Bell Numbers
Bell numbers count the **number of partitions of a set**, that is the number of ways of splitting *n* into **any number** of parts.

### Formula w.r.t Stirling Numbers
`B(n) is the sum of S(n,k) for k =1,2, ... , n`
### Example
Starting with `B0 = B1 = 1`, the first few Bell numbers are:

```
1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213597, 27644437, 190899322, 1382958545, 10480142147, 82864869804, 682076806159, 5832742205057
```
The *n<sup>th</sup>* of these numbers , *B<sub>n</sub>* counts the number of different ways to partition a set that has **exactly** *n* elements. 

## Problem
Write two procedures, **stirling** and **bell**. The first procedure, stirling 
calculates the stirling number for a given *n* and *k*. The second procedure, bell, returns the Bell number *B(n)* for a given *n*.

### Inputs
* Stirling:
    * `n` = Int, number of items in the set
    * `k` = Int, number of sets to partition into.
* Bell:
    * `n` = Int, number of items in the set

### Outputs
* Stirling:
    * Int, Stirling number for given *n*, *k*
* Bell
    * Int, Bell number for given *n*

### Method for Stirling
* Base Cases:
    * `n = k` -> return 1
    * `k > n` -> return 0
    * `n = 0` -> return 0
    * `k = 0` -> return 0
* Recursive Case:
    * `S(n, k) = k*S(n-1, k) + S(n-1, k-1)`

```python
def stirling(n, k):
    if n == k:
        return 1
    if n >= k and n > 0 and k > 0:
        return k * stirling(n-1, k) + stirling(n-1, k-1)
    return 0
```

### Method for Bell
* Loop from 1 -> *n* 
* Calculate stirling(n, iterator)
* Return sum of stirlings

```python
def bell(n):
    result = 0
    for i in range(1, n+1):
        result += stirling(n,i)
    return result
```