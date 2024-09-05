# 8.Password Strength Checker:
#   Problem: Check if a possword is "Weak", "Medium" or "Strong".
#   Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
#   Ans:
password="Secure3P@ss"
password_length=len(password)

if password_length <6:
    strength = "Weak"
elif password_length <=10:
    strength ="Medium"
else :
    strength = "Strong"

print("Password strength is: ",strength)
