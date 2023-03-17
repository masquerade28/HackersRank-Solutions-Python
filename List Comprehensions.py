'''
Let's learn about list comprehensions! 
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n. 
Here, 0 ≤ i ≤ x; 0 ≤ j ≤ y; 0 ≤ k ≤ z. Please use list comprehensions rather than multiple loops, as a learning exercise.
'''

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
n = int(input("Enter the sum: "))

L = []

for x in range(a+1):
    for y in range(b+1):
        for z in range(c+1):
            if x + y + z != n:
                NL = [x,y,z]
                L.append(NL)
            
print(L)
