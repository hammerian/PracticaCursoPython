x = "HolaMundo"

def myfunc():
  global x
  x = "HelloWorld"

myfunc()

print("My Python code shows " + x)