import random
Alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

Numbers=['1','2','3','4','5','6','7','8','9','0']

Symbols=['!','@','#','$','%','^','&','*','(',')','/','?']

print("PASSWORD GENERATOR")
na=int(input("Enter number of alphabets:"))
nd=int(input("Enter number of digits:"))
ns=int(input("Enter number of special characters:"))
password_list=[]

for i in range(0,na):
  char=random.choice(Alphabets)
  password_list+=char

for i in range(0,nd):
  char1=random.choice(Numbers)
  password_list+=char1  

for i in range(0,ns):
  char2=random.choice(Symbols)
  password_list+=char2

print(password_list)

random.shuffle(password_list)

print(password_list)

print("".join(password_list))