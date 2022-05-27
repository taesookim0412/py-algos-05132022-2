class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


# None -> Recent -> Least Recent -> None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.head = ListNode(None, 0)
        self.tail = ListNode(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # print('get', key, self.keyMap)
        if key in self.keyMap:
            return self.makeMostRecent(key).val
        return -1

    def makeMostRecent(self, key: int) -> ListNode:
        listNode = self.keyMap[key]

        self.deleteListNode(listNode)

        # Adjust list node pointers
        listNode.prev = self.head
        listNode.next = self.head.next

        # Adjust head and previous Most recent node
        self.head.next.prev = listNode
        self.head.next = listNode

        return listNode

    def deleteListNode(self, listNode):
        tempPrev = listNode.prev
        tempNext = listNode.next
        tempPrev.next = tempNext
        tempNext.prev = tempPrev

    def put(self, key: int, value: int) -> None:
        # print('put', key, self.keyMap)
        if key in self.keyMap:
            listNode = self.makeMostRecent(key)
            if listNode.val != value:
                listNode.val = value
        else:
            # Most recent node
            tempHeadNext = self.head.next

            newNode = ListNode(key, value)

            # Insert node into Most recent and move previous most recent pointers to point to our new node
            tempHeadNext.prev = newNode
            newNode.next = tempHeadNext
            newNode.prev = self.head
            self.head.next = newNode
            self.keyMap[key] = newNode

            # evict least recently used key value

            if len(self.keyMap) > self.capacity:
                # print('\n', self.keyMap, '\n')
                lruNode = self.tail.prev

                del self.keyMap[lruNode.key]

                newestLruNode = lruNode.prev

                # Point newest LRU node next to tail
                newestLruNode.next = self.tail

                # Point tail to newest LRU node
                self.tail.prev = newestLruNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)