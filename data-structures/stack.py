from collections import deque

# # Write a function in python that can reverse a string using stack data structure. 
# # Use Stack class from the tutorial.
# # reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

# def reverse_string(sentence):
#     storage = deque()
#     result = ''
#     for l in sentence:
#         storage.append(l)
#     print(storage)
#     while len(storage) != 0:
#         result += str(storage.pop())
#     return result

# if __name__ == '__main__':
#     print(reverse_string('We will conquere COVID-19') == "91-DIVOC ereuqnoc lliw eW")

# Write a function in python that checks if paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]".
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


def is_balanced(data):
    storage = deque()
    temp = {'}': '{', ')': '(', ']': '['}
    for val in data:
        if val == '{' or val == '(' or val == '[':
            storage.append(val)
        elif val == '}' or val == ')' or val == ']':
            #check if in stack, if true continue loop, if false return false
            if len(storage) == 0 or temp[val] != storage.pop():
                return False
    return True

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))