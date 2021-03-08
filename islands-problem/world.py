import queue


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

            if 0 <= i < self.rows and  0 <= j < self.columns and self.map[i][j] == self.settings.ISLAND:
                filtered_successors.append(successor)

        return filtered_successors

    def mark_island_as_visited_bfs(self, i, j):
        open = queue.SimpleQueue()
        close = []

        open.put([i, j])

        while open.qsize() != 0:
            state = open.get()
            # mark it as visited
            self.map[state[0]][state[1]] = self.settings.VISITED
            print(self.map, "\n")

            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self.discard_successors(successors)

            close.append(state)

            for successor in successors:
                open.put(successor)

    def mark_island_as_visited_dfs(self, i, j):
        # stack
        open = []
        close = []

        open.append([i, j])

        while len(open) != 0:
            state = open.pop()
            # mark it as visited
            self.map[state[0]][state[1]] = self.settings.VISITED
            print(self.map, "\n")

            actions = [self.settings.UP, self.settings.DOWN, self.settings.LEFT, self.settings.RIGHT]
            successors = self.agent.transition_function(state, actions)
            successors = self.discard_successors(successors)

            close.append(state)

            for successor in successors:
                open.append(successor)

    def number_of_islands(self):
        islands = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.map[i][j] == 1:
                    self.mark_island_as_visited_bfs(i, j)
                    islands += 1

        return islands
