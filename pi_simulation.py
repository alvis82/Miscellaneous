#!/usr/bin/env python

import math
import random

# This method is based on the fact that given a circle with radius r = 1
# inscribed within a square, the ratio of the area of the circle to the area of
# the square is pi/4. Then if we could compute ratio, then we could multiple it
# by 4 to obtain pi. So this method is to simulate picking lattice points in the
# square and count how many of them lie inside the circle. Then pi is
# approximated by 4 times the percentage of points inside the circle.
# The time complexity of this method is O(n^2) and space complexity is O(1).
# The performance of this method is bad. When n is small, the precision of pi is
# bad. When n grows, the precision grows as well but the time used increases
# much faster due to the quadratic time complexity.
def pi_simulation(n):
    if n < 0:
        raise ValueError("n must be positive.")

    count = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x ** 2 + y ** 2 <= n ** 2:
                count += 1

    return 4 * count / float((n + 1) ** 2)

# This method is also called Monte Carlo Method. It is a statistical simulation
# method which utilize a sequences of random numbers to perform the simulation.
# The time complexity is O(n) and the space complexity is O(1). The performance
# of this method is much better than the above one. It can provide more precise
# result even when n is small.
def pi_simulation_by_random(n):
    if n < 0:
        raise ValueError("n must be positive.")

    count = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1: count += 1
    return 4 * count / float(n)

if __name__ == '__main__':
    print "Calculate pi by simulation:"
    print "pi_simulation (n = 10):", pi_simulation(10)
    print "pi_simulation (n = 100):", pi_simulation(100)
    print "pi_simulation (n = 1000):", pi_simulation(1000)
    print "pi_simulation (n = 2000):", pi_simulation(2000)
    print "pi_simulation (n = 2000):", pi_simulation(5000)
    print
    for i in range(5):
        print "pi_simulation_by_random (n = 100):", \
            pi_simulation_by_random(100)
    for i in range(5):
        print "pi_simulation_by_random (n = 1000):", \
            pi_simulation_by_random(1000)
    for i in range(5):
        print "pi_simulation_by_random (n = 10000):", \
            pi_simulation_by_random(10000)
