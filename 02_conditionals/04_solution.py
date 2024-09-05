# 4.Fruit Ripeness Ckecker
#     Problem:
#       Determine if a fruit is ripe,overripe or unripe based on its color. 
#       (e.g:Banana: Green-Unripe, Yellow-Ripe, Brown-Overripe)
#     Ans:

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    else :
        print("OverRipe")

