# A program to count the number of ways to reach n'th stair

# Recurssive program to find n'th fibonacci number

# you can climb 1 or 2 or 3 stairs at a time
def fib(n):
    if n <= 1:
        return n
    if n == 2:
        return n
    if n == 3:
        return n+1
    return fib(n - 1) + fib(n - 2) + fib(n -3)


# returns no. of ways to reach s'th stair
def countWays(s):
    return fib(s)


# Driver program

s = 4
print("Number of ways = ",countWays(s))

'''
1
1

2
11 2

3
111 12 21 3

4
1111    112 121 211  13 31 22 

5



'''