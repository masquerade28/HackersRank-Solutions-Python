'''
Given an integer, n, perform the following conditional actions:
-> If n is odd, print Weird
-> If n is even and in the inclusive range of 2 to 5, print Not Weird
-> If n is even and in the inclusive range of 6 to 20, print Weird
-> If n is even and greater than 20, print Not Weird.
'''

def Weird_Not_Weird():
    num = int(input("Enter Number To Be Checked:"))
    
    if ( num % 2 != 0):
        print("Weird")

    elif (num in range (2, 6) or num > 20):
        print("Not Weird")

    else:
        print("Weird")

Weird_Not_Weird()
