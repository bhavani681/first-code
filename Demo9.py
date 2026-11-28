i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1  

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

x = ["apple","banana","cherry"]
for x in fruits:
  print(x)

#looping throgh a string
for x in "banana":
  print(x)

#the break satement
x = ["apple","banana","cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

x = ["apple","banana","cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#the continue statement
x == ["apple","banana","cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  

#the range() function
for x in range(6):
  print(x)

#using the start parameter
for x in range(2, 6):
  print(x)

#adding third parameter
for x in range(2, 30, 3):
  print(x)

#else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3:
    break
  print(x)
else:
    print("Finished")

#nested loop
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
  for x in fruits:
    print(x)
