from maze import Maze

def main():

    def letsBegin():
        print("Let's have some fun with mazes!")

    letsBegin()

    maze1 = Maze()

    print(f"{maze1.viesti()}")

    print(f"{maze1.algo1()}")

    print(f"{maze1.algo2()}")

if __name__ == "__main__":
    main()
