from maze import Maze


def main():

    def letsBegin():
        print("Let's have some fun with mazes!")

    letsBegin()

    maze1 = Maze(1)

    print(f"{maze1.viesti()}")


if __name__ == "__main__":
    main()
