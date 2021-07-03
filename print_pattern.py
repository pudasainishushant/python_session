# for num in range(10):
#     for i in range(num):
#         print(num,end=" ") 
#     print("\n")

# """
# 1st loop - num ->0
# 2nd loop -num -> 1
#     - Inner loop -> i -> 0 -> num -> 1
# 3rd loop - num -> 2
#     - Inner loop -> print 2 times
# 4th loop -num -> 3


# """
# """
# Output - 
# 1
# 2 2
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 

for i in range(5):
    """
    1t loop - i -> 0
    2nd - i -> 1
    3rd -i -> 2
    """
    for j in range(i):
        print(j,end=" ")
    print("\n")