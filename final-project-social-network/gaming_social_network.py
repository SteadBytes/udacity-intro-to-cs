# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#


# Example string input for testing
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def create_data_structure(string_input):
    """Parses a block of text and stores relevant
    information into a data structure.

    Args:
        string_input: block of text containing the network information

    Returns:
        The newly created network data structure
    """
    return network

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #


def get_connections(network, user):
    """  Returns a list of all the connections that user has

    Args:
        network: the gamer network data structure
        user: a string containing the name of the user
    Returns:
        A list of all connections the user has.
        - If the user has no connections, return an empty list.
        - If the user is not in network, return None.
    """
    return []


def get_games_liked(network, user):
    """  Returns a list of all the games a user likes

    Args:
        network: the gamer network data structure
        user: a string containing the name of the user
    Returns:
        A list of all games the user likes.
        - If the user likes no games, return an empty list.
        - If the user is not in network, return None.
    """
    return []


def add_connection(network, user_A, user_B):
    """Adds a connection from user_A to user_B.

    Args:
        network: the gamer network data structure
        user_A:  a string with the name of the user the connection is from
        user_B:  a string with the name of the user the connection is to

    Returns:
        The updated network with the new connection added.
        - If a connection already exists from user_A to user_B, return network unchanged.
        - If user_A or user_B is not in network, return False.
    """
    return network


def add_new_user(network, user, games):
    """Creates a new user profile and adds that user to the network, along with
    any game preferences specified in games.

    Args:
        network: the gamer network data structure
        user:    a string containing the name of the user to be added to the network
        games:   a list of strings containing the user's favorite games, e.g.:
                    ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
    Returns:
        The updated network with the new user and game preferences added. The new user
        should have no connections.
        - If the user already exists in network, return network *UNCHANGED* (do not change
            the user's game preferences)
    """
    return network


def get_secondary_connections(network, user):
    """Finds all the secondary connections (i.e. connections of connections) of a
    given user.

    Secondary connections can include the user himself/herself and a user's primary
    connection that is a secondary connection as well.

    Args:
        network: the gamer network data structure
        user:    a string containing the name of the user
    Returns:
        A list containing the secondary connections (connections of connections).
        - If the user is not in the network, return None.
        - If a user has no primary connections to begin with, return an empty list.
    """
    return []


def count_common_connections(network, user_A, user_B):
    """Finds the number of people that user_A and user_B have in common.

    Args:
        network: the gamer network data structure
        user_A:  a string containing the name of user_A
        user_B:  a string containing the name of user_B

    Returns:
        The number of connections in common (as an integer).
        - If user_A or user_B is not in network, return False.
    """
    return 0


def find_path_to_friend(network, user_A, user_B):
    """Finds a connections path from user_A to user_B. It has to be an existing
    path but it DOES NOT have to be the shortest path.

    Args:
        network: The network you created with create_data_structure.
        user_A:  String holding the starting username ("Abe")
        user_B:  String holding the ending username ("Zed")
    Returns:
        A list showing the path from user_A to user_B.
        - If such a path does not exist, return None.
        - If user_A or user_B is not in network, return None.
    """
    # your RECURSIVE solution here!
    return None

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# Your MYOP should either perform some manipulation of your network data
# structure (like add_new_user) or it should perform some valuable analysis of
# your network (like path_to_friend). Don't forget to comment your MYOP. You
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

#net = create_data_structure(example_input)
# print net
# print get_connections(net, "Debra")
# print get_connections(net, "Mercedes")
# print get_games_liked(net, "John")
# print add_connection(net, "John", "Freda")
# print add_new_user(net, "Debra", [])
# print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
# print get_secondary_connections(net, "Mercedes")
# print count_common_connections(net, "Mercedes", "John")
# print find_path_to_friend(net, "John", "Ollie")
