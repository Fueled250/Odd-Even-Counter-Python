#S.McDonald 11/5/2016
#odd_even_counter
#This program randomly generates 100 numbers and tracks how many of said numbers are
#either even or odd. The total amount of even and odd numbers are displayed after all the
#numbers have been generated. 


import random #to be used for generating random numbers

#function to check if the number is even or odd
def check_even(num):
    if(num % 2) == 0: #check if number is even
        return True
    else:
        return False

#create a main function
def main():
    #create a counter for even numbers
    even = 0 #counter starts at 0
    #create a counter for odd numbers
    odd = 0 #counter starts at 0
    
    #range for random numbers
    for count in range(100): #range set to 100
        #obtain a random number
        num = random.randint(1, 100)
        print(num) #display the random number

        #create a counter to count all the even and odd numbers
        if(check_even(num)):
            even += 1 #if number is even, count towards even
        else:
            odd += 1 #else, number is odd, so count towards odd

    #output
    print("Total Even Numbers: ", even)
    print("Total Odd Numbers: ", odd)

#call the main()
main()
    
