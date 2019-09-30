from ..Game.app import Logic, Structure, Prompts
from unittest import TestCase, mock
from unittest.mock import patch
import io
import unittest


class TestTic(TestCase):

    def setUp(self):
        self.logic = Logic()
        self.board = Structure()
        self.Prompts = Prompts()

    def test_choose_whether_to_play_again(self):
        case = self.Prompts.playAgain()
        original_input = mock.builtins.input
        mock.builtins.input = lambda: "yes"
        self.assertEqual(case, False)
        mock.builtins.input = original_input

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcome_message(self, mock_stdout):
        self.board.welcome()
        assert mock_stdout.getvalue() == 'Welcome to Tic Tac Toe, My Version!\n'  

    @patch('random.randint', return_value=1)
    def test_who_goes_first(self, mocked_randint):
        mocked_randint.value = (0, 1)
        self.assertTrue(self.logic.whoGoesFirst(), 'human')

    def test_updated_board(self):
        case = self.logic.updatedBoard([1, "A", 3, "Y", 5, 6, 7, 8, 9])
        self.assertTrue(case, True)

    def test_free_spaces_on_board(self):
        case = self.logic.freeSpaces(
            [' ', "A", ' ', "Y", ' ', ' ', ' ', '', '', ''], 5)
        self.assertTrue(case, True)

    def test_its_a_tie(self):
        case = self.logic.itsATie([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertTrue(case)


if __name__ == "__main__":
    unittest.main()