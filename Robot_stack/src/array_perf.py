'''
Created on 22 Jul 2017

@author: annub
'''
from src.Stack import *
import time
import matplotlib.pyplot as plt

# Create an array that will contain running times.
running_times = []

# Increase size of n in increments of 1000 from 0-3000 - you can adjust the upper bound if needed.
for n in range (0,100, 10):
    # Create set object named s.
    s = stack(100)
    
    # Add n elements to the set,nothing is being timed at this point, we are just adding N elements to our set for each experiment.
    for i in range(n):
        s.pushing(i)

    start = time.time()

    # Uncomment methods one at a time in order to time them individually.
    #s.is_empty()
    #s.size()
    s.pushing('a')
    #s.remove(0)

    end = time.time()

    run_time = end - start
    running_times.append(run_time)

# Plot the running times
plt.plot(running_times, 'bx')
plt.xlabel('Size of N (x 1000)')
plt.ylabel('Time')
plt.show()