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