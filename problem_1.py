

x = 2
y = 2
z = 2
n = 2
final_list = []



for i in list(range(0,x+1)):
    for j in list(range(0,y+1)):
        for k in list(range(0,z+1)):
            final_list.append([i,j,k])

# print(final_list)


filtered_list = [i for i in final_list if sum(i)!=n]
# filtered_list = []
# for i in final_list:
#     if sum(i)!=3:
#         filtered_list.append(i)

print(filtered_list)
