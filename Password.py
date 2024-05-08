import random
small_alphabets="abcdefghijklmnopqrstuvwxyz"
capital_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special_character="!@#$%^&*()_+<>?{}|[]"
s=small_alphabets+capital_alphabets+numbers+special_character
length=int(input("Enter length of the password:\n"))
password="".join(random.sample(s,length))
print("password:\n"+password)
