"""
Very inefficient sort method
takes 20 seconds to sort 20000 integer
use mergesort or quicksort for larger than 200 elements
"""
def insertion_sort(A):
    run = 0
    # for n element in list
    n = len(A)
    # let i be iterate counter of outer loop
    for i in xrange(n - 1):
        # if left greater than right
        # swap
        if A[i] > A[i + 1]:
            # loop back from left most of list to find the
            # insertion position
            # where left is greater than right
            for j in range(0, i):
                # swap if left greater then right
                if A[j] > A[i + 1]:
                    A[j], A[i + 1] = A[i + 1], A[j]

    return A

X = [20, 45, 93, 67, 10, 97, 52, 88, 33, 92]
Y = insertion_sort(X)
print Y
