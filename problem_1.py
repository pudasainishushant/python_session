
""""
Q 4. Ask user to enter three numbers 
x = 1 
y = 2 
z = 1 
 create a list like this:
 [[0,0,0],[0,1,0],[0,0,1],[1,0,0],[1,1,1],[0,2,0],[1,2,0],[1,2,1],[0,2,1]]

"""



x = 3
y = 3
z = 2

final_list = []

for i in list(range(0,x+1)):
    for j in list(range(0,y+1)):
        for k in list(range(0,z+1)):
            final_list.append([i,j,k])

print(final_list)