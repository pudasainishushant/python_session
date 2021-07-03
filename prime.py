
nums = [2,5,7,8,9,10,5,21]

def prime_or_not(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
    
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True
    
    else:
        return False

# prime_only = []
# for n in nums:
#     if prime_or_not(n) == True:
#         prime_only.append(n)
#     else:
#         pass

# print(prime_or_not(100))

primt_only = list(filter(prime_or_not,nums))
print(primt_only)