import sys
input = sys.stdin.readline

n = int(input())

heap = [0] * (n + 1)

def abs(a):
    if a >= 0:
        return a
    else:
        return -a

def append(i, cur):
    heap[cur] = i
    if cur == 1:
        return
    else:
        parent = cur // 2
        while abs(heap[parent]) >= abs(heap[cur]):
            if parent == cur:
                break
            if abs(heap[parent]) == abs(heap[cur]):
                if heap[parent] > heap[cur]:
                    heap[parent], heap[cur] = heap[cur], heap[parent]
                    cur = parent
                    parent //= 2
                else:
                    break
            elif abs(heap[parent]) > abs(heap[cur]):
                heap[parent], heap[cur] = heap[cur], heap[parent]
                cur = parent
                parent //= 2
            else:
                break
       
def remove(cur):
    if cur == 1:
        return 0
    elif cur == 2:
        temp = heap[1]
        heap[1] = 0
        return temp
    else:
        temp = heap[1]
        cur -= 1
        heap[1] = heap[cur]
        heap[cur] = 0

        start = 1
        left = 1 * 2
        right = 1 * 2 + 1
        while True:
            if left >= cur:
                break
            elif right >= cur:
                target = left
            elif abs(heap[left]) > abs(heap[right]):
                target = right
            elif abs(heap[left]) < abs(heap[right]):
                target = left
            else:
                if heap[left] < heap[right]:
                    target = left
                else:
                    target = right
            # print(heap[target], heap[start])
            if abs(heap[target]) < abs(heap[start]):
                heap[start], heap[target] = heap[target], heap[start]
                start = target
                left= start * 2
                right = start * 2 + 1
            elif abs(heap[target]) == abs(heap[start]):
                if heap[target] < heap[start]:
                    heap[start], heap[target] = heap[target], heap[start]
                    start = target
                    left= start * 2
                    right = start * 2 + 1
                else:
                    break
            else:
                break
        return temp

cur = 1
for _ in range(n):
    a = int(input())
    if a == 0:
        if cur == 1:
            print(0)
        else:
            print(remove(cur))
            if cur > 1:
                cur -= 1
    else:
        append(a, cur)
        cur += 1