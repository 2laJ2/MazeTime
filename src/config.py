class Config:
    # set up pygame window
    WIDTH = 500 # 500 for every 20 cells of width 20, max appr. 1820
    HEIGHT = 600 # 600 for every 20 cells of width 20, max appr. 980
    FPS = 30

    # define colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LIGHTBLUE = (0, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255 ,255 ,0)
    ORANGE = (255, 175, 0)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    LABYRINTH_COLOUR = PURPLE

    # setup maze variables
    x_max = 20 # 20# number of cells in the x axis
    y_max = 20 # 20# number of cells in the y axis
    w = 20     # width of cell, visualization of the solution path not visible if less than 4
    grid = []
    visited = {}
    stack = []
    solution = {}

    # values used with time function of the algorithms
    ABMAZE = 0.001 # 0.000001 large labyrinth
    WILSON_MYSTEERI = 0.05 # 0.000001 large labyrinth
    RATKAISU = 0.05 # 0.000001 large labyrinth
    NOLLA = 0.0

    # seed value used with creating mazes
    SEED = 0