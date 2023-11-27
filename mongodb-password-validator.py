import os
import getpass

# Input database user's password
database_user_password = getpass.getpass("Please input your database password: ")

# Initializing required special characters list
special_characters_list = [':','/','?','#','[',']','@']

# Print entered user's password
print("The original string : " + database_user_password)

# Verify if user password contains list element via list comprehension
verify = [ele for ele in special_characters_list if(ele in database_user_password)]

# Print result
result = str(bool(verify))
if result == "False":
    print("Your password looks good.")
else:
    print ("Please replaces the password with other special character(s) such as - _ = + $ ! ")
