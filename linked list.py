class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self,head=None):
        self.head=head

    def insert(self,item):
        curr=self.head
        if self.head:
            while curr.next:
                curr=curr.next
            curr.next=item
        else:
            self.head = item

    def display(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next


    def search(self,search_var):
        curr=self.head
        count=0
        search =False
        self.search_var=search_var
        while curr:
            if curr.data == search_var:
                print(f"Exsist At Postion {count} ")
                return count
                count+=1
                search=True
                break
            curr=curr.next
            count +=1
        if search == False:
            print("The Value Does Not Exsist")
            return None


    def modify(self,new_val,pos):
        curr=self.head
        count=1
        temp=new_val
        while curr:
            if count == pos:
                curr=curr.next
                curr.next = temp
                curr.next = curr
                break
            curr=curr.next
            count+=1


e1 = node(1)
e2 = node(2)
e3 = node(3)
e4 = node(4)

ll=linkedlist()
ll.insert(e1)
ll.insert(e2)
ll.insert(e3)
ll.insert(e4)

ll.display()

ll.search(2)
ll.search(7)

# ll.modify(5,2)

ll.display()