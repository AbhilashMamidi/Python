# 6.Transportation Mode Selectio
#   probelm: Choose a transportation based on the distance 
#   (e.g., <3km: Walk, 3-15km-Bike, >15km-Car)
  
distance = 5

if distance < 3:
    trasport ="Walk"
elif distance <=15:
    trasport ="Bike"
else :
    trasport = "Car"
print("AI recommends you the transport of: ",trasport)

