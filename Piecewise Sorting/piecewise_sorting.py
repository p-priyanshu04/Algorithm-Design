import sys

# Implementing Min Heap for Sorting 
class Min_Heap:
    def __init__(self,arr):
        self.arr = arr
        self.size = len(arr)
        self.build()

    def build(self):
        for i in range(len(self.arr) // 2 - 1,-1,-1):
            self.heapify_down(i)

    def heapify_down(self,i):
        smallest = i
        l = 2*i + 1
        r = 2*i + 2

        if l >= self.size and r >= self.size:
            return
        if l < self.size and self.arr[l][0] < self.arr[smallest][0]:
            smallest = l
        if r < self.size and self.arr[r][0] < self.arr[smallest][0]:
            smallest = r

        if(smallest==i):
            return
        else:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify_down(smallest)

    def push(self,x):
        if self.size == len(self.arr):
            self.arr.append(x)
        else:
            self.arr[self.size] = x
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self,i):
        if(i == 0):
            return
        parent = (i - 1) // 2
        if(self.arr[i][0] < self.arr[parent][0]):
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
            self.heapify_up(parent)

    def pop(self):
        if(self.size == 0):
            return
        
        x = self.arr[0]

        if(self.size == 1):
            self.size -= 1
            return x
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.heapify_down(0) 
        return x

# Reading the file
def read_file(file_path):
    a = []
    with open(file_path, "r") as file:
        for line in file:
            a.append(line)
    
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

# Taking input from command line arguments
f = sys.argv[1]
arr = read_file(f)
i = 0
n = len(arr)
m = int(sys.argv[2])
a = []

while(i < m):
    y = [arr[(n // m) * (i)], i]
    a.append(y)
    i += 1

# Sorting using Min Heap
hp = Min_Heap(a)
id = [1 for i in range(m)]
grp = 0
while(hp.size > 0):
    x = hp.pop()
    grp = x[1]
    if(id[grp] < (n//m)):
        y = [arr[(n // m) * (grp) + id[grp]],grp]
        id[grp] += 1
        hp.push(y)
        
    # Printing the Sorted Output 
    print(x[0])