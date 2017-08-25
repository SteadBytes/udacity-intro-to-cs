# Into to CS Final Project - Gaming Social Network
## Background
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

## Project Description
Complete the procedures according to the specifications below
as well as to implement a Make-Your-Own procedure (MYOP).

### Procedures/Specification
 #### `create_data_structure(string_input)`: 
  Parses a block of text and stores relevant 
  information into a data structure. You are free to choose and design any 
  data structure you would like to use to manage the information.

Arguments: 
  * string_input: block of text containing the network information

  You may assume that for all the test cases we will use, you will be given the 
  connections and games liked for all users listed on the right-hand side of an
  'is connected to' statement. For example, we will not use the string 
  "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
  as a test case for create_data_structure because the string does not 
  list B's connections or liked games.
  
  The procedure should be able to handle an empty string (the string '') as input, in
  which case it should return a network with no users.

Returns :
  * The newly created network data structure

#### `get_connections(network, user)`: 
  Returns a list of all the connections that user has

Arguments: 
  * network: the gamer network data structure
  * user:    a string containing the name of the user

Returns: 
  * A list of all connections the user has.
  * If the user has no connections, return an empty list.
  * If the user is not in network, return None.

#### `get_games_liked(network, user)`: 
  Returns a list of all the games a user likes

Arguments: 
  * network: the gamer network data structure
  * user: a string containing the name of the user

Returns: 
  * A list of all games the user likes.
  * If the user likes no games, return an empty list.
  * If the user is not in network, return None.

#### `add_connection(network, user_A, user_B)`: 
  Adds a connection from user_A to user_B. Make sure to check that both users 
  exist in network.

Arguments: 
  * network: the gamer network data structure 
  * user_A:  a string with the name of the user the connection is from
  * user_B:  a string with the name of the user the connection is to

Returns: 
  * The updated network with the new connection added.
  * If a connection already exists from user_A to user_B, return network unchanged.
  * If user_A or user_B is not in network, return False.

#### `add_new_user(network, user, games)`: 
  Creates a new user profile and adds that user to the network, along with
  any game preferences specified in games. Assume that the user has no 
  connections to begin with.

Arguments:
  * network: the gamer network data structure
  * user:    a string containing the name of the user to be added to the network
  * games:   a list of strings containing the user's favorite games:
    * ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']

Returns: 
  * The updated network with the new user and game preferences added. The new user 
  should have no connections.
  * If the user already exists in network, return network *UNCHANGED* (do not change
    the user's game preferences)

#### `get_secondary_connections(network, user)`: 
  Finds all the secondary connections (i.e. connections of connections) of a 
  given user.

Arguments: 
  * network: the gamer network data structure
  * user: a string containing the name of the user

Returns: 
  * A list containing the secondary connections (connections of connections).
  * If the user is not in the network, return None.
  * If a user has no primary connections to begin with, return an empty list.

**NOTE:** 
  It is OK if a user's list of secondary connections includes the user 
  himself/herself. It is also OK if the list contains a user's primary 
  connection that is a secondary connection as well.

#### `count_common_connections(network, user_A, user_B)`: 
  Finds the number of people that user_A and user_B have in common.
 
Arguments: 
  * network: the gamer network data structure
  * user_A:  a string containing the name of user_A
  * user_B:  a string containing the name of user_B

Returns: 
  * The number of connections in common (as an integer).
  * If user_A or user_B is not in network, return False.

#### `find_path_to_friend(network, user_A, user_B)`: 
  Finds a connections path from user_A to user_B. It has to be an existing 
  path but it DOES NOT have to be the shortest path.
  
Arguments:
  * network: The network you created with create_data_structure. 
  * user_A:  String holding the starting username ("Abe")
  * user_B:  String holding the ending username ("Zed")

Returns:
  * A list showing the path from user_A to user_B.
  * If such a path does not exist, return None.
  * If user_A or user_B is not in network, return None.

Sample output:
```
>>> print(find_path_to_friend(network, "Abe", "Zed"))
>>> ['Abe', 'Gel', 'Sam', 'Zed']
```
This implies that Abe is connected with Gel, who is connected with Sam, 
who is connected with Zed.

**NOTE:**
  You must solve this problem using recursion!

Hints: 
* Be careful how you handle connection loops, for example: 
    * A is connected to B. B is connected to C. C is connected to B. Make sure your code terminates in 
  that case.
* If you are comfortable with default parameters, you might consider using one in this procedure to keep track of nodes already visited in your search. You may safely add default parameters since all calls used in the grading script 
will only include the arguments network, `user_A`, and `user_B`.

#### Make-Your-Own-Procedure (MYOP)
Your MYOP should either perform some manipulation of your network data structure (like `add_new_user`) or it should perform some valuable analysis of your network (like `path_to_friend`).