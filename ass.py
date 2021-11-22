#Checking if a name is the same as revers
user_name=input('kindly insert your name here:').lower()
if user_name==user_name[::-1]:
    print(f'Hi{user_name}:your name is a palindrome')
    
else:
    print(f'Hi{user_name},your is not a palindrome')
