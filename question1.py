colors = ['Red', 'Green', 'Black', 'Orange']

def strings_to_list_of_string(string1):
    result = list(map(list,string1))
    return result

# result = []
# for color in colors:
#     result.append(strings_to_list_of_string(color))

result = list(map(strings_to_list_of_string,colors))
print(result)
# result = strings_to_list_of_string("Suzan")
# print(result)