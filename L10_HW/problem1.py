def f(*args):
  if len(args) == 0:
    return "no numbers given"
  else:
    s = 0
    for i in args:
      s += i
    return s / len(args)

print f(1,3,5)
