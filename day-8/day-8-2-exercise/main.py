#Write your code below this line 👇
def prime_checker(number):
# Corner case 
    is_prime = True 
    
    # Check from 2 to n-1 
    for i in range(2, number-1): 
        if number % i == 0: 
            is_prime = False; 
    
    if is_prime == True:
        print("it's a prime number")
    else:
        print("its not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
    