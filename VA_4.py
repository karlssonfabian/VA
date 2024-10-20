"""
Solutions to module VA 4

Student:
Mail:
"""
#!/usr/bin/env python3
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt 

@njit
def fib_numba(n):
    if n <= 1: return n
    return fib_numba(n-1) + fib_numba(n-2)
    


def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)


def meas_times():
	n_values = [10, 20, 30, 35, 40, 45, 47]
	python_times = []
	numba_times = []

	for n in n_values:
		start = pc()
		fib(n)
		python_times.append(pc() - start)

		start = pc()
		fib_numba(n)
		numba_times.append(pc() - start)
	
	print('Times for different n:')
	for n, python, numba in zip(n_values, python_times, numba_times):
		print(f'n = {n}: Python: {python:.4f}s. Numba: {numba:.4f}s')	
 
	plt.plot(n_values, python_times, label='Python', marker='o')
	plt.plot(n_values, numba_times, label='Numba', marker='o')
	plt.xlabel('Fibonacci n')
	plt.ylabel('Time (seconds)')
	plt.title('Fibonacci Timing Comparison')
	plt.legend()
	plt.grid()
	plt.show()

"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
def main():
	meas_times()

if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?"""