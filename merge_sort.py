def merge_sort(ori):
    left, right = ori[:len(ori)/2], ori[len(ori)/2:]
    if len(left) > 1 or len(right) > 1:
        left, right = merge_sort(left), merge_sort(right)
    return merge_lists(left, right)
    
def partition(ori):
    return ori[:len(ori)/2], ori[len(ori)/2:]
    
def merge_lists(list1, list2):
    s = list()
    l1, l2 = list(list1), list(list2)
    while True:
        if not l1 or not l2:
            break
        if l1[0] <= l2[0]:
            s.append(l1[0])
            l1.remove(l1[0])
        elif l1[0] > l2[0]:
            s.append(l2[0])
            l2.remove(l2[0])
    return s + l1 + l2


ori = [2, 1, 9, 9, 7, 5, 0, 3]
print(merge_sort(ori))
