"""
Very inefficient sort method
do not use for sort for list larger than 200 items
use quick sort or merge sort instead
"""
def bubble_sort(A):
    # for n element in list
    n = len(A)
    bound = n - 1
    # let i be iterate counter of outer loop
    # set swap to false to detect if swap occurred
    swap = False
    for i in xrange(n - 1):
        new_bound = bound
        for j in xrange(bound):
            if A[j] > A[j+1]:
                swap = True
                A[j+1], A[j] = A[j], A[j + 1]
                new_bound = j
            bound = new_bound
        print "bound is %s" % bound
        print A
        # a sorted list detected
        if swap is False:
            break

    return A

X = [20, 45, 93, 67, 10, 97, 52, 88, 33, 92]
# test for a sorted list
# X = [1, 2, 3, 4, 5, 6]
Y = bubble_sort(X)
print Y
