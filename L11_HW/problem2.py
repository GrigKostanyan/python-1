def f(car1, car2):
  return car1 + " is better than " + car2
class Car:
  model = "Eraz"
  color = "white"
  max_speed = 60

  def compareCar(self, car):
    if self.max_speed > car.max_speed:
      return f("car1", "car2")
    else:
      return f("car2", "car1")

car1 = Car()
car2 = Car()
car2.max_speed = 300
print car1.compareCar(car2)
