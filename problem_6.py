__author__ = 'Cody'

import time

max_number = raw_input(" What is the largest number?")
start_time = time.time()
sos = 0
sumsos = 0

for x in range(1,int(max_number)+1):
    sos += x**2
for x in range(1,int(max_number)+1):
    sumsos += x
    newsos = sumsos**2
end_time = float(time.time() -start_time)
answer = newsos - sos
print " The  difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is %s. It took %d"% (answer,end_time)
