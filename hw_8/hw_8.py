#1 Напишите декоратор, который проверял бы тип параметров
#функции, конвертировал их если надо и складывал:
def typed(func):
 def add_two_symbols(a,b):
  if type(a) == type(b) == str:
   func()
  elif type(a) == int:
   a = str(a)
   func()
  elif type(b) == int:
   b = str(b)
   func()
  return add_two_symbols()


@typed
def func(a, b):
 print(a+b)

func("3", 5)
