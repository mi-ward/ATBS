Practice Questions
1. What is the Unix epoch?
    Jan 1, 1970 UTC

2. What function returns the number of seconds since the Unix epoch?
    time.time()

3. How can you pause your program for exactly 5 seconds?
    time.sleep(5)

4. What does the round() function return?
    A number rounded to the closest integer

5. What is the difference between a datetime object and a timedelta object?
    datetime is a specific moment, a timedelta is a duration

6. Using the datetime module, what day of the week was January 7, 2019?
    Monday

7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?
    threadObj = threading.Thread(target=spam)
    threadObj.start()

8. What should you do to avoid concurrency issues with multiple threads?
    keep variables local to each thread