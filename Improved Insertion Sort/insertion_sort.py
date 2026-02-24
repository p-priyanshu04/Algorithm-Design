# Swap function to swap two elements in an array
def swap(a,i,j):

    a[i],a[j] = a[j],a[i]

# Insertion sort function
# This is a basic insertion sort that sorts the array in ascending order
def insertion_sort(a):
  
  for i in range(0,len(a)):

    j = i

    while(j > 0 and a[j - 1] > a[j]):
      swap(a,j,j - 1)
      j = j - 1

  return a