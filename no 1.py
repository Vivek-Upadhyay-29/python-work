def func():
  try:
    l = [1,3,4,5]
    i = int(input("Enter a number:"))
    print(l[i])
  except:
    print("Some error occured")    
  finally:
   print("I am always right")
x = func()

print(x)