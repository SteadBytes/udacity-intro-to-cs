# Gaming Social Network Final Project
![Udacity CS101 Course](https://img.shields.io/badge/Udacity-CS101%20Course-02b3e4.svg)

This repository contains notes/planning, code and tests for the CS101 final project.

## Background from Course Spec
You and your friend have decided to start a company that hosts a gaming social network site. It is up to you to create a **data structure** that manages the **game-network information**
and to define several procedures that operate on the network.

In a website, the data is stored in a database. In our case, however, all the information comes in a big string of text. **Each pair of sentences** in the text is formatted as follows:
```
<user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
```
For example:
```
John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
```
Each sentence will be **separated** from the next by **only a period**. There will
not be whitespace or new lines between sentences.

Your friend records the information in that string based on user activity on the website and gives it to you to manage. You can think of every **pair of sentences as defining a user's profile**.

You may assume that `<user>` is a unique identifier for a user. For example:
* There can be at most one 'John' in the network.
* Connections are *not symmetric*.
    * if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is connected to 'Bob'.
You may assume that for all the test cases we will use, you will be given the
connections and games liked for all users listed on the right-hand side of an
'is connected to' statement. For example: 
* we will not use the string "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X." as a test case for create_data_structure because the string does not list B's connections or liked games.