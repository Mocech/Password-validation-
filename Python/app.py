# Ensuring password does not match existing user data.
import maskpass

userName =input("Enter your username ")
password=maskpass.askpass()

characters = []
for char in password:
    characters.append(char)
uppercase = characters[0].upper()

CommonWords = list(("1234567890","qwertyy","aaaaa"))
if len(password) >6:
   if password in userName:
        print("Provide another  password which is not used in multiple devices")
   elif password in CommonWords:
      print("Provide new password which is not common")
   elif characters[0] == uppercase:
      print("Proceed to use the same password")
   else:
      print("Password must begin with a capital letter")    
else:
    print("Password must be more than six characters")