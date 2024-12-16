import unittest
from pacman_finale import GameRenderer, ScoreType


class TestAddScore(unittest.TestCase):
    def test_add_score(self):
        renderer = GameRenderer(600, 600)
        renderer.add_score(ScoreType.COOKIE)
        self.assertEqual(renderer._score, 10)  # Test pour un cookie

        renderer.add_score(ScoreType.POWERUP)
        self.assertEqual(renderer._score, 60)  # Ajout de 50 points (cookie + power-up)

        renderer.add_score(ScoreType.GHOST)
        self.assertEqual(renderer._score, 460)  # Ajout de 400 points pour un fantôme


if __name__ == "__main__":
    unittest.main()
