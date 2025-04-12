import sys
input = sys.stdin.readline

def heappush(heap, data):
    heap.append(data)
    cur = len(heap) - 1
    
    while cur != 0:
        par = (cur - 1) // 2
        if heap[par] > heap[cur]:
            heap[par], heap[cur] = heap[cur], heap[par]
            cur = par
        else:
            break
    
    return heap

def heappop(heap):
    if not heap:
        return 0
    if len(heap) == 1:
        return heap.pop()
    
    pop_data = heap[0]
    heap[0] = heap.pop()
    cur = 0

    while cur < len(heap):
        left = cur * 2 + 1
        right = cur * 2 + 2

        if left < len(heap) and right < len(heap):
            if heap[left] > heap[right]:
                target = right
            else:
                target = left
        elif left < len(heap):
            target = left
        else:
            break

        if heap[cur] > heap[target]:
            heap[cur], heap[target] = heap[target], heap[cur]
            cur = target
        else:
            break

    return pop_data

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(arr, x)
    else:
        data = heappop(arr)
        print(data)