import unittest
import gaming_social_network as gsn


class TestCreateDataStructure(unittest.TestCase):

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
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
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


if __name__ == '__main__':
    unittest.main()
