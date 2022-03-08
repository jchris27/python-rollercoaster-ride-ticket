print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  # elif age == 45 or age <= 55:
  elif age <= 45 and age >= 55:  
    bill = 0
    print("Everything is going to be ok. Have a free ride on us!!")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input("Do you want a photo taken? Y(Yes) or N(No).").lower()

  if wants_photo == "y":
    bill += 3

  print(f"Your final bill is ${bill}. Thank you!")
else:
  print("Sorry, you have to grow taller before you can ride.")