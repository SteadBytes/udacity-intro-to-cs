import unittest
import gaming_social_network as gsn
from copy import deepcopy


class TestNetwork(unittest.TestCase):

    def setUp(self):
        self.example_input = "John is connected to Bryant, Debra, Walter.\
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
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Jeff is connected to .\
Jeff likes to play ."
        self.network = gsn.create_data_structure(self.example_input)

    def test_empty_string(self):
        net = gsn.create_data_structure('')
        self.assertEqual(net, {}, 'Empty string should return empty dict')

    def test_normal_input(self):
        john_expected = {'connections': ['Bryant', 'Debra', 'Walter'], 'games': [
            'The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']}
        freda_expected = {'connections': ['Olive', 'John', 'Debra'], 'games': [
            'Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']}
        self.assertIsInstance(self.network, dict)
        self.assertEqual(self.network['John'], john_expected)
        self.assertEqual(self.network['Freda'], freda_expected)

    def test_extract_name(self):
        name = gsn.extract_name('John is connected to Bryant, Debra, Walter.')
        self.assertIsInstance(name, str)
        self.assertEqual(name, 'John')

    def test_extract_connections(self):
        connections = gsn.extract_data(
            'John is connected to Bryant, Debra, Walter', 'to')
        self.assertIsInstance(connections, list)
        self.assertEqual(connections, ['Bryant', 'Debra', 'Walter'])

    def test_extract_games(self):
        sentence = ('John likes to play The Movie: The Game,'
                    'The Legend of Corgi, Dinosaur Diner')
        games = gsn.extract_data(sentence, 'play')
        self.assertIsInstance(games, list)
        self.assertEqual(games, ['The Movie: The Game',
                                 'The Legend of Corgi', 'Dinosaur Diner'])

    def test_extract_data_no_start_str(self):
        sentence = ('John likes to The Movie: The Game,'
                    'The Legend of Corgi, Dinosaur Diner')
        self.assertIsNone(gsn.extract_data(sentence, 'play'))

    def test_get_connections(self):
        ollie_expected = ['Mercedes', 'Freda', 'Bryant']
        connections = gsn.get_connections(self.network, 'Ollie')
        self.assertIsInstance(connections, list)
        self.assertEqual(connections, ollie_expected)

    def test_get_connections_no_user(self):
        """ Test whether get_connections returns None for a user
        **not** present in the network
        """
        self.assertIsNone(gsn.get_connections(self.network, 'Bilbo_Baggins'))

    def test_get_connections_no_connections(self):
        self.network['Test_User'] = {}
        self.assertEqual(gsn.get_connections(self.network, 'Test_User'), [])
        self.network.pop('Test_user', None)

    def test_get_connections_empty_connections(self):
        self.assertEqual(gsn.get_connections(self.network, 'Jeff'), [])

    def test_get_games_liked(self):
        ollie_expected = ['Call of Arms',
                          'Dwarves and Swords', 'The Movie: The Game']
        games = gsn.get_games_liked(self.network, 'Ollie')
        self.assertIsInstance(games, list)
        self.assertEqual(games, ollie_expected)

    def test_get_games_liked_no_user(self):
        self.assertIsNone(gsn.get_games_liked(self.network, 'Bilbo_Baggins'))

    def test_get_get_games_liked_no_games(self):
        self.network['Test_User'] = {}
        self.assertEqual(gsn.get_games_liked(self.network, 'Test_User'), [])

    def test_get_get_games_liked_empty_connections(self):
        self.assertEqual(gsn.get_games_liked(self.network, 'Jeff'), [])

    def test_add_connection(self):
        updated_network = gsn.add_connection(self.network, 'John', 'Mercedes')
        self.assertIsInstance(updated_network, dict)
        self.assertIn('Mercedes', self.network['John']['connections'])
        self.assertNotIn('John', self.network['Mercedes']['connections'])

    def test_add_connection_no_user(self):
        """ Test whether add_connection returns False if either user_A or user_B
        not present in the network
        """
        unknown_user = 'unkown_user'
        known_user = 'John'
        # Should return False if *either* user_A or user_B not in network
        # -> try both ways round
        self.assertFalse(gsn.add_connection(
            self.network, unknown_user, known_user))
        self.assertFalse(gsn.add_connection(
            self.network, known_user, unknown_user))

    def test_add_connection_existing_connection(self):
        # Deepcopy is O(NM) time -> better way to test?
        current_network = deepcopy(self.network)
        # Connection already present, should make no changes to network
        network = gsn.add_connection(self.network, 'John', 'Bryant')
        self.assertEqual(current_network, network)

    def test_add_new_user(self):
        user = 'Gandalf'
        games = ['Lord of the Rings: War in the North',
                 'Minecraft', 'Dwarf Fortress']
        self.assertIsInstance(gsn.add_new_user(
            self.network, user, games), dict)
        self.assertIn(user, self.network,
                      'User %s not added to network successfully' % user)
        self.assertEqual(self.network[user]['games'], games,
                         'User %s games not added to network succesfully' % user)

        self.assertEqual(self.network[user]['connections'], [])

    def test_add_new_user_existing_user(self):
        games = ['Lord of the Rings: War in the North',
                 'Minecraft', 'Dwarf Fortress']
        # Deepcopy is O(NM) time -> better way to test?
        current_network = deepcopy(self.network)
        # User already present, should make no changes to network
        network = gsn.add_new_user(self.network, 'John', games)
        self.assertEqual(current_network, network)

    def test_get_secondary_connections(self):
        expected = ['Olive', 'Ollie', 'Freda', 'Mercedes', 'Walter',
                    'Levi', 'Jennie', 'Robin', 'John', 'Bryant']
        conns = gsn.get_secondary_connections(self.network, 'John')
        self.assertIsInstance(conns, list)
        self.assertEqual(conns, expected)

    def test_get_secondary_connections_no_user(self):
        """ Test whether get_secondary_connections returns None for a user
        **not** present in the network
        """
        self.assertIsNone(gsn.get_secondary_connections(
            self.network, 'Unkown_User'))

    def test_get_secondary_connections_no_primary(self):
        """Test whether get_secondary_connections return empty list for
        a user with no primary connections
        """
        self.network['Test_User'] = {'connections': []}
        self.assertEqual(gsn.get_secondary_connections(
            self.network, 'Test_User'), [])

    def test_count_common_connections(self):
        expected = 2
        common_connections = gsn.count_common_connections(
            self.network, 'Levi', 'Olive')
        self.assertEqual(common_connections, expected)

    def test_count_common_connections_no_connections(self):
        common_connections = gsn.count_common_connections(
            self.network, 'John', 'Jennie')
        self.assertEqual(common_connections, 0)

    def test_count_common_connections_no_user(self):
        unknown_user = 'unkown_user'
        known_user = 'John'
        # Should return False if *either* user_A or user_B not in network
        # -> try both ways round
        self.assertFalse(gsn.count_common_connections(
            self.network, unknown_user, known_user))
        self.assertFalse(gsn.count_common_connections(
            self.network, known_user, unknown_user))

    def test_find_path_to_friend_short(self):
        path = gsn.find_path_to_friend(self.network, 'John', 'Olive')
        for i in range(1, len(path)):
            self.assertIn(path[i], self.network[path[i - 1]]['connections'])

    def test_find_path_to_friend_long(self):
        path = gsn.find_path_to_friend(self.network, 'John', 'Robin')
        for i in range(1, len(path)):
            self.assertIn(path[i], self.network[path[i - 1]]['connections'])

    def test_find_path_to_friend_no_path(self):
        self.assertIsNone(gsn.find_path_to_friend(
            self.network, 'John', 'Jeff'))

    def test_find_path_to_friend_no_user(self):
        unknown_user = 'unkown_user'
        known_user = 'John'
        # Should return None if *either* user_A or user_B not in network
        # -> try both ways round
        self.assertIsNone(gsn.find_path_to_friend(
            self.network, unknown_user, known_user))
        self.assertIsNone(gsn.find_path_to_friend(
            self.network, known_user, unknown_user))

    def test_find_path_to_friend_circular(self):
        """ Test find_path_to_friend recursion terminates with connection loops.
        i.e. A is connected to B. B is connected to C. C is connected to B
        """
        self.network['A'] = {'connections': ['B']}
        self.network['B'] = {'connections': ['C']}
        self.network['C'] = {'connections': ['B', 'D']}
        self.network['D'] = {}
        expected = ['A', 'B', 'C', 'D']
        self.assertEqual(gsn.find_path_to_friend(
            self.network, 'A', 'D'), expected)

    def test_users_by_game(self):
        expected = ['John', 'Jennie']
        users = gsn.users_by_game(self.network, 'Dinosaur Diner')
        self.assertIsInstance(users, list)
        self.assertEqual(users, expected)

    def test_users_by_game_no_game(self):
        """ Test whether users_by_game returns None when no users like the game.
        """
        self.assertIsNone(gsn.users_by_game(self.network, 'COD_WAW'))

    def test_delete_user(self):
        """ Test whether user removed from network and from
            any other user connections
        """
        gsn.delete_user(self.network, 'John')
        self.assertNotIn('John', self.network)
        for user in self.network:
            self.assertNotIn('John', self.network[user]['connections'],
                             '\'John\' found in %s connections' % user)

    def test_delete_user_no_user(self):
        """Test whether delete_user returns original *unchanged* network when
        given a user that doesn't exist.
        """
        # Deepcopy is O(NM) time -> better way to test?
        current_network = deepcopy(self.network)
        # User already present, should make no changes to network
        network = gsn.delete_user(self.network, 'Gandalf')
        self.assertEqual(current_network, network)


if __name__ == '__main__':
    unittest.main()
