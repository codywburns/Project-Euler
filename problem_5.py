#__author__ = 'Cody'
'''
PROBLEM 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

The smallest number that can be evenly divided by each number between 1 and 20 is 232792560. It took 42.2259998322 Seconds to figure this out.
'''
def human_time(xtime):
    qualifier = " Seconds"
    if xtime >= 60:
        xtime = float(xtime / 60)
        qualifier = " Minutes"
    human = str(xtime) + qualifier
    return human

import time

max_number = raw_input('What is the largest number?')
start_timer = time.time()
candid_number = 1
#super_max = max_number**max_number
calc = True
test_number = int(max_number)

while calc == True:
     test_number += int(max_number)
     #print test_number
     if test_number % 2 == 0 and test_number % 3 == 0 and test_number % 7 == 0:
        for x in range(int(max_number),0,-1):
            #print x
            #time.sleep(1)
            if test_number % x != 0:
                break
            elif x == 1:
                if candid_number < test_number:
                    candid_number= test_number
                    calc = False
total_time = human_time(time.time()-start_timer)
print "The smallest number that can be evenly divided by each number between 1 and %d is %d. It took %s to figure this out."% (int(max_number),candid_number,total_time)
