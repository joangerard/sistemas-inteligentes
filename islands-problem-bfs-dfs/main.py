import numpy as np
from world import World
from settings import Settings
from agent import Agent


def main():
    map = np.array([[1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1],
                    [1, 0, 1, 0, 1]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)

    number_islands = world.number_of_islands()

    print(world.map)
    print(number_islands)


if __name__ == "__main__":
    main()
