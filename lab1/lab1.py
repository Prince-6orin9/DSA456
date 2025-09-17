# lab1.py

# Function 1: Rock-Paper-Scissors
def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()
    
    if player == opponent:
        return False
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True
    return False

# Function 2: Factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Function 3: Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Function 4: Sum to goal
def sum_to_goal(nums, goal):
    seen = set()
    for num in nums:
        complement = goal - num
        if complement in seen:
            return num * complement
        seen.add(num)
    return 0

# Class: UpCounter
class UpCounter:
    def __init__(self, step=1):
        self.step = step
        self.value = 0
    
    def count(self):
        return self.value
    
    def update(self):
        self.value += self.step

# Class: DownCounter (inherits UpCounter)
class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step

# Optional: quick tests
if __name__ == "__main__":
    print(wins_rock_scissors_paper("Rock", "Scissors"))  # True
    print(factorial(5))  # 120
    print(fibonacci(7))  # 13
    print(sum_to_goal([2, 4, 5, 7], 9))  # 20
    
    up = UpCounter(2)
    print(up.count())  # 0
    up.update()
    print(up.count())  # 2
    
    down = DownCounter(3)
    print(down.count())  # 0
    down.update()
    print(down.count())  # -3
