
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car Go')

    def stop(self):
        print('Car Stop')

    def turn(self, direction):
        print('Car turn', direction)

    def show_speed(self):
        print('SPEED', self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('OVER 60 SPEED')
        else:
            print('SPEED', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('OVER 40 SPEED')
        else:
            print('SPEED', self.speed)


class PoliceCar(Car):
    pass


tcar = TownCar(40, 'RED', 'BMW', is_police=False)
print(tcar.name)
print(tcar.color)
print('POLICE', tcar.is_police)
tcar.show_speed()
tcar.go()
tcar.stop()
tcar.turn('right')

police = PoliceCar(100, 'Black', 'UAZ', True)
print(police.name)
print(police.color)
print('POLICE', police.is_police)
police.show_speed()
police.go()
police.stop()
police.turn('left')

wcar = WorkCar(50, 'YELLOW', 'KAMAZ', False)
print(wcar.name)
print(wcar.color)
print('POLICE', wcar.is_police)
wcar.show_speed()
wcar.go()
wcar.stop()
wcar.turn('left')
