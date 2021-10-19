def f():
  return "Hi"
def decorator1(func = f):
  return func() + ", it's me"
def decorator2(func):
  return "<u>" + func() + "</u>"
def decorator3():
  return decorator1(f)

print decorator2(decorator1)
print decorator2(decorator3)
