# Binary Search for insertion position
def binarySearch(arr, x, end):

    l,r = 0, end

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return l

# Improved Insertion Sort
# This function sorts an array in ascending order using a improved insertion sort algorithm.
def improved_insertion_sort(a):

    for i in range(0,len(a) - 1,2):
        x1,x2=max(a[i],a[i + 1]),min(a[i],a[i + 1])

        pos_x1=binarySearch(a,x1,i - 1)
        
        j = i + 1

        while j-2 >= pos_x1 :
            a[j] = a[j - 2]
            j = j - 1

            
        a[pos_x1 + 1] = x1
        a[pos_x1] = x2

        pos_x2 = binarySearch(a,x2,pos_x1 - 1)

        j = pos_x1

        while j - 1 >= pos_x2:
            a[j] = a[j - 1]
            j= j - 1

        a[pos_x2] = x2
    # To handle the last element, if the length of the array is odd 
    if(len(a) % 2 == 1):

      pos_x2 = binarySearch(a,a[len(a) - 1],len(a) - 2)

      j = len(a)-1

      while j > 0 and j > pos_x2:
          a[j] = a[j - 1]
          j = j - 1

    return a