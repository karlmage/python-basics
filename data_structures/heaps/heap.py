class Min_int_heap:
    def __init__(self, items=None):
        if items is None:
            items = []
        self._size = 0
        self._items = items

    def _get_l_child_index(self, p_index: int) -> int:
        return 2 * p_index + 1

    def _get_r_child_index(self, p_index: int) -> int:
        return 2 * p_index + 2

    def _get_parent_index(self, ch_index: int) -> int:
        return (ch_index - 1) // 2

    def _has_l_child(self, index: int) -> bool:
        return self._get_l_child_index(index) < self._size

    def _has_r_child(self, index: int) -> bool:
        return self._get_r_child_index(index) < self._size

    def _has_parent(self, index: int) -> bool:
        return self._get_parent_index(index) >= 0

    def l_child(self, index: int):
        if self._has_l_child(index):
            return self._items[self._get_l_child_index(index)]
        else:
            print("No left child found")
            return None

    def r_child(self, index: int):
        if self._has_r_child(index):
            return self._items[self._get_r_child_index(index)]
        else:
            print("No right child found")
            return None

    def parent(self, index: int):
        if self._has_parent(index):
            return self._items[self._get_parent_index(index)]
        else:
            print("No parent found")
            return None

    def _swap(self, p_index: int, ch_index: int):
        temp = self._items[p_index]
        self._items[p_index] = self._items[ch_index]
        self._items[ch_index] = temp

    def _heapify_down(self):
        peek_item = self.peek()
        index = 0
        smaller_ch_index = 0
        while self._has_l_child(index):
            if self.l_child(index) < self.r_child(index):
                smaller_ch_index = self._get_l_child_index(index)
            else:
                smaller_ch_index = self._get_r_child_index(index)
            self._swap(index, smaller_ch_index)
            index = smaller_ch_index

    def _heapify_up(self):
        index = self._size - 1
        while self._has_parent(index) and self._items[index] <= self.parent(index):
            self._swap(index, self._get_parent_index(index))
            index = self._get_parent_index(index)

    def peek(self):
        if self._size == 0:
            print("Peeking an empty heap")
            return None
        else:
            return self._items[0]

    def poll(self):
        if self._size == 0:
            print("Polling an empty heap")
            return None
        else:
            item = self.peek()
            self._items[0] = self._items.pop(-1)
            self._size -= 1
            self._heapify_down()
            return item

    def add_item(self, item: int):
        self._items.append(item)
        self._size += 1
        self._heapify_up()

    def add_items(self, items: [int]):
        for item in items:
            self.add_item(item)

    def show(self):
        print(f"{self._items[0]}\n")
        count = 1
        prev_row_length = 1
        curr_row_length = 0

        while count < self._size:
            print(self._items[count])
            count += 1
            curr_row_length += 1
            if curr_row_length / prev_row_length == 2:
                prev_row_length = curr_row_length
                curr_row_length = 0
                print("\n")

if __name__ == "__main__":
    heap = Min_int_heap()
    items = [45, 14, 156, 19, 3, 5, 6, 1, 0, 89]
    heap.add_items(items)
    heap.show()
    heap.add_item(9)
    heap.show()

