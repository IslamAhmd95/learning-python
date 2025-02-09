"""
What is Multithreading?
Multithreading is a technique that allows a program to run multiple threads (smaller units of a process) at the same time. It’s useful for improving performance when tasks involve waiting, such as downloading files or reading data.

🟢 Key Points:
    Threads share the same memory space.
    Best for I/O-bound tasks (tasks that spend time waiting, not using the CPU).

Python's Global Interpreter Lock (GIL)
    The GIL is a mutex (lock) that ensures only one thread executes Python bytecode at a time.
    It prevents memory corruption but limits Python’s performance for CPU-heavy tasks.
    I/O-bound tasks (file reading, API calls) benefit from multithreading, but CPU-bound tasks (heavy calculations) don’t.
    For CPU-bound tasks, use the multiprocessing module instead of threads.

CPU-Intensive Tasks vs I/O-Intensive Tasks

    CPU-Intensive Tasks

        Why Multithreading Doesn't Work Well:
            The GIL ensures that only one thread can execute Python code at any given moment.
            Even if you have multiple CPU cores, only one thread runs at a time because the GIL restricts parallel execution.
            So, even though tasks might appear to run "concurrently," they are actually taking turns (serially), which leads to inefficiency for CPU-heavy tasks.

        Why Multiprocessing Works Better:
            Each process runs in its own memory space, with its own GIL instance, so processes can truly execute in parallel across multiple CPU cores.
            While processes use more memory and resources than threads, the performance gain for CPU-heavy tasks is worth it.

        This is why multiprocessing is ideal for tasks like:
            Mathematical computations
            Data analysis
            Image or video processing


    I/O-Intensive Tasks

        Why Multithreading Works Well:
            I/O-bound tasks (like reading files or downloading data) spend most of their time waiting for external operations to complete.
            When a thread is waiting for I/O, it releases the GIL, allowing other threads to run while waiting.
            This overlapping makes multithreading efficient for I/O-bound tasks, even though they share resources like memory.

        Why Not Multiprocessing for I/O Tasks?
            Multiprocessing could handle I/O tasks, but creating and managing separate processes (each with its own memory) would add unnecessary overhead for lightweight I/O operations.
            Threads are more lightweight, and their shared memory model is sufficient for handling small tasks like file I/O or network requests.

    Analogy

        CPU-Intensive Tasks:

            Think of a kitchen with one chef (CPU) and multiple workers (threads).

                The chef must oversee every worker’s task, but the GIL (as a strict rule) only lets one worker at a time use the kitchen tools (CPU execution).
                This means workers wait in line instead of working simultaneously, slowing things down.
                Using multiprocessing is like opening separate kitchens (processes), each with its own tools and chef, allowing all workers to cook independently in parallel.

        I/O-Intensive Tasks:

            Think of call center agents (threads) taking customer calls (I/O operations).

                When one agent is waiting for a customer response, they can pause and let another agent handle a different customer.
                Multithreading allows efficient handling of calls because the GIL allows threads to “swap in and out” during waiting periods.

"""
import threading
import time
import requests
import concurrent.futures
import os

# regular way to run function multiple times
def do_something():
    print("Sleeping for 1 second...")
    time.sleep(1)
    print("Done sleeping .")

start = time.perf_counter()  # perf_counter() is like a stopwatch, but it’s super precise and works in fractions of a second, making it great for performance measurement!

do_something()
do_something()  # adding one more second

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds(s)")  # Finished in 2.0 seconds(s)
# function -> one second > done function -> the second function -> one second for the second function -> done the second function -> all done
# the second function can't start until the first function is done, so the time is 2 seconds "1 for each function"


# use threading to run function multiple times

t1 = threading.Thread(target=do_something) # don't use the paranthesis with the function name, we're just passing it not executing it
t2 = threading.Thread(target=do_something)

start = time.perf_counter() 

t1.start() # start the thread
t2.start() # start the thread

t1.join() # wait for the thread to finish
t2.join() # wait for the thread to finish

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds(s)")  # Finished in 1.0 seconds(s)
# function -> one second -> the second function -> one second for the second function -> done all functions -> all done 
# the second function can start executing during the first function execution, so the time is 1 second for both functions


# Multithreading using loops
threads = []
start = time.perf_counter() 
# Create and start 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)


# Wait for all threads to finish
for t in threads:
    t.join()

finish = time.perf_counter()

print(f"All threads finished in {round(finish - start, 2)} second instead of 10 seconds.")


# passing arguments to the function
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping .")

threads = []
start = time.perf_counter() 
# Create and start 10 threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])  # seconds = 1.5
    t.start()
    threads.append(t)


# Wait for all threads to finish
for t in threads:
    t.join()

finish = time.perf_counter()

print(f"All threads finished in {round(finish - start, 2)} seconds instead of 15 seconds.")



# ThreadPoolExecutor
"""
What Is ThreadPoolExecutor?
    ThreadPoolExecutor is a class in Python’s concurrent.futures module that provides an efficient way to manage a pool of threads for executing tasks concurrently. Instead of creating and managing individual threads manually, ThreadPoolExecutor lets you submit tasks to a pool of threads that handle them automatically.

    
It simplifies multithreading by:
    Reusing Threads: Avoids the overhead of creating and destroying threads repeatedly.
    Task Management: Lets you queue tasks and manage their execution.
    Scalability: Allows easy control over the number of threads running in parallel.

    
Why Is It Better Than Using Threads Manually?
    Simplifies Thread Management:
        With manual threading, you must explicitly create, start, and join each thread, which can get complex.
        ThreadPoolExecutor abstracts this complexity and lets you focus on tasks rather than thread lifecycle.

    Thread Reuse:
        Threads are expensive to create and destroy. ThreadPoolExecutor reuses threads from the pool for multiple tasks, reducing overhead.

    Task Submission:
        Provides convenient methods like .submit() and .map() for queuing tasks, making code cleaner and more readable.

    Limits the Number of Threads:
        Allows you to set a maximum number of threads in the pool (max_workers), preventing system resource exhaustion.

    Error Handling:
        Makes it easier to handle exceptions and results from tasks using Future objects, compared to manually managing thread exceptions.

        
When Should You Use ThreadPoolExecutor?
    I/O-Bound Tasks:
        Downloading files.
        Making multiple API calls.
        Reading/writing files.

    Batch Processing:
        Running many lightweight tasks concurrently.

    Avoiding Manual Thread Management:
        If you want clean and efficient multithreading without handling thread creation, joining, or errors manually.

        
Analogy for Better Understanding
    Imagine you run a help desk with multiple support agents (threads):

        Without ThreadPoolExecutor:
            You manually hire, assign tasks, and release agents for every customer. This involves overhead and inefficiency.

        With ThreadPoolExecutor:
            You have a fixed team of agents (thread pool).
            When a customer arrives, you assign them to an available agent.
            Once the agent is done, they’re ready for the next customer.
            This reduces hiring and firing overhead while efficiently managing the workload.
"""


# example
def task(name):
    print(f"Task {name} starting")
    time.sleep(2)
    print(f"Task {name} completed")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # The pool has 3 workers (max_workers=3), so 3 tasks run in parallel.
    # Task "D" waits for a thread to become available.
    executor.submit(task, "A")
    executor.submit(task, "B")
    executor.submit(task, "C")
    executor.submit(task, "D")
    """
    Output:
        Task A starting
        Task B starting
        Task C starting
        Task A completed
        Task B completed
        Task C completed
        Task D starting
        Task D completed
    """


# example
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping ."

start = time.perf_counter() 

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1.5) for _ in range(10)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

finish = time.perf_counter()

print(f"All threads finished in {round(finish - start, 2)} seconds instead of 15 seconds.")


# example with an iterable "secs" 
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping for {seconds}."  # Returns a string indicating the task has completed after sleeping for seconds, "executor.submit" Expects a Return Value
    # We use return instead of print in this context because the result of the do_something function needs to be captured and processed by the calling code (future.result()).

start = time.perf_counter() 

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]  
    results = [executor.submit(do_something, sec) for sec in secs] 

    for future in concurrent.futures.as_completed(results): 
        print(future.result())

finish = time.perf_counter()

print(f"All threads finished in {round(finish - start, 2)} seconds instead of 21 seconds.")
"""
Explanation:

    - concurrent.futures.ThreadPoolExecutor() Creates a thread pool where multiple tasks can run concurrently in separate threads.
    - with ... as executor: Ensures the thread pool is properly managed (threads are created and cleaned up automatically).
    - executor.submit(do_something, sec) Submits the do_something function to the thread pool with sec as an argument.
        Each task (do_something) will be executed in a separate thread.
    - "results" A list of "Future" objects, where each "Future" represents an asynchronous "غير متزامن" execution of a task.
    - concurrent.futures.as_completed(results)
        Iterates over the Future objects as they complete (in the order they finish, not the order they were started).
    - future.result()
        Retrieves the result of the completed task.
        In this case, it fetches the return value of the do_something function.
    - "21 seconds" This is the time it would take if the tasks were executed sequentially (6 + 5 + 4 + 3 + 2 + 1 = 21 seconds). Since tasks run concurrently, the actual time is close to the duration of the longest task (6 seconds).

Notes:

    - The combination of submit() and result() in the concurrent.futures module is conceptually similar to using start() and join() when working with threads in the threading module. Here's how they compare:
    1. submit() vs start()

    submit():
        Submits a task (function) to the ThreadPoolExecutor for execution.
        The task starts running in a separate thread or process (depending on the executor type).
        Returns a Future object, which allows you to interact with the task (e.g., check its status or retrieve its result).

    start():
        Directly starts a thread in the threading module.
        The thread begins executing the target function.
        No built-in mechanism like Future to track the thread's progress or result (though you can use shared variables or other techniques to achieve this).

    2. result() vs join()
    
    result():
        Blocks the calling thread until the task (submitted with submit()) is complete.
        Returns the value that the task's function produces (via return).
        If an exception occurs in the task, calling result() raises the exception.

    join():
        Blocks the calling thread until the thread on which it is called is complete.
        Does not return any value from the thread (you’d have to use shared variables or other techniques to retrieve results).

"""


# using executer map
def square(n):
    return n * n

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(square, [1, 2, 3, 4])

print(list(results))  # Output: [1, 4, 9, 16]



# example
def do_something(seconds):
    print(f"Sleeping for {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping for {seconds}."  # Returns a string indicating the task has completed after sleeping for seconds, "executor.submit" Expects a Return Value

start = time.perf_counter() 

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print(f"All threads finished in {round(finish - start, 2)} seconds instead of 21 seconds.")

"""
Notes:

    submit&as_completed VS map

        - executor.map(do_something, secs)1. executor.submit and as_completed

            How It Works:
                - executor.submit schedules individual tasks for execution and returns a Future object for each task.
                - You can track the status of each task using the Future object.
                - concurrent.futures.as_completed is used to retrieve results as each task completes (not necessarily in the order they were submitted).
            Advantages:
                - Provides fine-grained control over individual tasks.
                - Allows tasks to be processed as they complete, which can be useful when task durations vary significantly.
                - Flexible if you need to handle exceptions or additional task-specific logic for each result.
            Output Order: Results will appear in the order of task completion (not submission order).

        - executor.map

            How It Works:
                - executor.map schedules all tasks at once and blocks until all tasks complete.
                - It automatically collects results and returns them in the same order as the input arguments.
            Advantages:
                - Simpler syntax for mapping a function to a sequence of arguments.
                - Results are automatically returned in the order of input, making it easier if order matters.
                - Suitable for cases where you don't need to handle tasks individually or process them as they complete.
            Output Order: Results will always match the input order, even if tasks complete out of order.
"""


# real world example to donwload images from internet with threadpool 
"""
# the code is commented so that the images are not downloaded
img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

# Record the start time
t1 = time.perf_counter()

# Define the folder name
folder_name = "images"

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Function to download an image
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]  # Extract the unique image identifier
    img_path = os.path.join(folder_name, f'{img_name}.jpg')  # Save in the "images" folder
    with open(img_path, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name}.jpg was downloaded and saved to {folder_name}/')

# Use ThreadPoolExecutor for concurrent downloading
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

# Record the end time
t2 = time.perf_counter()

# Print the total execution time
print(f'Finished in {t2 - t1:.2f} seconds')
"""



"""
Synchronous and Asynchronous are not types of multithreading but rather concepts or modes of execution that describe how tasks are handled in a program. These concepts apply to many areas, including multithreading, multiprocessing, networking, and general programming.


Synchronous Execution
    Definition: In synchronous execution, tasks are executed one at a time, and each task must complete before the next one starts. It follows a strict step-by-step order.
    Analogy: Imagine you’re standing in a line at a single cashier in a grocery store. Each person (task) must finish paying before the next person can start.
    Key Characteristics:
    Blocking: The program waits for each task to finish before moving to the next one.
    Sequential: Tasks are executed in order, and no task overlaps.
    Use Cases: When tasks are dependent on each other or when order and predictability are critical.
    Synchronous Multithreading: Threads execute in a controlled sequence (e.g., thread 1 starts and finishes before thread 2).
    Example:
        import time

        def task1():
            print("Task 1 started")
            time.sleep(2)  # Simulates a 2-second task
            print("Task 1 completed")

        def task2():
            print("Task 2 started")
            time.sleep(1)  # Simulates a 1-second task
            print("Task 2 completed")

        task1()
        task2()

Asynchronous Execution
    Definition: In asynchronous execution, tasks are started without waiting for previous tasks to complete. Multiple tasks can overlap, and the program can handle other tasks while waiting for one to finish.
    Analogy: Imagine the same grocery store, but now there are multiple cashiers. Customers can go to different cashiers simultaneously, so no one waits unnecessarily.
    Key Characteristics:
    Non-blocking: A task can continue working while waiting for another task to finish (e.g., waiting for input/output).
    Concurrent: Multiple tasks can run "at the same time" or appear to do so, depending on the system.
    Use Cases: Networking (e.g., downloading files), handling user input/output in web servers, or running independent tasks concurrently.
    Asynchronous Multithreading: Threads can run concurrently without waiting for one to finish before the other starts.
    Example:
        import asyncio

        async def task1():
            print("Task 1 started")
            await asyncio.sleep(2)  # Simulates a 2-second task
            print("Task 1 completed")

        async def task2():
            print("Task 2 started")
            await asyncio.sleep(1)  # Simulates a 1-second task
            print("Task 2 completed")

        async def main():
            await asyncio.gather(task1(), task2())  # Run tasks concurrently

        asyncio.run(main())


Types of Thread Synchronization
    There are mechanisms used for thread synchronization, which ensures that threads access shared resources in a safe and organized way.

    1. Locks
        A Lock ensures that only one thread can access a specific resource (e.g., a variable or file) at a time.
        It prevents data corruption when multiple threads try to modify the same resource simultaneously.
        Think of it like a bathroom key: only one person can enter at a time. Others must wait for the key to become available.

    2. Semaphores
        A Semaphore is like a counter-based lock. It allows multiple threads to access a resource, but only up to a limit.
        Think of it as a parking lot: it has a limited number of spaces. Once it's full, new cars must wait for a spot to open.
        Use Case: Limit how many threads can perform a task simultaneously.

    3. Condition
        A Condition allows threads to communicate and coordinate with each other.
        Threads can wait for a specific condition to be met before continuing.
        Think of it like traffic lights: cars (threads) wait for the green light (condition) before proceeding.
"""

#  Example of locks

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Acquire lock
            # Without the lock, threads could access counter simultaneously and corrupt the value.
            counter += 1  # Safe access

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Output: 500000 (Correct)


# Example of semaphore

semaphore = threading.Semaphore(2)  # Max 2 threads can access at once

def limited_task(name):
    with semaphore:
        print(f"{name} starts")
        time.sleep(2)
        print(f"{name} ends")

threads = [threading.Thread(target=limited_task, args=(f"Thread-{i}",)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
"""
Output:
    Thread-0 starts
    Thread-1 starts
    Thread-0 ends
    Thread-1 ends
    Thread-2 starts
    ...
"""


# Example of condition

# Shared resource: A list to hold "items" (e.g., books).
items = []

# Condition for threads to communicate.
condition = threading.Condition()

# Producer Function: Adds items to the list.
def producer():
    with condition:  # Acquire the condition's lock.
        print("Producing item")
        items.append("item")  # Add a new "item" (e.g., book).
        condition.notify()  # Notify waiting consumers that an item is ready.

# Consumer Function: Waits for items to be available and then processes them.
def consumer():
    with condition:  # Acquire the condition's lock.
        print("Waiting for item")
        condition.wait()  # Wait until the producer notifies (when an item is available).
        print("Consumed", items.pop())  # Remove and process the "item".

# Create threads for producer and consumer.
threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
"""
Explanation:
    Initial State:
        The items list (shared resource) is empty.
        The consumer thread starts first and tries to consume an item, but the shelf (list) is empty.
    Consumer Waits:
        The consumer thread executes condition.wait().
        This makes it pause and release the lock until the producer thread signals it.
    Producer Adds an Item:
        The producer thread starts and acquires the lock using with condition.
        It adds an item to the items list (e.g., puts a book on the shelf).
        The producer calls condition.notify(), signaling the consumer that an item is available.
    Consumer Resumes:
        The consumer thread wakes up from condition.wait() and acquires the lock again.
        It processes the item by removing it from the list (e.g., takes the book).

Output:
    Waiting for item  # Consumer starts first but waits for an item.
    Producing item    # Producer adds an item.
    Consumed item     # Consumer processes the item after being notified.
"""



"""
Race Condition
    A Race Condition occurs when multiple threads access a shared resource without proper synchronization, causing unpredictable results.
    Think of it as two people writing on the same whiteboard at the same time, leading to confusion.
    By using Locks, Semaphores, or Conditions, we can prevent race conditions by controlling how threads interact with shared resources.
"""
# Example of race condition
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # No lock!

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Output may be incorrect, e.g., 456789
# Fix: Use a lock to ensure synchronization (as shown in the lock example).