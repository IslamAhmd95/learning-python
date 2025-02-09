import multiprocessing 
from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def square_sum(numbers):
    total = sum([num ** 2 for num in numbers])
    print(f"The total square for {numbers=}: {total}")

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

chunk1 = numbers[:5]  
chunk2 = numbers[5:] 

# Create two processes to handle each chunk of numbers
# Process 1 will execute the `square_sum` function for the first chunk
process1 = multiprocessing.Process(target=square_sum, args=(chunk1,))
# Process 2 will execute the `square_sum` function for the second chunk
process2 = multiprocessing.Process(target=square_sum, args=(chunk2,))

# Start both processes
process1.start()  # This starts process1, which begins executing the `square_sum` function for chunk1
process2.start()  # This starts process2, which begins executing the `square_sum` function for chunk2

# Wait for both processes to finish
# This method blocks the main program until the respective process (process1 or process2) completes its execution.
# Without join(), the main program might finish execution before the processes complete their tasks, leading to incomplete results.
process1.join()  # The main program will wait for process1 to complete before proceeding
process2.join()  # The main program will wait for process2 to complete before proceeding
# Once both processes have finished, the program will exit



# example
def do_something():
    print("Starting doing something...")
    time.sleep(1)  # simulate some work
    print("Finished doing something.")

start = time.perf_counter()

processes = []
for _ in range(10):  # Create 10 processes
    # Create a new process that runs the `do_something` function
    p = multiprocessing.Process(target=do_something)
    p.start()  # Start the process
    processes.append(p)  # Add the process to the list for tracking

# Wait for all the processes to finish
for p in processes:
    p.join()  # This ensures that the main program waits for each process to complete

# Record the finish time
finish = time.perf_counter()

# Calculate and display the total time taken
print(f"Finished all processes in {finish - start:0.2f} seconds")  # Finished all processes in ~1 second
"""
Why Does It Finish in ~1 Second Instead of 10 Seconds?
    Processes Run Concurrently:
        Each process is independent and runs in parallel with the others. The do_something function takes 1 second to complete, and all 10 processes execute concurrently (in parallel), not sequentially.
        This means that the time.sleep(1) delay is happening for all processes simultaneously.
    Parallel Execution on Multiple CPU Cores:
        The multiprocessing module creates separate processes, and each process can run on a separate CPU core (if available). Modern systems typically have multiple cores, so the operating system can distribute these processes across available cores.
    Total Time = Maximum Time of a Single Process:
        Since all processes execute in parallel and take approximately 1 second, the total execution time is roughly equal to the duration of the longest individual process, which is 1 second in this case.
"""


"""
What is ProcessPoolExecutor?
    ProcessPoolExecutor is part of the concurrent.futures module in Python. It provides a high-level interface for asynchronously executing functions using multiple processes (similar to Pool in multiprocessing).

It simplifies managing a pool of worker processes with a clean API, allowing you to submit tasks and retrieve results.


Key Methods in ProcessPoolExecutor:
    map(func, iterable):
        Applies the function func to each item in the iterable in parallel.
        Blocking method (waits for all tasks to finish before proceeding).
    submit(func, *args):
        Submits a single task to the pool and returns a Future object.
        Non-blocking (allows you to submit multiple tasks and retrieve results later).
    as_completed():
        Allows iterating over Future objects as they complete.

When to Use ProcessPoolExecutor?
    When you want a cleaner and more intuitive API for managing processes.
    When you need to submit tasks asynchronously and track their progress using Future objects.
    When exception handling and clean-up are important.
"""

# example that demonstrates the use of ProcessPoolExecutor with map
def long_task(n):
    time.sleep(1)  # Simulate a long computation
    return n * n

numbers = [1, 2, 3, 4]

# Using ProcessPoolExecutor
start = time.perf_counter()

with ProcessPoolExecutor() as executor:
    # Submit tasks using map (blocking)
    # Using map: Results are returned in the same order as the input iterable.
    results = list(executor.map(long_task, numbers))

print("Results from ProcessPoolExecutor map:", results)

end = time.perf_counter()
print(f"Finished in {end - start:.2f} seconds")



# example that demonstrates the use of ProcessPoolExecutor with submit and as_completed
start = time.perf_counter()

with ProcessPoolExecutor() as executor:
    # Submit tasks individually
    # Using submit with as_completed: Results may not follow the input order because they are processed as they complete.
    futures = [executor.submit(long_task, n) for n in numbers]
    
    # Collect results as they complete
    results = []
    for future in as_completed(futures):
        results.append(future.result())

print("Results from ProcessPoolExecutor submit:", results)

end = time.perf_counter()
print(f"Finished in {end - start:.2f} seconds")




# example of using multiprocessing.Pool to demonstrate its functionality, along with an explanation of how it works.

def square(n):
    time.sleep(1)  # Simulate some computation
    return n * n

numbers = [1, 2, 3, 4, 5]

start = time.perf_counter()

# Create a Pool with 4 processes
with multiprocessing.Pool(processes=4) as pool:
    # Use the map function to apply `square` to each element in `numbers`
    results = pool.map(square, numbers)

end = time.perf_counter()

print("Results:", results)
print(f"Finished in {end - start:.2f} seconds")
"""
Output:
    Results: [1, 4, 9, 16, 25]
    Finished in 1.01 seconds

explanation:
    The Pool is created with 4 worker processes.
    pool.map(square, numbers) splits the input list numbers into chunks and assigns each chunk to a worker process.
    Each process applies the square function to its chunk in parallel.
    Since time.sleep(1) simulates a 1-second delay for each calculation, all tasks finish in roughly 1 second (as tasks run in parallel).
"""


# Example: Using Pool.apply
# apply is used to run a single function in one of the pool's processes.
start = time.perf_counter()

with multiprocessing.Pool(processes=4) as pool:
    # Use apply to run a single task
    result = pool.apply(square, (5,))
    print("Result from apply:", result)

end = time.perf_counter()

print(f"Finished in {end - start:.2f} seconds")
"""
Output:
    Result from apply: 25
    Finished in 1.00 seconds

explanation:
    pool.apply sends the square function with input 5 to one of the worker processes.
    Unlike map, apply handles only one task at a time.
    The computation takes 1 second because it is a single task.
"""


# Example: Using Pool.apply_async
# apply_async is non-blocking and allows submitting multiple tasks without waiting for one to complete.
start = time.perf_counter()

with multiprocessing.Pool(processes=4) as pool:
    # Use apply_async to submit tasks asynchronously
    results = [pool.apply_async(square, (n,)) for n in [1, 2, 3, 4]]

    # Collect results
    output = [result.get() for result in results]
    print("Results from apply_async:", output)

end = time.perf_counter()

print(f"Finished in {end - start:.2f} seconds")
"""
Output:
    Results from apply_async: [1, 4, 9, 16]
    Finished in 1.01 seconds

explanation:
    apply_async submits the square function with different inputs (1, 2, 3, 4) to the pool of worker processes.
    It does not block the main program, so all tasks are sent to workers immediately.
    .get() is used to retrieve the result of each task.
"""