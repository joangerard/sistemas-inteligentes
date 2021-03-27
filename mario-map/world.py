import queue
import math


class World:
    def __init__(self, map, settings, agent):
        self.map = map
        self.settings = settings
        self.agent = agent

        (self.rows, self.columns) = self.map.shape

    def discard_successors(self, successors):
        filtered_successors = []

        for successor in successors:
            i = successor[0]
            j = successor[1]

            if 0 <= i < self.rows and 0 <= j < self.columns and\
                    self.map[i][j] == self.settings.EMPTY:
                filtered_successors.append(successor)

        return filtered_successors

    def discard_successors_marios_perspective(self, successors):
        filtered_successors = []

        for successor in successors:
            i = successor[0]
            j = successor[1]

            if 0 <= i < self.rows and 0 <= j < self.columns and \
                    (self.map[i][j] == self.settings.EMPTY or self.map[i][j] == self.settings.PIPE):
                filtered_successors.append(successor)

        return filtered_successors

    def discard_neighbors(self, neighbors):
        filtered_neighbors = []

        for neighbor in neighbors:
            i = neighbor[0]
            j = neighbor[1]

            if 0 <= i < self.rows and 0 <= j < self.columns and \
                    self.map[i][j] != self.settings.VISITED and self.map[i][j] != self.settings.WALL:
                filtered_neighbors.append(neighbor)

        return filtered_neighbors

    def bfs(self, pipes):

        open = queue.SimpleQueue()

        # start bfs from pipes:
        for pipe in pipes:
            open.put(pipe)

        while open.qsize() != 0:
            state = open.get()

            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self.discard_successors(successors)

            for successor in successors:
                self.map[successor[0]][successor[1]] = self.map[state[0]][state[1]] + 1
                open.put(successor)

    def find_position_shortest_pipe_from(self, mario_position):
        open = queue.SimpleQueue()

        # start bfs from Mario:
        open.put(mario_position)

        while open.qsize() != 0:
            state = open.get()

            # Goal Test: return pipe's position
            if self.map[state[0]][state[1]] == self.settings.PIPE:
                return True, state

            # Mark state as visited
            self.map[state[0]][state[1]] = self.settings.VISITED

            # Transition Function
            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self.discard_successors_marios_perspective(successors)

            # Put the successors into the queue
            for successor in successors:
                open.put(successor)

        # No solution
        return False, None

    def get_next_step(self, current_position, map_numbers):

        # get neighbors if apply
        actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
        neighbors = self.agent.transition_function(current_position, actions)
        neighbors = self.discard_neighbors(neighbors)

        # suppose the next square that Mario will visit will be the first neighbor square
        if len(neighbors):
            next_position = neighbors[0]
            min = map_numbers[next_position[0], next_position[1]]

            for neighbor in neighbors:
                # if we find a better square on the map we will replace the next position that Mario will visit
                if map_numbers[neighbor[0], neighbor[1]] < min and \
                        map_numbers[neighbor[0], neighbor[1]] != self.settings.WALL:

                    next_position = neighbor
                    min = map_numbers[neighbor[0], neighbor[1]]

            return next_position

    def build_numbers(self):
        pipes_position = []

        # get all the pipes position
        for i in range(self.rows):
            for j in range(self.columns):
                if self.map[i][j] == 0:
                    pipes_position.append([i, j])

        self.bfs(pipes_position)
        return self.map

    def get_shortest_path(self, map_numbers, mario_position):
        current_position = mario_position

        # verify that mario has access to at least one pipe
        if map_numbers[current_position[0], current_position[1]] == math.inf:
            return map_numbers, False

        while map_numbers[current_position[0], current_position[1]] != self.settings.PIPE:
            map_numbers[current_position[0], current_position[1]] = self.settings.VISITED
            current_position = self.get_next_step(current_position, map_numbers)

        map_numbers[current_position[0], current_position[1]] = self.settings.VISITED
        return map_numbers, True
