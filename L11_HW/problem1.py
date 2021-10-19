class Circle:
  radius = 5.0
  color = "blue"

  def getDesc(self):
    print "A " + self.color + " circle with radus " + str(self.radius) + "."
  
circle = Circle()
circle.getDesc()
