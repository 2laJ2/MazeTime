class Config:
    # set up pygame window
    WIDTH = 500
    HEIGHT = 600
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
    x = 20          # x axis
    y = 20          # y axis
    w = 20          # width of cell
    grid = []
    visited = []
    stack = []
    solution = {}
