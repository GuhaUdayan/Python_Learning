email_id = raw_input("Enter email id:")
email = email_id.strip()
print("User name", email[0: email.find('@')])
if email.endswith(".com") :
    print("Email ends with .com" )
    print("Email service provider :", email[email.find('@') + 1 : email.find(".com") ]  )
else :
    print("Email ends with non .com ")    
