# Lab 2 Submission

## Part A – Analysis

In this part, I analyzed four functions with respect to their behavior, purpose, and efficiency.  

**Function 1:** This function takes an integer `number` and calculates the sum of squares of all integers from 1 to `number`. For example, `function1(3)` computes `1² + 2² + 3² = 14`. The function uses a single loop running `number` times, so its time complexity is O(n). The space complexity is O(1) because it only uses a few variables and no additional data structures.  

**Function 2:** This function computes the sum of squares from 1 to `number` using the formula `(number * (number + 1) * (2 * number + 1)) // 6`. For instance, `function2(3)` returns 14. Since it only performs a few arithmetic operations, its time complexity is O(1), and the space complexity is also O(1).  

**Function 3:** This function implements a bubble sort algorithm to sort a list in ascending order. It uses nested loops to compare and swap adjacent elements. For example, `function3([3, 1, 2])` produces `[1, 2, 3]`. The worst-case and average-case time complexity is O(n²) due to the nested iterations over the list, but it sorts in-place so the space complexity is O(1).  

**Function 4:** This function calculates the factorial of a given number. For example, `function4(4)` computes `1*2*3*4 = 24`. The loop runs `number-1` times, giving a time complexity of O(n), and uses constant extra space, O(1).  

Overall, these functions illustrate a mix of iterative and formula-based approaches, highlighting the difference between algorithmic efficiency. Functions 1 and 4 scale linearly with input size, function 2 is constant-time due to the formula, and function 3 is quadratic because of the nested loops. Understanding these time and space complexities helps predict performance and guides efficient programming practices.  

---

## Part B – Programming (Recursive Functions)

The following recursive functions were implemented in `lab2.py`:

1. Factorial: Calculates `n!` recursively.
2. Linear Search: Finds the index of a key in a list recursively.
3. Binary Search: Performs a recursive search on a sorted list.

**Reflection (Optional Extension)**

While implementing these functions, I noticed that recursion simplifies certain problems like factorial and searches but uses extra memory for the call stack. Python’s simplicity makes code shorter and readable compared to C/C++, where iterative approaches often require more boilerplate. Recursive functions need careful handling of base cases, which differs from C/C++ because Python handles integer sizes and stack memory dynamically. Understanding complexity in Python allows me to choose the right algorithm for efficiency and readability.