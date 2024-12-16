import unittest
from pacman_finale import MovableObject, GameRenderer, Wall


class TestHandleCollision(unittest.TestCase):
    def test_collision_in_direction(self):
        renderer = GameRenderer(600, 600)
        wall = Wall(renderer, 1, 1, 32)
        renderer.add_wall(wall)

        movable = MovableObject(renderer, 32, 32, 32)
        collision, _ = movable.check_collision_in_direction((-1, 0))  # Collision à gauche
        self.assertTrue(collision)

        collision, _ = movable.check_collision_in_direction((1, 0))  # Pas de collision à droite
        self.assertFalse(collision)


if __name__ == "__main__":
    unittest.main()
