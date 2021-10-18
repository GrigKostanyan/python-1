name = "Batman"
age = 2
password = "Superman*"

if name == "Batman":
  print "Welcome Mr. Batman!"

if age < 16:
  print "Dear " + name + ", you are too young to register"

if not ('*' in password) or not('&' in password):
  print "Please enter a different password"
