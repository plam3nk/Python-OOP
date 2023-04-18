from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('Plamen', 19, 100)
        self.other = TennisPlayer('Ivan', 19, 80)

    def test_correct_initialization(self):
        self.assertEqual(self.player.name, 'Plamen')
        self.assertEqual(self.player.age, 19)
        self.assertEqual(self.player.points, 100)
        self.assertEqual(self.player.wins, [])

    def test_is_name_not_long_enough(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'pl'

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_not_old_enough(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_that_is_already_added_returns_string(self):
        self.player.wins = ['tournament']

        result = self.player.add_new_win('tournament')

        self.assertEqual(result, "tournament has been already added to the list of wins!")

    def test_add_new_win_successfully(self):
        self.player.add_new_win('tournament')
        self.assertEqual(self.player.wins[0], 'tournament')

    def test_other_is_better_player_returns_string(self):
        self.player.points = 50
        result = self.player < self.other

        self.assertEqual(result, f'{self.other.name} is a top seeded player and'
                                 f' he/she is better than {self.player.name}')

    def test_player_is_better_than_other_returns_string(self):
        result = self.player < self.other

        self.assertEqual(result, f'Plamen is a better player than Ivan')

    def test_str_method(self):
        self.player.add_new_win('Race')
        self.player.add_new_win('Cars')

        self.assertEqual(str(self.player), 'Tennis Player: Plamen\n'
                                           'Age: 19\n'
                                           'Points: 100.0\n'
                                           'Tournaments won: Race, Cars')

    def test_str_method_with_empty_tournaments(self):
        self.assertEqual(str(self.player), 'Tennis Player: Plamen\n'
                                           'Age: 19\n'
                                           'Points: 100.0\n'
                                           'Tournaments won: ')


if __name__ == '__main__':
    main()