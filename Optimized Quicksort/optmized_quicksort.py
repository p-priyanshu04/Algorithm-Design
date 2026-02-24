import random

# Partition function using median of three 
def partition(a,low,high):

    if(high-low>=2):
      random_numbers = random.sample(range(low, high + 1),3)
      x1=random_numbers[0]
      x2=random_numbers[1]
      x3=random_numbers[2]
    else:
      x1=random.randint(low,high)
      x2=random.randint(low,high)
      x3=random.randint(low,high)

    #Computing median
    if(a[x1]>=a[x2] and a[x1]<=a[x3]) or (a[x1]<=a[x2] and a[x1]>=a[x3]):
        pivot=a[x1]
    elif(a[x2]>=a[x1] and a[x2]<=a[x3]) or (a[x2]<=a[x1] and a[x2]>=a[x3]):
        pivot=a[x2]
    else:
        pivot=a[x3]

    i = low - 1
    j = high + 1

    while(True):
        
        while(True):
            i = i + 1
            if(a[i] >= pivot):
                break

        
        while(True):
            j = j - 1
            if(a[j] <= pivot):
                break
        

        if(i>=j):
            return j

        a[i],a[j]=a[j],a[i]

# Insertion sort
def insertion_sort(a,li,ri):
  for i in range(li,ri+1):
    j=i
    while(j>0 and a[j-1]>a[j]):
      a[j],a[j-1]=a[j-1],a[j]
      j-=1
  return a

# Quick sort
def quick_sort(a,li,ri):
    
    if(ri-li>=1304): 
        p = partition(a,li,ri)
        quick_sort(a,li,p)
        quick_sort(a,p+1,ri)
    else :
        insertion_sort(a,li,ri)


import sys

filename = sys.argv[1]

a = []

with open(filename,"r") as f:
    for line in f:
        numbers = line.strip().split()
        for num in numbers:
            a.append(int(num))

quick_sort(a,0,len(a)-1)




 


