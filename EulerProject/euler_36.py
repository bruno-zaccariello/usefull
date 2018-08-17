from my_functions.my_math import to_binary

def is_palindrome(string):
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1]) if string[0] == string[-1] else False

def get_result():
    ans = []
    for i in range(10**6):
        if is_palindrome(str(i)) and is_palindrome(to_binary(i)):
            ans.append(i)
    return ans