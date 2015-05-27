#coding=utf-8

__author__ = 'cody'

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

def wordize(numberin):
    #turn the number into a string
    forward = []
    number_word = str(numberin)
    for y in number_word:
        forward.append(y)
    return forward

def ezidrow(number2in):
    backward= []
    numberword = str(number2in)
    for y in range(len(str(number2in)),0,-1):
        n = y-1
        backward.append(numberword[n])
    return backward

def checker(forw,back,num):
    #checks if numbers are the same
    checky= 0
    snum = str(num)
    for x in range(len(snum)):
        if forw[x] == back[x]:
            checky += 1
    return checky
def estimate_time(x):
    est_time = (x * x) / 197600
    qualifier = "seconds"
    if est_time > 60:
        est_time = float(est_time) / 60
        qualifier = "minutes"
    stringy = "%d %s" %(est_time, qualifier)
    return stringy


#global vars
current_high = 0
frame = raw_input("Enter the length of the number to check?")
framenum = int(frame) -1
frame_left = 10 ** framenum
frame_right = (10 **(framenum+1 )) -1
escape = False

#okay = raw_input("it should take about " + estimate_time(frame_right) + ". is that ok?")
#if okay == "n":
#    exit()
print "calculating..."
starttime = time.time()
print frame_left,frame_right
for first_num in range(frame_right,frame_left,-1): # started out going from lowest to highest, then realized it would be quicker to go the other way
    print first_num
    for sec_num in range(frame_right, frame_left,-1):
        print sec_num
        numbers = first_num * sec_num
        print numbers
        forwards= wordize(numbers)
        backwords = ezidrow(numbers)
        #print "forwards:", forwards
        #print "backwards", backwords
        common_length = checker(forwards,backwords,numbers)
        if common_length == len(str(numbers)):
            if numbers> current_high:
                current_high = numbers
                print numbers
    if first_num <sec_num:
       escape = True
       break
            #print current_high
    if escape == True:
        break
stop_time =time.time()
total_time = float(stop_time - starttime)
qualifier = "seconds"
if total_time > 60:
    total_time = total_time / 60
    qualifier = "minutes"
print "%d is the highest number I could find. It is the product of %d and %d It took about %d %s." % (current_high, first_num,sec_num, total_time, qualifier)
