import time
import matplotlib.pyplot as plt

def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def time_func(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    return end_time - start_time

n_values = range(36)
fibonacci_times = [time_func(fibonacci, n) for n in n_values]
func_times = [time_func(func, n) for n in n_values]

plt.plot(n_values, fibonacci_times, label="fibonacci")
plt.plot(n_values, func_times, label="func")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.legend()
plt.show()
