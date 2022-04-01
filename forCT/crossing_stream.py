def Search(rocks, end, k):
    rocks.append(end)
    left, right = 0, end

    while left <= right:
        mid = (left+right) // 2

        prev, cnt = 0, 0
        min_d = end

        for rock in rocks:
            d = rock - prev

            if d < mid :
                cnt += 1
            else:
                min_d = min(min_d, d)
                prev = rock
        
        if cnt <= k:
            left = mid + 1
            result = min_d
        else:
            right = mid - 1

    return result
            
L, n, k = map(int, input().split())
A = list(map(int, input().split()))

print(Search(A, L, k))