from random import randint
import time

def selection_sort(A):
    run = 0
    # for n element in list
    # let i be iterate counter of outer loop
    n = len(A)
    for i in xrange(len(A)):

        # let smallest be variable for smaller index
        smallest = i
        # let j be iterate bound of inner loop
        # let x be iterate counter
        # assign i to j as inner loop starts from i
        # prior loop already put i with the smaller value
        j = i
        for x in range(j, n):
            run += 1
            # compare and assign smaller index
            if A[smallest] > A[x]:
                smallest = x
        # inplace swap to move smaller to left most
        A[i], A[smallest] = A[smallest], A[i]
    print "run [%s] of times" % run
    return A

#lst = [4, 9, 7, 12, 101, 12, 101, 6, 5, 3, 1]

#newlist = selection_sort(lst)
#print newlist
X = []
end = 201
for m in xrange(1, end):
    X.append(randint(1, 12023))
start = time.time()
Y = selection_sort(X)
done = time.time()
elapsed = done - start
print(elapsed)
print Y[0]
print Y[len(Y)-1]
print "finished"

# program output
"""
using 2 cores cpu MHz: 3407.994 VM Centos7 4GB memory
In the testing, I ran the sort on 20,000 number
sorting 20K randomized integer from 1 to 12023
The result is very slow
run 200 Million iterations!
Never run this on anything larger than 1000 items
run [200,010,000] of times
15.1821532249
2
12022
finished

Process finished with exit code 0
