# Problem Solving

## Understanding Problems
**Problem** is defined by the **set** of possible inputs and the *relationship* between them and the desired outputs.

### Steps
1. What are the inputs?
    * Find Inputs
    * Find assumptions about inputs
        * Defensive programming to accomodate for assumptions -> check if met
    * How are inputs represented?
        * Strings, Integers, Lists, Objects etc
2. What are the outputs?
    * How should outputs be specified?
        * Return, print to terminal, write to file etc
        * Output **type** 
3. Solve the problem
    * Understand relationship (mapping inputs to outputs)
        * Work out example inputs and outputs -> Also use as test cases
    * Consider systematically how a human solves the problem
    * Algorithm pseudocode of
    * Simplify algorithm to be simple mechanical + handle all cases 
    * Don’t optimize prematurely
        * Start with a simple, correct solution
    * Extract possible procedures/methods (helpers) from pseudocode algorithm
    * Write small (sometimes stub) methods then test individually
        * assert for testing
    * Complete methods to handle all cases/complexities