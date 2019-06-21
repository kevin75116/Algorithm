"""
Practice of Quick Sort algorithm.
"""

def partition(l):
    """Partition a list into 2 sub lists.

    :param list l: the original list of numbers
    :return list s: a list of numbers smaller than pivot value
    :return list pivot: a list includes only the pivot value
    :return list g: a list of numbers greater than pivot value
    """
    s, g = [], []
    pivot = [] if len(l) == 0 else l[-1]
    if len(l) not in [0, 1]:
        pivot = l[-1]
        for i in l[:-1]:
            if i > pivot:
                g.append(i)
            elif i <= pivot:
                s.append(i)
    return s, [pivot], g

def partition2(l):
    """Partition a list into 2 sub lists.

    This partition algorithm is a race of two pointers, i and j.
    Pointer i is to keep the index of the smaller value, which is
    compared to the pivot, in the list l. And j is just the index
    of current item in the list l.

    Once if j points to a value smaller than pivot, accumrate i
    and then swap values that pointer i and j point to. Otherwise,
    do nothing and go to next iteration.

    :param list l: the original list of numbers
    :return list s: a list of numbers smaller than pivot value
    :return list pivot: a list includes only the pivot value
    :return list g: a list of numbers greater than pivot value
    """
    i = -1
    pivot = l[-1]  # select the rightmost value as the pivot
    for j, v in enumerate(l[:-1]):
        if v <= pivot:
            i = i + 1
            l[i], l[j] = l[j], l[i]
    return l[:i+1], [pivot], l[i+1:-1]

def quicksort(l):
    if len(l) in [0, 1]:
        return l
    elif len(l) > 1:
        s, p, g = partition(l)
    return quicksort(s) + p + quicksort(g)
    

# Test1
input_list = [2, 1, 9, 9, 7, 5, 0, 3]
expect_out = [0, 1, 2, 3, 5, 7, 9, 9]
print("Pass test1: %s" % (quicksort(input_list) == expect_out))
