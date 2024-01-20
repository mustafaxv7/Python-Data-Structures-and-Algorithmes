class Node:
    def __init__(self,data = None,next = None) -> None:
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print('The List is empty')
            return
        temp = self.head
        llist = ''
        while temp:
            llist += str(temp.data) + ' --> '
            temp = temp.next
        llist += 'None'
        print(llist)
    
if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_begining(12)
    llist.insert_at_begining(8)
    llist.insert_at_begining(2)
    llist.print()
    
