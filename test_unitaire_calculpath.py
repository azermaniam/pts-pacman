import unittest
from pacman_finale import Ghost, Pathfinder, PacmanGameController


class TestGhostPathfinding(unittest.TestCase):
    def test_calculate_path(self):
        # Setup
        game_controller = PacmanGameController()
        ghost = Ghost(None, 3, 3, 32, game_controller)
        pathfinder = Pathfinder(game_controller.numpy_maze)

        # Simuler un chemin
        path = pathfinder.get_path(3, 3, 5, 5)
        ghost.set_new_path(path)

        # Vérifications
        self.assertIsNotNone(ghost.location_queue)  # Vérifie que le chemin existe
        self.assertEqual(len(ghost.location_queue), len(path))  # Longueur correcte


if __name__ == "__main__":
    unittest.main()
