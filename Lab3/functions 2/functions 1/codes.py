#1
oun = float(input("ounces"))
grams = oun * 28.3495231
print(grams)

#2
Far= float(input(" "))
Cel=(5/9)*(Far-32)
print("celcius:",Cel)

#3
def solve(num_heads, num_legs):
    
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens  
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits  
    return "No solution"

chickens, rabbits = solve(35, 94)
print("Chickens:", chickens)
print("Rabbits:", rabbits)


#4
def is_prime(n):
    if n < 2:
       return False
    for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
        return False
    return True
   

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
    
numbers = list(map(int, input().split()))

print(*filter_prime(numbers))


#5
from itertools import permutations

def print_permut(s):
    perms = permutations(s)  
    for p in perms:
        print("".join(p))  

user_input = input(" ")
print_permut(user_input)


#6
def reverse_word(s):
    words = s.split()  
    reversed_s = " ".join(reversed(words))  
    return reversed_s  

rev = input(" ")  
print(reverse_word(rev))


#8
def spy_game(nums):
    code = [0, 0, 7]  

    for num in nums:
        if num == code[0]:  
            code.pop(0)  
        if not code:  
            return True

    return False  


nums = list(map(int, input(" ").split()))


print(spy_game(nums))


#9
import math
radius=float(input(" "))

def sphere_volume(radius):
    return (4/3) *math.pi * radius ** 3

print("V=",sphere_volume(radius))


#10
def unique_elements(lst):
    unique_list = []  
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)  
    return unique_list


nums = list(map(int, input(" ").split()))


print(" ", unique_elements(nums))


#11
def is_palindrome(text):
    text = text.replace(" ", "").lower()  
    return text == text[::-1]


word = input(" ")


if is_palindrome((word)):
    print("YES!")
else:
    print("NO!")
    
    
#12
def histogram(lst):
    for num in lst:
        print('*' * num)  

nums = list(map(int, input(" ").split()))

histogram(nums)


#13
import random  


print("Hello! What is your name?")
name = input()


secret_number = random.randint(1, 20)
print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")


attempts = 0  


while True:
    attempts += 1  
    print("Take a guess.")  
    guess = int(input())  

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
        break


