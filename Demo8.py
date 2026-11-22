age = 20
if age > 18:
  pass
else:
  print("not eligible to vote")

value = 5
if value < 0:
  print("Negative number")
elif value == 0:
  pass
else:
  print("Positive number")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

day = 3
match day:
  case 6:
    print("weekend")
  case 7:
    print("weekend")
  case _:
    print("Other day")
  
