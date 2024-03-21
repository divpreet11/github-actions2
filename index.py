def is_palindrome_extra_variable(num):
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    
    return original_num == reversed_num

number = 12321
if is_palindrome_extra_variable(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
