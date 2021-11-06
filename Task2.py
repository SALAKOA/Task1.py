#expression 0f 100/25
a = 100
b = 25
c = 100/25
print(c)

#program code for simple intrest
P = int(input("enter the value of P: "))
R = int(input("enter the value of R: "))
T = int(input("enter the value of T: "))
simple_interest = (P*R*T)/100
print(f"the simple interests is " , simple_interest)

#program for user's full name
first_name = input("enter my first name:")
last_name = input("enter my last name:")
full_name = (first_name + last_name)
print(full_name)

#program for calculating average age of 6 boys
boy1= int(input('enter the age of boy1:'))
boy2= int(input('enter the age of boy2:'))
boy3= int(input('enter the age of boy3:'))
boy4= int(input('enter the age of boy4:'))
boy5= int(input('enter the age of boy5:'))
boy6= int(input('enter the age of boy6:'))
average= (boy1+boy2+boy3+boy4+boy5+boy6) / 6
print(average)

#program that convert celcius to fahrenheit
c=float(input('enter your value in celcius'))
f=(c*1.8)+32
print(f)
