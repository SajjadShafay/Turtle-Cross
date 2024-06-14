from car import Car


class Carmanager:
    def __init__(self):
        self.car_list = []
        for _ in range(35):
            self.car_list.append(Car())

    def next_level(self):
        for item in self.car_list:
            item.next_level()

    def move_cars(self):
        for item in self.car_list:
            item.move()

    def detect_collisions(self, player):
        for item in self.car_list:
            if item.detect_collision(player):
                return True
