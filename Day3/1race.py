class Car:
    fuel_mp = 0.5
    fuel_default = 50
    lap_len_default = 100

    def __init__(self, color, tank_size, n_laps, lap_len, **kwargs):
        self.color = color
        self.tank_size = tank_size
        self.n_laps = n_laps
        self.lap_len = lap_len
        for key, value in kwargs.items():
            self.key = key

    # returns a remaining fuel after a lap
    def run_laps(self):
        print("Lap is done")
        return self.fuel_reducer()

    # check if the tank contains 10lt or less, tell the driver to do a pit-stop and re-fill the tank
    def check_pit_stop(self):
        if self.tank_size <= 10:
            print("Make a pit-stop and re-fill the tank")
        else:
            print("Fuel is enough")
        # return "whatever"

    def fuel_reducer(self):
        self.tank_size -= self.fuel_mp * self.lap_len
        return self.tank_size


test_car = Car('red', 50, 2, 30)
print(test_car.run_laps())
test_car.check_pit_stop()
print(test_car.run_laps())
test_car.check_pit_stop()
print(test_car.run_laps())
print(test_car.check_pit_stop())
print(test_car.run_laps())
print(test_car.check_pit_stop())
