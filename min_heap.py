# Course: CS261 - Data Structures
# Assignment: 5
# Student: Nirav Sheth
# Description: Implement a Min Heap Data structure with add, get_min, remove_min, and build_heap functions


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        method adds a new object to the MinHeap maintaining heap property
        """
        if self.is_empty() is True:
            self.heap.append(node)
        else:
            self.heap.append(node)
            idx_new_node = self.heap.length() - 1
            idx_parent_node = int((idx_new_node - 1) / 2)
            while node < self.heap.get_at_index(idx_parent_node):
                self.heap.swap(idx_new_node, idx_parent_node)
                idx_new_node = idx_parent_node
                idx_parent_node = int((idx_new_node - 1) / 2)

        return

    def get_min(self) -> object:
        """
        method returns an object with a minimum key without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty() is True:
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)


    def remove_min(self) -> object:
        """
        method returns an object with a minimum key and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException
        """
        self.heap.swap(0, self.heap.length() - 1)
        removed_node = self.heap.pop()

        priority_idx = 0
        while priority_idx * 2 + 1 < self.heap.length():
            if priority_idx * 2 + 2 > self.heap.length() - 1:
                if self.heap.get_at_index(priority_idx) > self.heap.get_at_index(priority_idx * 2 + 1):
                    self.heap.swap(priority_idx, priority_idx * 2 + 1)
                    priority_idx = priority_idx * 2 + 1
                else:
                    return removed_node
            else:
                if self.heap.get_at_index(priority_idx) > self.heap.get_at_index(priority_idx * 2 + 1) or \
            self.heap.get_at_index(priority_idx) > self.heap.get_at_index(priority_idx * 2 + 2):
                    if self.heap.get_at_index(priority_idx * 2 + 1) < self.heap.get_at_index(priority_idx * 2 + 2):
                        self.heap.swap(priority_idx, priority_idx * 2 + 1)
                        priority_idx = priority_idx * 2 + 1
                    else:
                        self.heap.swap(priority_idx, priority_idx * 2 + 2)
                        priority_idx = priority_idx * 2 + 2
        return removed_node

    def build_heap(self, da: DynamicArray) -> None:
        """
        method receives a dynamic array with objects in any order and builds a proper
        MinHeap from them
        """
        new_heap = DynamicArray()
        for i in range(da.length()):
            new_heap.append(da.get_at_index(i))

        for i in range(da.length()-1, -1, -1):
            node = new_heap.get_at_index(i)
            idx_parent_node = int((i-1) / 2)
            while node < new_heap.get_at_index(idx_parent_node):
                idx_left_child = idx_parent_node * 2 + 1
                idx_right_child = idx_parent_node * 2 + 2
                if new_heap.get_at_index(idx_left_child) > new_heap.get_at_index(idx_right_child):
                    new_heap.swap(idx_parent_node, idx_right_child)
                    idx_parent_node = idx_right_child
                else:
                    new_heap.swap(idx_parent_node, idx_left_child)
                    idx_parent_node = idx_left_child

                if idx_parent_node*2+2 < new_heap.length():
                    if new_heap.get_at_index(idx_parent_node*2+1) < new_heap.get_at_index(idx_parent_node*2+2):
                        node = new_heap.get_at_index(idx_parent_node*2+1)
                    else:
                        node = new_heap.get_at_index(idx_parent_node * 2 + 2)
                elif idx_parent_node*2+1 < new_heap.length():
                    node = new_heap.get_at_index(idx_parent_node*2+1)
                else:
                    node = new_heap.get_at_index(idx_parent_node)


        self.heap = new_heap
        return

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([17 ,15, 13, 9, 6, 5, 10, 4, 8, 3, 1])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
