"""

def funtion_name(parameter1,parameter2,...parameter_n):
    # doc string

    # statement1
    # statement2
    ...
    # statement n

    return return_vale1, return_vale_2..... return_value_n


value_1 = function_name(parameter_1,....parameter_2)

"""



def add_num(num1,num2):
    """
    Add two given numbers
    params: num1: int
            num2: int
    return: result : int
    """
    result = num1 + num2
    sub_result = num1 - num2
    # print("Addition ko result chai {} ho hai boro".format(result))
    return result


def sub_num(num1,num2):
    """
    Add two given numbers
    params: num1: int
            num2: int
    return: result : int
    """
    result = num1 - num2
    # sub_result = num1 - num2
    # print("Addition ko result chai {} ho hai boro".format(result))
    return result


if __name__ == "__main__":
    num1 = int(input("Enter first number \t"))
    # print("Data type of first variable is ",type(num1))
    num2 = int(input("Enter second number \t"))
    result,sub_result,div_result = add_num(num1,num2)
    # print(type(result))
    # print("Addition result is -> ",result_addition)
    print("The addition of {} and {} is {}".format(num1,num2,result))