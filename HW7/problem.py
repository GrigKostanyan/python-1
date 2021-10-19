import timeit
class Person:
  name = "X"
  last_name = "Y"
  age = 5
  gender = "unknown"
  student = False
  __password = ""

  def Greeting(self, second_person):
    print "Welcome dear " + second_person.name + "."

  def Goodbye(self):
    print "Bye everyone!"

  def Favourite_num(self, num1):
    return "My favourite number is " + str(num1)

  def Read_file(self, filename):
    fileName = filename + ".txt"
    f = open(fileName)

  def set_password(self, p):
    self.__password = p

  def get_password(self):
    return self.__password

  def GreetingDecorator(self, person2):
    start = timeit.default_timer()
    self.Greeting(person2)
    stop = timeit.default_timer()
    print "Time: " + str(stop - start)

person1 = Person()

person1.set_password("abcd")
print person1.get_password()

person2 = Person()
person1.GreetingDecorator(person2)

person1.Goodbye()
