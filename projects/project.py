DEFAULT_PROFIT = 1000


class Project:
    def __init__(self, name, start_step, duration):
        self.name = name
        self.start_step = start_step
        self.duration = duration

    def calc_profit(self):
        return DEFAULT_PROFIT * self.duration


