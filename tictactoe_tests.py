from tictactoe import *
import unittest

class TicTacToeTest(unittest.TestCase):
    def test_board_eq1(self):
        b0 = Board()
        b0[0][0] = X(); b0[0][1] = O(); b0[0][2] = X()
        b0[1][0] = O(); b0[1][1] = X(); b0[1][2] = O()
        b0[2][0] = O(); b0[2][1] = X()

        b1 = Board()
        b1[0][0] = X(); b1[0][1] = O(); b1[0][2] = X()
        b1[1][0] = O(); b1[1][1] = X(); b1[1][2] = O()
        b1[2][0] = O(); b1[2][1] = X()

        self.assertEqual(b0, b1, 'Boards are equality.')
        self.assertEqual(b1, b0, 'Boards are equality.')

    def test_board_eq2(self):
        b0 = Board()
        b0[0][0] = O(); b0[0][1] = O(); b0[0][2] = O()
        b0[1][0] = X(); b0[1][1] = O(); b0[1][2] = X()
        b0[2][0] = O(); b0[2][1] = X()

        b1 = Board()
        b1[0][0] = O(); b1[0][1] = O(); b1[0][2] = O()
        b1[1][0] = X(); b1[1][1] = O(); b1[1][2] = X()
        b1[2][0] = O(); b1[2][1] = X()

        self.assertEqual(b0, b1, 'Boards are equality.')
        self.assertEqual(b1, b0, 'Boards are equality.')

    def test_board_eval1(self):
        b = Board()
        b[0][0] = O(); b[0][1] = O()
        b[1][0] = X(); b[1][1] = X(); b[1][2] = X()
        b[2][0] = O()
        self.assertEqual(b.eval(),1,'X wins.')

    def test_board_eval2(self):
        b = Board()
        b[0][0] = O(); b[0][1] = X(); b[0][2] = O()
        b[1][0] = O(); b[1][1] = X(); b[1][2] = X()
        b[2][0] = O()
        self.assertEqual(b.eval(),-1,'O wins.')

    def test_full_board1(self):
        b = Board()
        b[0][0] = O(); b[0][1] = O(); b[0][2] = X()
        b[1][0] = X(); b[1][1] = X(); b[1][2] = O()
        b[2][0] = O(); b[2][1] = X(); b[2][2] = O()
        self.assertTrue(b.full(),'Full Board.')

    def test_full_board2(self):
        b = Board()
        b[0][0] = X(); b[0][1] = O(); b[0][2] = O()
        b[1][0] = O(); b[1][1] = X(); b[1][2] = X()
        b[2][0] = O(); b[2][1] = X(); b[2][2] = O()
        self.assertTrue(b.full(),'Full Board.')

    def test_minimax1(self):
        b = Board()
        b[0][0] = X; b[0][1] = O(); b[0][2] = O()
        b[1][0] = X; b[1][1] = O()
        self.assertEqual(minimax(Computer,b),1,'Board contains a win for X.')

    def test_minimax2(self):
        b = Board()
        b[0][0] = X; b[0][1] = O()
        b[1][0] = X; b[1][1] = X()
        b[2][0] = O; b[2][1] = O()
        self.assertEqual(minimax(Computer,b),1,'Board contains a win for X.')

if __name__ == '__main__':
   unittest.main()




