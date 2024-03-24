class HashTable:
    def __init__(self):
        self.max_size = 2
        self.table = [0]*2

    def search_key(self, key):
        temp = None
        for x in self.table:
            if x == 0:
                continue
            temp = x.list_search(key)
            if temp != None:
                print("Key Found: " + str(temp))
                return x
        print("Key Not Found.")
        return None

    def get_index(self, index):
        if index < 0 or index >= self.table_length():
            print("ERROR: Index out of range.")
            return
        return self.table[index]

    def insert_hash(self, node):
        A = random.uniform(0, 1)
        hashval = math.floor(self.max_size * ((node.key*A) % 1))
        if self.table[hashval] == 0:
            self.table[hashval] = DoublyLinkedList()
        self.table[hashval].list_insert(node)
        self.resize()

    def delete_key(self, key):
        temp = self.search_key(key)
        if temp == None:
            print("Key does not exist")
        else:
            temp.delete_node(key)

    def print_table(self):
        for x in self.table:
            if x != 0:
                x.print_list()
        return

    def table_length(self):
        count = 0
        for x in self.table:
            if x != 0:
                count += 1
        return count

    def resize(self):
        length = self.table_length()
        table_copy = self.table
        if length == self.max_size:
            print("Table is full. Resizing to double the original size.")
            self.max_size = 2*self.max_size
            self.table = [0] * self.max_size
        elif length == self.max_size//4:
            print("Table has very few elements in it. Reducing table size by 1/4th.")
            self.max_size = self.max_size // 2
            self.table = [0] * self.max_size
        else:
            print("Hash table does not need resizing.")
            return

        temp = []
        for x in table_copy:
            if x != 0:
                temp = x.node_list()
                for y in temp:
                    A = random.uniform(0, 1)
                    hashval = math.floor(self.max_size * ((y.key*A) % 1))
                    if self.table[hashval] == 0:
                        self.table[hashval] = DoublyLinkedList()
                    self.table[hashval].list_insert(y)
        print("Hash table has been resized.")

if __name__ == "__main__":
    hashtable = HashTable()
    node0 = Node(10, "Apple")
    node1 = Node(25, "Banana")
    node2 = Node(36, "Orange")
    node3 = Node(48, "Grapes")

    print("Initially, the hash table is empty.")
    hashtable.print_table()
    print("Length of table:", hashtable.table_length())

    hashtable.insert_hash(node0)
    hashtable.insert_hash(node1)
    hashtable.insert_hash(node2)
    hashtable.insert_hash(node3)

    print("\nAfter inserting nodes:")
    hashtable.print_table()
    print("Length of table:", hashtable.table_length())

    print("\nSearch result for key 36:", hashtable.search_key(36))

    hashtable.delete_key(25)
    hashtable.delete_key(15)  # Trying to delete a non-existent key

    print("\nAfter deleting key 25:")
    hashtable.print_table()
    print("Length of table:", hashtable.table_length())
