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


def extract_name(sentence):
    """Extracts the name from a single sentence of the 'database' input_string.

    The name is the first word in the string.

    Args:
        sentence (str): String in form <user> is connected to <user1>, ..., <userM>
                        OR <user> likes to play <game1>, ..., <gameN>.
    """
    pos = sentence.find(' ')
    return sentence[:pos]


def extract_data(sentence, start_str):
    """Extracts the comma separated connection or film data from a sentence
    of the 'database' input_string. Starting from a given substring to the
    end of the string.

    To retrieve connections, start_str='to'. To retrieve games, start_str='play'

    Args:
        - sentence (str): String in form <user> is connected to <user1>, ..., <userM>
            OR <user> likes to play <game1>, ..., <gameN>.
        - start_str (str): Substring to identify the beginning of the desired data.
    """
    pos = sentence.find(start_str)
    if pos == -1:
        return None
    if pos + len(start_str) == len(sentence) - 1:
        return []
    items = sentence[pos + (len(start_str) + 1):].split(',')
    return list(map(lambda x: x.lstrip(), items))


def create_data_structure(string_input):
    """Parses a block of text and stores relevant
    information into a data structure.

    Args:
        string_input: block of text containing the network information

    Returns:
        The newly created network data structure
    """
    sentences = string_input.split('.')
    network = {}
    if string_input != '':
        for i in range(0, len(sentences) - 1, 2):
            connections = extract_data(sentences[i], 'to')
            games = extract_data(sentences[i + 1], 'play')
            name = extract_name(sentences[i])

            if not name in network:
                network[name] = {'connections': [], 'games': []}
            network[name]['connections'] += connections
            network[name]['games'] += games
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
    if not user in network:
        return None
    if not 'connections' in network[user]:
        return []
    return network[user]['connections']


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
    if not user in network:
        return None
    if not 'games' in network[user]:
        return []
    return network[user]['games']


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
    if user_A not in network or user_B not in network:
        return False
    if not user_B in network[user_A]['connections']:
        network[user_A]['connections'].append(user_B)
    return network


def add_new_user(network, user, games):
    """Creates a new user profile and adds that user to the network, along with
    any game preferences specified in games.

    Users have no connections to begin with.

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
    if not user in network:
        network[user] = {'connections': [], 'games': games}
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
    if user not in network:
        return None
    if network[user]['connections'] != []:
        result = []
        for conn in get_connections(network, user):
            for conn_2 in get_connections(network, conn):
                if conn_2 not in result:
                    result.append(conn_2)
        return result
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
    if user_A not in network or user_B not in network:
        return False
    common_connections = 0
    for conn in network[user_A]['connections']:
        if conn in network[user_B]['connections']:
            common_connections += 1
    return common_connections


def find_path_to_friend(network, user_A, user_B, path=None):
    """Finds a connections path from user_A to user_B. It has to be an existing
    path but it DOES NOT have to be the shortest path.

    Args:
        network: the gamer network data structure
        user_A:  String holding the starting username ("Abe")
        user_B:  String holding the ending username ("Zed")
    Returns:
        A list showing the path from user_A to user_B.
        - If such a path does not exist, return None.
        - If user_A or user_B is not in network, return None.
    """
    if path is None:
        path = []

    if user_A in network and user_B in network:
        path.append(user_A)
        current_connections = get_connections(network, user_A)
        if user_B in current_connections:
            return [user_A, user_B]
        for u in current_connections:
            if u not in path:
                next_path = find_path_to_friend(network, u, user_B, path)
                if next_path:
                    return [user_A] + next_path

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------


def users_by_game(network, game):
    """ Filters users by a liked game.

    Args:
        network: the gamer network data structure
        game (str): name of game to filter by
    Returns:
        List of users who like the game
        - None if no users like the game
    """
    result = []
    for user in network:
        if game in get_games_liked(network, user):
            result.append(user)
    if result == []:
        return None
    return result


def delete_user(network, user):
    """ Removes a user from the network, including within connections.

    Args:
        network: the gamer network data structure
        user: user to remove
    Returns:
        The updated network with the user completely removed.
        - If the user doesn't exist in the network the original *unchanged*
            network is returned
    """
    if user in network:
        del network[user]
        for u in network:
            connections = get_connections(network, u)
            if user in connections:
                i = connections.index(user)
                del connections[i]
    return network
