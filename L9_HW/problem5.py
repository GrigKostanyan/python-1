def f(name, *args):
  if len(args) == 0:
    print "No grades available for " + name
  else:
    s = 0
    for i in args:
      s += i
    print name + ", your average grade is: " + str( s/len(args) )
f("X", 8, 10)
