class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def list_search(self, key):
        temp = self.head
        while temp != None and temp.key != key:
            temp = temp.next
        if temp != None:
            return str(temp.data)
        else:
            return None

    def list_insert(self, node):
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def delete_node(self, key):
        curr = self.head

        while curr:
            if curr.key == key:
                if curr.prev:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                else:
                    self.head = curr.next
                    self.head.prev = None
                print("Node with key " + str(key) + " deleted.")
                return
            curr = curr.next
        print("Node with key " + str(key) + " not found")

    def print_list(self):
        temp = self.head
        while temp != None:
            print("Key: " + str(temp.key) + "  Value: " + str(temp.data))
            temp = temp.next
        return

    def node_list(self):
        if self.head == None:
            return None
        n_list = []
        temp = self.head
        while temp != None:
            n_list.append(temp)
            temp = temp.next
        return n_list
