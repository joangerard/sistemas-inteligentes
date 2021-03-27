import numpy as np
from world import World
from settings import Settings
from agent import Agent
import math


def first_approach():
    '''
    This method is used to resolve the 2nd assignment
    '''
    inf = math.inf
    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    map = np.array([[inf, -1 , inf,  0 ],
                    [inf, inf, inf, -1],
                    [inf, -1 , inf, -1],
                    [0, -1 , inf, inf]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)

    # First solution (from pipes' perspective): generate numbers and then return shortest path:
    map_numbers = world.build_numbers()
    print('Number of squares to arrive to shortest pipe:\n', map_numbers)

    mario_position = [0, 0]
    mario_path, success = world.get_shortest_path(map_numbers, mario_position)
    if success:
        print('Shortest path (-2 marks the path to be followed by Mario to the shortest path):\n', mario_path)
    else:
        print('No solution')


def second_approach():
    '''
    You can use this approach to compare BFS with A* algorithm
    '''

    inf = math.inf
    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    map = np.array([[inf, -1 , inf,  0],
                    [inf, inf, inf, -1],
                    [inf, -1 , inf, -1],
                    [0,   -1 , inf, inf]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)
    mario_position = [0, 0]

    success, pipe_position = world.find_position_shortest_pipe_from(mario_position)

    if success:
        print('Shortest pipe is at position:\n', pipe_position)
    else:
        print('No solution')


def main():
    # first_approach()
    second_approach()


if __name__ == "__main__":
    main()
