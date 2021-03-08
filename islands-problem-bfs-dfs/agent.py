class Agent:
    def __init__(self, settings):
        self.settings = settings

    def transition_function(self, state, actions):
        successors = []
        for action in actions:
            if action == self.settings.UP:
                successors.append([state[0] - 1, state[1]])
            if action == self.settings.DOWN:
                successors.append([state[0] + 1, state[1]])
            if action == self.settings.LEFT:
                successors.append([state[0], state[1] - 1])
            if action == self.settings.RIGHT:
                successors.append([state[0], state[1] + 1])

        return successors
