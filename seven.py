# Given three ints, a b c, one of them is small, one is medium and one is large.

# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.

# Do not assume the ints will come to you in a reasonable order.

# <EXAMPLES>

 # seven(2, 4, 6) → True
# seven(4, 6, 2) → True
# seven(4, 6, 3) → False
# seven(4, 60, 9) → False

 # <HINT>
# There is a function for lists called sort.

#Defgine function
def seven(a, b, c):
    #create list 
    emplist =[a, b, c]   
    #Sort list
    emplist.sort()
    #compare differences
    if emplist[2] - emplist[1] == emplist[1] - emplist[0]:
        return True
    else:
        return False
    
print(seven(3, 4, 6))
print(seven(2, 4, 6))