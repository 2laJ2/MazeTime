class Config:
    # set up pygame window
    WIDTH = 1000# 500 for every 20 cells of width 20
    HEIGHT = 1200# 600 for every 20 cells of width 20
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

    # setup maze variables
    x_max = 40# 20 # number of cells in the x axis 
    y_max = 20# 20 # number of cells in the y axis
    w = 20         # width of cell
    grid = []
    visited = []
    stack = []
    solution = {}
