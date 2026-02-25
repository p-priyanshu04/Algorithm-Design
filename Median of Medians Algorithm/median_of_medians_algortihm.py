import sys

def insertion_sort(a):
    for i in range(0, len(a)):
        j = i
        while j > 0 and a[j-1][0] > a[j][0]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

def find_pivot(a, l, r):
    n = r - l + 1
    if n <= 5:
        insertion_sort(a[l:r+1])
        return a[l + n // 2][0]
    else:
        med_chunk = []
        for i in range(l, r + 1, 5):
            temp = a[i:i + 5]
            insertion_sort(temp)
            med_chunk.append((temp[len(temp) // 2][0], None))
        return find_pivot(med_chunk, 0, len(med_chunk) - 1)

def partition(a, low, high, pivot):
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if a[i][0] >= pivot:
                break
        while True:
            j -= 1
            if a[j][0] <= pivot:
                break
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

def select(a, l, r, i):
    if l == r:
        return a[l][0]
    pivot = find_pivot(a, l, r)
    q = partition(a, l, r, pivot)
    k = q - l + 1
    if i == k:
        return a[q][0]
    elif i < k:
        return select(a, l, q - 1, i)
    else:
        return select(a, q + 1, r, i - k)

def find_median(a):
    n = len(a)
    if n == 0:
        return
    if n % 2 == 1:
        return select(a, 0, n - 1, n // 2 + 1)
    else:
        mid1 = select(a, 0, n - 1, n // 2)
        mid2 = select(a, 0, n - 1, n // 2 + 1)
        return (mid1 + mid2) / 2

file_path = sys.argv[1]
k = int(sys.argv[2])

data = []
with open(file_path, 'r') as f:
    for line in f:
        row = [float(x) for x in line.strip().split()]
        data.append(row)

income = [(data[i][1], i) for i in range(len(data))]
median = find_median(income[:]) 

income = [(abs(income[i][0] - median), income[i][1]) for i in range(len(income))]

select(income, 0, len(income) - 1, k)

print("The IDs are: ")
for val in income[:k]:
    print(int(data[val[1]][0]))