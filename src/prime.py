#prime numbers from 1 to 100
# This program generates prime numbers
#! /usr/bin/python

a=range(4,100)
print "1 is a prime number"
print "2 is a prime number"
print "3 is a prime number"
for i in a:
	if((i%2!=0)and(i%3!=0)and(i%5!=0)and(i%7!=0)):
	  print i," is prime number"
