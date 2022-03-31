import math
import time

B = []
C = []

for i in range(190000, 190100):
    B.append(i)

for i in range(-190000, 190000):
    C.append(i)

A = B + C
#A = list(map(int, input().split()))

#O(n)
start = time.time()



cnt = 0

for i in range(len(A)-1, -1, -1):
    if A[i-1] > A[i]:
        cnt += 1
        break
    else:
        cnt += 1

if cnt == len(A):
    cnt = 0

print(cnt)

end = time.time()
print(f"{end - start:.5f} sec")

#O(logn)
"""
def search(A, start, end):
    start_i = start
    end_i = end
    mid_i = (start + end) // 2

    if start_i == end_i:
        return start
    
    if end_i - start_i == 1:
        if A[start_i] > A[end_i]:
            return end_i
        elif A[start_i] < A[end_i]:
            return start_i

    if A[start_i] < A[end_i]:
        return start

    if A[start_i] > A[mid_i]:
        search(A, start_i, mid_i)
    elif A[start_i] < A[mid_i]:
        search(A, mid_i+1, end_i)

first_i = search(A, 0, len(A)-1)

cnt = len(A) - first_i

if first_i == 0:
    cnt = 0
    print(cnt)
else:
    print(cnt)
"""




