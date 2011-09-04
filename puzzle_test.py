import unittest
from puzzle import PuzzleGrid, QUARTER, PENNY, EMPTY

class TestPuzzleGrid(unittest.TestCase):
    def setUp(self):
        self.grids = [
            PuzzleGrid(4, 4),
            PuzzleGrid(3, 5),
            PuzzleGrid(2, 7)
        ]

    def test_puzzle_creation(self):
        correct = [
            [QUARTER, QUARTER, QUARTER, QUARTER, EMPTY, PENNY, PENNY, PENNY, PENNY],
            [QUARTER, QUARTER, QUARTER, EMPTY, PENNY, PENNY, PENNY, PENNY, PENNY],
            [QUARTER, QUARTER, EMPTY, PENNY, PENNY, PENNY, PENNY, PENNY, PENNY, PENNY]
        ]

        for i in xrange(len(self.grids)):
            self.assertEqual(self.grids[i].initial_grid, correct[i])

    def test_puzzle_solving(self):
        correct = [
            [PENNY, PENNY, PENNY, PENNY, EMPTY, QUARTER, QUARTER, QUARTER, QUARTER],
            [PENNY, PENNY, PENNY, PENNY, PENNY, EMPTY, QUARTER, QUARTER, QUARTER],
            [PENNY, PENNY, PENNY, PENNY, PENNY, PENNY, PENNY, EMPTY, QUARTER, QUARTER]
        ]

        for i in xrange(len(self.grids)):
            grid = self.grids[i]
            self.assertEqual(grid.grid, correct[i])

    def test_moves(self):
        correct = [
            [
                (3, 4),
                (5, 3),
                (6, 5),
                (4, 6),
                (2, 4),
                (1, 2),
                (3, 1),
                (5, 3),
                (7, 5),
                (8, 7),
                (6, 8),
                (4, 6),
                (2, 4),
                (0, 2),
                (1, 0),
                (3, 1),
                (5, 3),
                (7, 5),
                (6, 7),
                (4, 6),
                (2, 4),
                (3, 2),
                (5, 3),
                (4, 5)
            ],
            [
                (2, 3),
                (4, 2),
                (5, 4),
                (3, 5),
                (1, 3),
                (0, 1),
                (2, 0),
                (4, 2),
                (6, 4),
                (7, 6),
                (5, 7),
                (3, 5),
                (1, 3),
                (2, 1),
                (4, 2),
                (6, 4),
                (8, 6),
                (7, 8),
                (5, 7),
                (3, 5),
                (4, 3),
                (6, 4),
                (5, 6)
            ],
            [
                (1, 2),
                (3, 1),
                (4, 3),
                (2, 4),
                (0, 2),
                (1, 0),
                (3, 1),
                (5, 3),
                (6, 5),
                (4, 6),
                (2, 4),
                (3, 2),
                (5, 3),
                (7, 5),
                (8, 7),
                (6, 8),
                (4, 6),
                (5, 4),
                (7, 5),
                (9, 7),
                (8, 9),
                (6, 8),
                (7, 6)
            ]
        ]

        for i in xrange(len(self.grids)):
            grid = self.grids[i]
            self.assertEqual(grid.moves, correct[i])

    def test_moves_per_turn(self):
        correct = [
            [1, 2, 3, 4, 4, 4, 3, 2, 1],
            [1, 2, 3, 4, 3, 4, 3, 2, 1],
            [1, 2, 2, 4, 2, 4, 2, 3, 2, 1]
        ]

        for i in xrange(len(self.grids)):
            grid = self.grids[i]
            self.assertEqual(grid.moves_per_turn, correct[i])

    def test_max_moves(self):
        correct = [
            4,
            4,
            4
        ]

        for i in xrange(len(self.grids)):
            grid = self.grids[i]
            self.assertEqual(grid.get_max_moves(), correct[i])

    def test_max_move_theories(self):
        for i in xrange(1, 12):
            for j in xrange(1, 12):
                grid = PuzzleGrid(i, j)
                real_max = grid.get_max_moves()
                n = min(i, j)
                m = max(i, j)
                diff = abs(n - m)
                if diff > 2:
                    expected_max = n + 2
                elif diff == 2:
                    if i < j and i % 2 == 0 or i > j and i % 2 > 0:
                        expected_max = m
                    else:
                        expected_max = m - 1
                else:
                    expected_max = m
                self.assertEqual(real_max, expected_max)

if __name__ == '__main__':
    unittest.main()
