from projects.soft import SoftProject
from projects.game_project import GameProject
from projects.game_engine_project import GameEngineProject


class GameManager:
    def __init__(self, steps_count, initial_balance):
        self.steps_count = steps_count
        self.balance = initial_balance
        self.step = 0
        self.projects = []

    def run(self):
        for step in range(self.steps_count):
            projects_count = len(self.projects)
            if projects_count > 0:
                last_project = self.projects[projects_count - 1]
                if last_project.start_step + last_project.duration > self.step:
                    self.step = self.step + 1
                    continue
                self.balance = self.balance + last_project.calc_profit()

            print('Текущий ход: ' + str(self.step))
            print('Ваш баланс: ' + str(self.balance) + '$')
            print('Выберите тип создаваемого проекта: 1 - Софт, 2 - Игровой движок, 3 - Игра')
            current_project_type = input()
            print('Выберите название проекта')
            current_name = input()
            print('Выберите сложность создаваемого проекта от 1 до 5')
            current_duration = int(input())
            if current_project_type == '1':
                current_project = SoftProject(current_name, self.step, current_duration)
            elif current_project_type == '2':
                current_project = GameProject(current_name, self.step, current_duration, 'strategy')
            elif current_project_type == '3':
                current_project = GameEngineProject(current_name, self.step, current_duration)
            else:
                raise ValueError('Неверный тип проекта')

            self.projects.append(current_project)
            self.step = self.step + 1
