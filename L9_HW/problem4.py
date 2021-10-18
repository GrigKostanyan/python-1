def f(password):
  if len(password) < 10:
    return False
  digitCount = 0
  for i in password:
    if i >= '1' and i <= '9':
      digitCount += 1
      if digitCount >= 2:
        return True
  return False

if f("12aaaaaaaa") == True:
  print "True"
else:
  print "False"
