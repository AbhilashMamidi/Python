#2.Movie Ticket Pricing
#problem: movie tickets are priced based on age:$12 for adults (18 and over),
#  $8 for children. Everyone gets a $2 discount on wednesday.

age=22
day="wednesday"
price=12 if age>=18 else 8
if day=="wednesday":
    price-=2
print("Ticket price for you is $",price)
 