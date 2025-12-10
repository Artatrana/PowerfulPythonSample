# Nonlocal variable in python 
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

numberList = [15, 85, 35, 89, 125, 2]
print(max(numberList))