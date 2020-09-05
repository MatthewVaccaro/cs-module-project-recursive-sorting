def merge(a, b):
    # what will be returned once everything is sorted
    finalMergeList = []
    # We need something that will hold each side of the array to increament
    indexA = 0
    indexB = 0
    # We need to loop over both arrays - Base case is if one index is no longer less then the counters
    while indexA < len(a) and indexB < len(b):
        # If a is less append it && inc
        if a[indexA] < b[indexB]:
            finalMergeList.append(a[indexA])
            indexA += 1
        # Append B and Inc
        else:
            finalMergeList.append(b[indexB])
            indexB += 1
    # Its very possible the lists wont append equally -
    # If one list ends early we can extend the rest to the list
    # If the len of a is = to its counter we know its done so extend B
    if len(a) == indexA:
        finalMergeList.extend(b[indexB:])
    # else Extend A
    else:
        finalMergeList.extend(a[indexA:])

    return finalMergeList


def merge_sort(a):
    # If None
    if len(a) <= 1:
        return a

    # Continue to split the array down until it's singles
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    # Once there singles they will run through this code, and continue to get more and more merge
    # Over the course of recurssion
    return merge(left, right)
