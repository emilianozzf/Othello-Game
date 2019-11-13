from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 400)
    m1 = Maze(600, 600, 150, 450, 150, 450, g)
    m2 = Maze(600, 600, 150, 450, 150, 450, g)
    m1.eat_dots(150, 150)
    m2.eat_dots(0, 150)
    assert m1.dots.top_row[2].x != 150 and m1.dots.left_col[2].y != 150
    assert m2.dots.top_row[0].x != 0 and m2.dots.top_row[-1].x != 600
