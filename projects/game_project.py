from projects.project import Project


class GameProject(Project):
    def __init__(self, name, start_step, duration, game_type):
        super().__init__(name, start_step, duration)
        self.game_type = game_type

