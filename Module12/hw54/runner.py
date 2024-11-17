class Runner:
    def __init__(self, name, speed=5):
        if not isinstance(name, str):
            raise TypeError('Name должен быть строкой')
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError('Speed должен быть положительным числом')
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
