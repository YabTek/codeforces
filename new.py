def heappush(heap,value):
    heap.append(value)
    current = len(heap) - 1
    heapify_up(heap,current)

def heapify_up(heap,current):
    if current % 2 != 0:
        parent = (current-1)//2
    else:
        parent = (current)//2
                 

    while current and heap[current] < heap[parent]:
            heap[current],parent = parent,heap[current]
            current = parent
            if current % 2 != 0:
                parent = (current-1)//2
            else:
                parent =  (current)//2
                 



def test():
    heap = [2, 4, 5, 7, 9, 10]
    heappush(heap, 3)
    assert heap == [2, 4, 3, 7, 9, 10, 5], f"Error: expected [2, 4, 3, 7, 9, 10, 5],but got {heap}"
    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heappush(heap, 0)
    assert heap == [0, 1, 3, 4, 2, 6, 7, 8, 9, 5], f"Error: expected [0, 2, 1, 4, 5,6, 7, 8, 9, 3], but got {heap}"
    print("Great Job !!!")
test()