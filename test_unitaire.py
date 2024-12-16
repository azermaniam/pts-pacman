import unittest
from pacman_finale import translate_screen_to_maze


class TestTranslateScreenToMaze(unittest.TestCase):
    def test_translation(self):
        # Cas normal : coordonnées divisibles par la taille
        self.assertEqual(translate_screen_to_maze((64, 96), 32), (2, 3))

        # Cas limite : coordonnées à zéro
        self.assertEqual(translate_screen_to_maze((0, 0), 32), (0, 0))

        # Cas non divisible : arrondi à l'entier inférieur
        self.assertEqual(translate_screen_to_maze((50, 90), 32), (1, 2))

        # Cas avec taille différente
        self.assertEqual(translate_screen_to_maze((100, 200), 50), (2, 4))


if __name__ == '__main__':
    unittest.main()
    