weight = 2

#ground shipping
if weight <= 2: 
  cost = weight * 1.5 + 20
  print("Ground shipping will cost $" + str(cost) + "0" + " based on a weight of " + str(weight) + " lbs.")
elif weight <= 6:
  cost = weight * 3 + 20
  print("Ground shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs")
elif weight <= 10:
  cost = weight * 4 + 20
  print("Ground shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs")
else:
  cost = weight * 4.75 + 20
  print("Ground shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs.")

#premium ground shipping
premium_ground_shipping = 125

print("Premium ground shipping is $" + str(premium_ground_shipping) + ".")

#Drone shipping
if weight <= 2:
  cost = weight * 4.5
  print("Drone shipping will cost $" + str(cost) + " based on weight.")
elif weight <= 6: 
  cost = weight * 9
  print ("Drone shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs.")
elif weight <= 10:
  cost = weight * 12
  print("Drone shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs.")
else:
  cost = weight * 14.25
  print("Drone shipping will cost $" + str(cost) + " based on a weight of " + str(weight) + " lbs.")




