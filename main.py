def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    if n <= 1:
      counts[n] += 1
      return n
    counts[n] += 1
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)

"""
Q4,
"""
def print_fibonacci_and_counts(n):
  counts = [0] * (n+1)
  fibonacci_numbers = []

  for i in range(n+1):
      fibonacci_numbers.append(fib_recursive(i, counts))

  print("Fibonacci numbers:")
  print(fibonacci_numbers)
  print("\nCounts:")
  print(counts)

print_fibonacci_and_counts(10)
    
def fib_top_down(n, fibs):
    if fibs[n] != -1:
      return fibs[n]
      
    if n <= 1:
      fibs[n] = n
    else:
      fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)

    return fibs[n]

def fib_bottom_up(n):
    if n <= 1:
      return n

    fibs = [0] * (n + 1)
    fibs[1] = 1

    for i in range(2, n + 1):
      fibs[i] = fibs[i - 1] + fibs[i - 2]

    return fibs[n]

