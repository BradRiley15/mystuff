"""
    2x + y + z = 3
    x -  y - z = 0
    x + 2y + z = 0

    [2  1  1]        [3]  1st equation
    [1 -1 -1] ans =  [0]  2nd
    [1  2  1]        [0]  3rd

    top = [a b c]
    mid = [d e f]
    bot = [g h i]
    ans = [j k l]
    
    To find discriminant for original coefficients:
    Add
    top[0]*mid[1]*bot[2]+
    top[1]*mid[2]*bot[0]+
    top[2]*mid[0]*bot[1]

    Subtract
    bot[0]*mid[1]*top[2]-
    bot[1]*mid[2]*top[0]-
    bot[2]*mid[0]*top[1]

    To replace first column with answers you must replace all the #[0]'s, because 0's are the first number in each list.
    Add
    ans[0]*mid[1]*bot[2]+
    top[1]*mid[2]*ans[2]+
    top[2]*ans[1]*bot[1]

    Subtract
    ans[2]*mid[1]*top[2]-
    bot[1]*mid[2]*ans[0]-
    bot[2]*ans[1]*top[1]

    This will produce:
    [3  1  1]
    [0 -1 -1]
    [0  2  1]
    And calculate the descriminant with that matrix    

    Now the 2nd column:
    Add
    top[0]*ans[1]*bot[2]+
    ans[0]*mid[2]*bot[0]+
    top[2]*mid[0]*ans[2]

    Subtract
    bot[0]*ans[1]*top[2]-
    ans[2]*mid[2]*top[0]-
    bot[2]*mid[0]*ans[0]

    Can you guess the 3rd?
    Add
    top[0]*mid[1]*ans[2]+
    top[1]*ans[1]*bot[0]+
    ans[0]*mid[0]*bot[1]

    Subtract
    bot[0]*mid[1]*ans[0]-
    bot[1]*ans[1]*top[0]-
    ans[2]*mid[0]*top[1]
    
"""
# Cramer's Rule in python 3!
# Brad Riley
# 4/18/16
# I tried my best to follow the process just as you would in real life.
# Beware this only works if you have 3 equations, not 2.


top = [] # Top row of numbers in the original matrix
mid = [] # Middle row
bot = [] # Bottom row
ans = [] # Answers to the equations
descrim = [0,0,0] # List for the descriminants


print("""             Coefficient #'s       Answers
             0x +  1y + 2z =          0
             3x -  4y - 5z =          1
             6x +  7y + 8z =          2
""")
for i in range(9): # Matrix Creator
    integer = int(input("Please enter coefficient #" + str(i) + ": "))
    if len(top) != 3:
        top.append(integer)
    elif len(mid) != 3:
        mid.append(integer)
    else:
        bot.append(integer)
    
for i in range(3): # Creates list for 
    integer = int(input("Please enter the answer to the equation #" + str(i) + ": "))
    ans.append(integer)


#Descriminant for the first equation with no answer plugged in
OG = top[0]*mid[1]*bot[2]+top[1]*mid[2]*bot[0]+top[2]*mid[0]*bot[1] - bot[0]*mid[1]*top[2]- bot[1]*mid[2]*top[0]-bot[2]*mid[0]*top[1]

#Descriminant with 1st column replaced with the equations answers
descrim[0] = ans[0]*mid[1]*bot[2]+top[1]*mid[2]*ans[2]+top[2]*ans[1]*bot[1] - ans[2]*mid[1]*top[2]-bot[1]*mid[2]*ans[0]-bot[2]*ans[1]*top[1]
#2nd
descrim[1] = top[0]*ans[1]*bot[2]+ans[0]*mid[2]*bot[0]+top[2]*mid[0]*ans[2] - bot[0]*ans[1]*top[2]-ans[2]*mid[2]*top[0]-bot[2]*mid[0]*ans[0]
#3rd
descrim[2] = top[0]*mid[1]*ans[2]+top[1]*ans[1]*bot[0]+ans[0]*mid[0]*bot[1] - bot[0]*mid[1]*ans[0]-bot[1]*ans[1]*top[0]-ans[2]*mid[0]*top[1]

#descrim = [1st equation descriminant with 1st column replaced, 2nd, 3rd]

input(descrim)
#Actually applying cramers rule
for i in range(3):
    ans[i] = descrim[i]/OG

#Printing answers
print("The answers to these equations are:")
for i in range(3):
    try: # Tries to convert to integer if it can so it's easier to read.
        ans[i]=int(ans[i])
    except ValueError:
        pass
    print(ans[i])
