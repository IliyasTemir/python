#1
from functools import reduce
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)

#2
import math
def count_case_letters(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())

    return {"Uppercase": upper_count, "Lowercase": lower_count}

if __name__ == "__main__":
    user_input = input()
    result = count_case_letters(user_input)
    
    print(f"{result['Uppercase']}")
    print(f"{result['Lowercase']}")

#3
def palindrome(t):
    clean_t = ''.join(filter(str.isalnum, t)).lower()
    return clean_t == clean_t[::-1]

if __name__ == "__main__":
    user_input = input()
    if palindrome(user_input):
        print("Yes")
    else:
        print("No")

#4
import time
import math

def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

if __name__ == "__main__":
    num = int(input())  
    delay = int(input("milliseconds: "))
    delayed_square_root(num, delay)
    
#5
def all_elements_true(t):
    return all(t)
