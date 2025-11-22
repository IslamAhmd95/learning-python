"""
What is Async IO?
    Async IO (Asynchronous Input/Output) is a programming model that allows you to execute multiple I/O-bound tasks concurrently without using multiple threads or processes. Instead of blocking the execution of a task while waiting for I/O operations (like reading/writing files, network requests, etc.), the program can "pause" the task and switch to another while waiting for the I/O operation to complete.

    In Python, the asyncio module provides tools to use Async IO programming.

    
async io vs threads vs processes ?

    1. Async IO: Best for Lightweight, I/O-Bound Tasks
        When to Use:
            When the program spends most of its time waiting for I/O operations (e.g., network requests, file reads/writes, database queries).
            Examples:
            Web servers handling many simultaneous client requests.
            Fetching data from APIs or web scraping.
            Chat applications or real-time notifications.
        Why Async IO?:
            It is lightweight and scales well for I/O-bound tasks.
            Avoids the overhead of threads or processes (e.g., context switching, memory usage).
            Single-threaded but can handle thousands of tasks concurrently.

    2. Threads: Best for Moderate, Mixed, or Blocking Tasks
        When to Use:
            When tasks are partially CPU-bound but not very heavy.
            When you need to run blocking I/O operations in parallel (e.g., working with non-async libraries or legacy code).
            Examples:
            Running multiple blocking I/O tasks (e.g., downloading multiple large files).
            Background tasks that don’t need real-time responses.
            Handling simultaneous user sessions in GUI applications.
        Why Threads?:
            Threads are great for blocking operations or when async is not an option.
            Suitable for workloads that involve a mix of CPU and I/O but are not heavily CPU-bound.
            Python threads share memory, so you can easily share data between them.
            Caution: Python threads are affected by the Global Interpreter Lock (GIL), so they do not run truly in parallel for CPU-bound tasks.

    3. Processes: Best for Heavy, CPU-Bound Tasks
        When to Use:
            When tasks involve intensive computation and need full CPU power (e.g., image processing, machine learning, data analysis).
            When true parallelism is required to utilize multiple CPU cores.
            Examples:
            Video processing, encryption, or compression.
            Running CPU-intensive simulations or computations.
            Machine learning model training.
        Why Processes?:
            Bypasses the GIL, so processes can achieve true parallelism on multi-core systems.
            Each process has its own memory space, which makes them isolated but requires more memory and IPC (Inter-Process Communication) for data sharing.
            

Blocking and Non-Blocking:
    Blocking:
        A task stops and waits for something to finish (e.g., waiting for data from a database or a file to download).
        While waiting, the program (or thread) can’t do anything else.
        Example:
        Imagine you're stuck in a traffic jam (blocking). You can’t move until the cars ahead of you move.
    Non-Blocking:
        A task does not stop the program while waiting. It schedules something else to run in the meantime.
        When the result of the task is ready, it resumes where it left off.
        Example:
        You’re in a drive-thru. After placing your order, instead of waiting in line, you drive to a pickup spot and do something else (like answering messages) while waiting for your food.
            

Why Use Threads for Blocking?
    Multithreading allows you to deal with blocking tasks by running multiple threads in parallel. If one thread is blocked (e.g., waiting for a file to download), other threads can continue running.

    Correct Understanding:
    Multithreading provides separate lightweight threads to handle blocking tasks.
    Example:
    If one thread is waiting for a file to download, another thread can process a user request simultaneously.

    
Async IO and Non-Blocking
    Async IO uses one thread and relies on non-blocking operations to handle multiple tasks. Instead of blocking, tasks "pause" themselves and let the event loop run other tasks until the paused one can resume.

    Correct Understanding:
    Async IO is a smart, single-threaded approach to handle non-blocking tasks (e.g., network requests).
    It is lightweight because it doesn’t need multiple threads or the overhead of context switching.


How Does Multithreading Handle Waiting Tasks?
    Multithreading Example (Blocking in Threads):
        Imagine you have two chefs (threads):
            Chef 1 is boiling pasta.
            Chef 2 is chopping vegetables.
        If Chef 1 finishes first, Chef 2 keeps working independently.
        However:
            Each thread is blocking within itself (e.g., Chef 1 waits for pasta water to boil, but Chef 2 is unaffected).
            Threads can run at the same time, but they are independent.
            If you run a CPU-heavy task, the threads may still slow each other down because of the GIL in Python.


Async IO Example (Non-Blocking Tasks):
    Imagine you have one chef who is multitasking:
        The chef sets a timer for boiling pasta and starts chopping vegetables.
        When the timer rings, the chef switches back to the pasta.
        The chef constantly switches between tasks but never waits idly.
    The tasks share the same thread and are paused/resumed as needed.
    Async IO depends on non-blocking operations to allow efficient multitasking.
                        

Key Difference Between Threads and Async IO
Multithreading:
    Multiple tasks can run at the same time because there are multiple threads.
    Each thread may still block itself (e.g., waiting for a file or a network response).
    Useful for tasks that are blocking or don’t support async/await.
Async IO:
    Tasks run on one thread, but they don’t block the thread.
    Instead of waiting, tasks "pause" themselves and let the event loop schedule something else to run.
    Async IO is more efficient for lightweight, I/O-bound tasks.

    
What is the Event Loop?
    The event loop is the core of the Async IO framework. It is responsible for managing and executing asynchronous tasks.

    How it works:
        The event loop maintains a queue of tasks to run.
        When a task involves an I/O operation (e.g., a network request), the event loop pauses the task and moves it to the waiting state.
        While waiting for the I/O operation to complete, the event loop picks another task from the queue and starts executing it.
        Once the I/O operation is complete, the paused task resumes from where it left off.
        Think of the event loop as a "task manager" that ensures no task blocks the main thread for too long.

    Why use the Event Loop?
        It allows efficient management of tasks without requiring multiple threads or processes.
        Enables writing concurrent code in a simple, readable, and linear style.


What is a Coroutine Function?
    A coroutine function is a special type of Python function defined using the async def keyword. When called, it does not execute immediately but instead returns a coroutine object, which represents a future task to be run.
    Coroutine functions can be paused and resumed using await expressions.
    Key Features of Coroutines:
        Non-blocking: Can await other asynchronous operations without blocking the event loop.
        Awaitable: You can use the await keyword to pause execution and wait for a coroutine to complete.


"""
import asyncio
import time

# example
async def say_hello():
    print("Hello, world!")
    await asyncio.sleep(1)  # Pause here for 1 second
    print("Goodbye, world!")

# This doesn't execute the function; it creates a coroutine object
coroutine = say_hello()

# Run the coroutine in an event loop
asyncio.run(coroutine)
"""
Output:
    Hello, world!
    Goodbye, world!
"""


# example
async def main():
    print("Hello, World!")

print(main())  # <coroutine object main at 0x72b85b1e5a80>

# start the event loop and run the coroutine
asyncio.run(main())  # Hello, World!



# example

# Define an asynchronous function that simulates fetching data.
async def fetch_data(delay):
    print("Fetching data...") 
    await asyncio.sleep(delay)  # Simulates an I/O-bound task (e.g., downloading a file) by pausing for 'delay' seconds.
    print("Data fetched.") 
    return {"data": "Some data"} 

# Define the main coroutine that coordinates the async operations.
async def main():
    print("Starting the main coroutine...")

    # Create a coroutine object from fetch_data(2). 
    # This does NOT start executing fetch_data yet.
    task = fetch_data(2)  

    # 'await' tells the event loop to run the fetch_data coroutine.
    # It pauses this main coroutine until fetch_data completes.
    result = await task  

    # Prints the result returned from fetch_data after it finishes.
    print(f"Received result: {result}")  
    print("Main coroutine finished.")

# Run the main coroutine using asyncio.run().
asyncio.run(main())

"""
Output:
    Starting the main coroutine...
    Fetching data...
    Data fetched.
    Received result: {'data': 'Some data'}
    Main coroutine finished.

Notes from the example above:

    task = fetch_data(2)
        the function fetch_data is not executing yet. Instead, a "coroutine object" is created, which the event loop will execute later when you await it.
        Think of it like this: You’ve written down an order in a task queue (but the chef hasn’t started cooking yet).
    result = await task
        The await keyword tells the event loop to start running the coroutine (i.e., execute the fetch_data function).
        The event loop pauses the main() coroutine here until the fetch_data coroutine completes.
        While waiting, the event loop can perform other tasks (if any).
        Once fetch_data finishes, the result (a dictionary {"data": "Some data"}) is returned and assigned to the result variable.
        Analogy:
            You finally tell the chef to start cooking. Once the chef finishes (2 seconds later in this case), they hand you the completed dish (the result).
"""


# example

# Define an asynchronous function that simulates fetching data.
# This code is asynchronous, but it's not concurrent because we are awaiting one task at a time.
# It isn't truly synchronous because it's using asynchronous await calls. It just doesn't take advantage of concurrency because of the sequential await.
async def fetch_data(delay, id):
    print("Fetching data...id=", id) 
    await asyncio.sleep(delay)
    print("Data fetched...id=", id) 
    return {"data": "Some data", "id": id} 

# Define the main coroutine that coordinates the async operations.
async def main():
    # Create a coroutine objects
    # This does NOT start executing fetch_data yet.
    task1 = fetch_data(2, 1) 
    # 'await' tells the event loop to run the fetch_data coroutine.
    # It pauses this main coroutine until fetch_data completes.
    result = await task1  
    # Prints the result returned from fetch_data after it finishes.
    print(f"Received result: {result}")  

    task2 = fetch_data(2, 2) 
    # 'await' tells the event loop to run the fetch_data coroutine.
    # It pauses this main coroutine until fetch_data completes.
    result = await task2 
    # Prints the result returned from fetch_data after it finishes.
    print(f"Received result: {result}")   

start = time.perf_counter()
# Run the main coroutine using asyncio.run().
asyncio.run(main())
# task2 does not run during task1's waiting time because you explicitly await task1 before even creating task2. This ensures the tasks execute sequentially.
finish = time.perf_counter()
print(f"Running in {round(finish - start, 2)} seconds")  # 4 seconds
"""
Task 1 runs, finishes, then Task 2 starts.
Total time = task1 time + task2 time = 4 seconds.


Why it's not concurrent:
    You’re awaiting each task sequentially, so the second task doesn't even get created until the first one finishes.
    No overlap of execution between tasks occurs.
"""



# example

# This is asynchronous and concurrent, which means the tasks are created and run simultaneously
async def fetch_data(delay, id):
    print("Fetching data...id=", id) 
    await asyncio.sleep(delay)
    print("Data fetched...id=", id) 
    return {"data": "Some data", "id": id} 

async def main():
    # create tasks for running coroutine concurrently
        # This schedules each fetch_data coroutine to run concurrently.
        # These tasks start executing right away in the background.
        # The event loop switches between them while they are waiting (e.g., during asyncio.sleep).
    task1 = asyncio.create_task(fetch_data(2, 1))  # Task starts running immediately
    task2 = asyncio.create_task(fetch_data(1, 2))  # Task starts running immediately
    task3 = asyncio.create_task(fetch_data(3, 3))  # Task starts running immediately

    # await task1: Waits for task1 to complete. While waiting, the event loop can run other tasks (task2, task3).
    # await task2: Waits for task2 to complete. If it's already finished (because it had the shortest delay), this returns instantly.
    # await task3: Waits for task3 to complete. The same principle applies.
    result1 = await task1  # Waits for task1 to finish, but other tasks keep running
    result2 = await task2  # Waits for task2 to finish (likely already done by now)
    result3 = await task3  # Waits for task3 to finish (likely last to complete)

    print(result1, result2, result3)

start = time.perf_counter()

# Run the main coroutine using asyncio.run().
asyncio.run(main())

finish = time.perf_counter()
print(f"Running in {round(finish - start, 2)} seconds")  # 3 seconds

"""
Why it's concurrent:
    All tasks are created at once using asyncio.create_task(), which tells the event loop to start running them simultaneously.
    While one task is "paused" (e.g., waiting during await asyncio.sleep), the event loop switches to another task.
    Their delays overlap, saving time.

Result:
    Total runtime = time of the longest task (e.g., max(2, 1, 3) = 3 seconds).
"""


# example
# A more simple way to run the tasks concurrently
async def main():
    # You don’t need to manually create tasks with asyncio.create_task and then await them individually.
    # gather handles everything for you.
    results = await asyncio.gather(fetch_data(2, 1), fetch_data(1, 2), fetch_data(3, 3))

    for result in results:
        print(result)

start = time.perf_counter()

# Run the main coroutine using asyncio.run().
asyncio.run(main())

finish = time.perf_counter()
print(f"Running in {round(finish - start, 2)} seconds")  # 3 seconds



# example
async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for id, delay in enumerate([2, 1, 3], start=1):  # [(1, 2), (2, 1), (3, 3)]
            task = tg.create_task(fetch_data(delay, id))
            tasks.append(task)

    # after the task group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(result)

start = time.perf_counter()

# Run the main coroutine using asyncio.run().
asyncio.run(main())

finish = time.perf_counter()
print(f"Running in {round(finish - start, 2)} seconds")  # 3 seconds
"""
How the Code Works
    Creating Tasks with asyncio.TaskGroup:
        A TaskGroup is a new feature (introduced in Python 3.11) that provides a safer and cleaner way to manage multiple tasks running concurrently.
        Inside the TaskGroup, each task is created with tg.create_task(...), which ensures the tasks are managed by the TaskGroup.
    Storing Tasks:
        Each task created is added to the tasks list, allowing you to access their results after all tasks are completed.
    Waiting for Completion:
        The async with block ensures that all tasks in the TaskGroup are completed before the program continues. If any task fails, the TaskGroup handles cleanup and cancels other tasks automatically.
    Retrieving Results:
        After the TaskGroup finishes, the task.result() method is used to retrieve the result of each task. This is possible because tasks store their return values.

        
Why TaskGroup Might Be Better than asyncio.gather
    Better Error Handling:
        If one task fails, TaskGroup automatically cancels all other tasks and ensures proper cleanup. This avoids leaving dangling or unfinished tasks, making it safer for managing errors in concurrent code.
        In contrast, asyncio.gather requires extra handling for errors; otherwise, it may leave some tasks running even after an error occurs.
    Cleaner Code:
        TaskGroup uses an async with block to group tasks, making it clear when tasks are created, managed, and awaited. It provides a structured way to define concurrent work.
    Explicit Task Management:
        With TaskGroup, you explicitly create tasks using tg.create_task(). This provides more control and makes it easier to track which tasks are being managed.
        In asyncio.gather, you pass coroutines directly, which may feel less structured.
    Automatic Cleanup:
        When the TaskGroup block ends, all its tasks are guaranteed to finish or be cancelled. This makes it safer, especially in larger programs where tasks might otherwise linger.
    Future-Proof and Recommended:
        Since TaskGroup is newer and designed to address shortcomings of asyncio.gather, it's the recommended approach for managing tasks in modern Python codebases.

Performance Comparison
    The efficiency of TaskGroup and asyncio.gather is almost the same in terms of raw speed because both run tasks concurrently using the same event loop. However, TaskGroup is "better" because it makes your code more robust and easier to debug.
        For example:
            With TaskGroup: If one task raises an error, all other tasks are immediately cancelled.
            With asyncio.gather: If one task raises an error, by default the others are not cancelled unless you explicitly handle it.
"""



"""
What is a Future?
    A Future in Python is an object that represents a result that hasn’t been computed yet but will be available in the future. It’s like a placeholder for a value that will eventually be produced by some asynchronous task.
    Think of it as an empty box:
        At first, the box is empty.
        Eventually, some task puts a value in the box (or marks it as failed with an error).
        You can check the box later to get the value (or the error).

How Futures Work
    A Future starts "pending."
        No result is available yet.
    When a task finishes:
        The Future is resolved (if successful) or rejected (if an error occurs).
    You can "await" a Future to pause until it’s resolved.
"""

# example
async def set_future_value(future, delay):
    print(f"Task: Waiting for {delay} seconds to set the result...")
    await asyncio.sleep(delay)  # Simulate some async work
    future.set_result("Result is ready!")  # Set the result of the Future
    print("Task: Future result set.")

async def main():
    # Create a Future object
    my_future = asyncio.Future()

    # Start an async task to set the Future's result
    asyncio.create_task(set_future_value(my_future, 2))

    print("Main: Waiting for the Future to be resolved...")
    # Await the Future (wait for it to get a result)
    result = await my_future
    print(f"Main: Got result from Future: {result}")

# Run the event loop
asyncio.run(main())

"""
Explanation of the Code:
    asyncio.Future():
        Creates a Future object called my_future. At this point, it’s empty and "pending."
    set_future_value Coroutine:
        Simulates some async work using await asyncio.sleep(delay).
        After 2 seconds, it sets the result of the Future using future.set_result("Result is ready!").
    asyncio.create_task(set_future_value(my_future, 2)):
        Starts the set_future_value coroutine in the background. It will eventually set the result of my_future.
    await my_future:
        Pauses the main() coroutine until the Future has a result. Once my_future is resolved, it retrieves the result and continues.

Output:
    Main: Waiting for the Future to be resolved...
    Task: Waiting for 2 seconds to set the result...
    Task: Future result set.
    Main: Got result from Future: Result is ready!

Analogy:
    Imagine a pizza delivery system:
        Future: The receipt you get when you place an order (it represents the pizza you’ll receive later).
        Task: The delivery process (cooking and delivering the pizza).
        Await: Waiting at the door for the delivery to arrive.
        set_result(): The moment the delivery person hands you the pizza

Key Points to Note:
    The Future starts as "pending" and becomes "done" when set_result() is called.
    await my_future pauses the main coroutine until the Future is resolved.
    Futures are low-level constructs and are often managed automatically by tools like asyncio.create_task() or asyncio.gather().
"""



"""
What Is Synchronization?
    Synchronization ensures that multiple tasks (or threads) work together properly without interfering with each other, especially when they:
        Access shared resources (like variables, files, or databases).
        Depend on specific conditions or events to happen before they can proceed.
    Without synchronization, you could encounter issues like:
        Race conditions: Multiple tasks accessing shared data simultaneously, causing unpredictable results.
        Deadlocks: Tasks waiting indefinitely for each other to release resources.
        Incorrect execution order: Tasks running at the wrong time, breaking logical dependencies.

        
How Lock, Semaphore, and Event Help With Synchronization
    1. Lock (Mutual Exclusion)
        Relation to Synchronization:
            Lock ensures mutual exclusion, meaning only one task can access a shared resource at a time.
        Use:
            When multiple tasks might read/write to a shared resource (e.g., updating a bank balance or writing to a file).
        Synchronization Effect:
            Prevents race conditions by allowing only one task to modify the resource at a time.
        Example: 
            Imagine you have one bathroom (shared resource). A lock is like the key—only one person can use the bathroom at a time, and others wait until the key is returned (lock released).

    2. Semaphore (Limited Access)
        Relation to Synchronization: 
            Semaphore limits how many tasks can access a shared resource simultaneously.
        Use: 
            When you have a shared resource that can handle a limited number of tasks at once (e.g., a server allowing only 10 simultaneous connections).
        Synchronization Effect: 
            Avoids resource exhaustion by controlling the number of tasks accessing the resource.
        Example: 
            Think of a restaurant with 5 tables (shared resource). A semaphore ensures that only 5 groups of people (tasks) can sit at the tables at any time. If all tables are full, new customers must wait for someone to leave.

    3. Event (Coordination/Signaling)
        Relation to Synchronization: 
            Event coordinates tasks "تنسق المهام" by allowing one task to signal others when it's time to proceed.
        Use: 
            When some tasks depend on a signal or condition to continue (e.g., workers waiting for a "start" signal).
        Synchronization Effect: 
            Synchronizes task execution order by pausing tasks until the required signal is given.
        Example: 
            Imagine runners (tasks) waiting at the start line. An event is like the starting gun—the runners don’t move until the gun fires (event is set).

Summary of Syntax:
    Lock: asyncio.Lock() + async with lock:
    Semaphore: asyncio.Semaphore(limit) + async with semaphore:
    Event: asyncio.Event() + event.wait() / event.set()
"""

# Lock example

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = asyncio.Lock()

    async def deposit(self, amount):
        print(f"Trying to deposit {amount}")
        async with self.lock:  # Acquire the lock
            print(f"Depositing {amount}")
            await asyncio.sleep(1)  # Simulate some delay
            self.balance += amount
            print(f"New balance: {self.balance}")

async def main():
    account = BankAccount()

    # Two concurrent deposits
    await asyncio.gather(
        account.deposit(100),
        account.deposit(200)
    )

asyncio.run(main())

"""

Output:
    Trying to deposit 100
    Depositing 100
    Trying to deposit 200
    New balance: 100
    Depositing 200
    New balance: 300

Explanation:
    The lock ensures only one deposit happens at a time.
    Without the lock, both tasks might modify self.balance simultaneously, causing errors.

"""

# Semaphore example

async def download_file(semaphore, file_id):
    async with semaphore:  # Acquire a "slot"
        print(f"Downloading file {file_id}...")
        await asyncio.sleep(2)  # Simulate download
        print(f"File {file_id} downloaded.")

async def main():
    semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent downloads

    # Start multiple download tasks
    tasks = [download_file(semaphore, i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
"""
Output:
    Downloading file 0...
    Downloading file 1...
    File 0 downloaded.
    Downloading file 2...
    File 1 downloaded.
    Downloading file 3...
    File 2 downloaded.
    Downloading file 4...
    File 3 downloaded.
    File 4 downloaded.

Explanation:
    Only 2 downloads happen at the same time because of the Semaphore.
    When one finishes, another can start.

"""


# Event example

import asyncio

async def worker(event, worker_id):
    print(f"Worker {worker_id} is waiting for the signal...")
    await event.wait()  # Wait for the event to be set
    print(f"Worker {worker_id} received the signal and started!")

async def main():
    event = asyncio.Event()

    # Start worker tasks
    workers = [worker(event, i) for i in range(3)]
    task = asyncio.gather(*workers)

    print("Preparing signal...")
    await asyncio.sleep(2)  # Simulate some preparation time
    print("Sending signal!")
    event.set()  # Set the event to signal workers

    await task

asyncio.run(main())

"""
Output:
    Worker 0 is waiting for the signal...
    Worker 1 is waiting for the signal...
    Worker 2 is waiting for the signal...
    Preparing signal...
    Sending signal!
    Worker 0 received the signal and started!
    Worker 1 received the signal and started!
    Worker 2 received the signal and started!

Explanation:
    event.wait(): Workers wait until the event is signaled.
    event.set(): Signals all waiting workers to proceed.
"""