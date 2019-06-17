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
    if len(l) == 0:
        return [], [], []
    elif len(l) == 1:
        return [], l[-1], []
    else:
        s, g = [], []
        pivot = l[-1]
        for i in l[:-1]:
            if i > pivot:
                g.append(i)
            elif i <= pivot:
                s.append(i)
        return s, [pivot], g


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
