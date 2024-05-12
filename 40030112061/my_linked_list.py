class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    #insertion :  

    def InsertNodeAtTheEndOfTheList(self , new_data):
          data = Node(new_data)
          if self.head == None :
                self.head = data
          else : 
                q = self.head
                while q.next != None :
                      q = q.next
                q.next = data
 
    def InsertNodeAtTheFrontOfTheList(self , new_data):
          data = Node(new_data)
          if self.head == None :
                self.head = data
          else : 
                q = self.head
                data.next = q
                self.head = data
    
    #deleting : 

    def DeleteAtBack(self):
          if self.head == None :
                print('list is already empty!')
          else:
            q = self.head
            
            while q.next != None : 
                    q = q.next
            q = None

    def DeleteAtFront(self):
          if self.head == None :
                print('list is already empty!')
          else:
            self.head = self.head.next


    #search :

    def Search(self , element):
          q = self.head
          index = 0 
          found = False
          while q != None :
                if q.data == element:
                      found = True
                      break
                else : 
                      index += 1
                      q = q.next
          if found == True :
                return index
          else :
                return "element not found"

    #cearing the list :

    def Clear(self):
          self.head = None
          print("list cleard!")

    #size of liked list :

    def Size(self):
          list_size = 0 
          q = self.head
          while q != None:
                list_size += 1
                q = q.next
          print(list_size)
    
    #print : 

    def PrintForward(self):
          if self.head == None:
                print('list is empty')
          q = self.head
          while q != None:
                print(q.data)
                q = q.next
    
    def PrintBackWard(self):
          if self.head == None : 
             print('list is empty')
          else : 
            p = None #pointer of the end of the list 
            while p != self.head:
                    q = self.head
                    while q.next != p :
                            q = q.next
                    print(q.data)
                    p = q   
    # reversing 
    def ReverseNoneRecrusive(self):
        prev = None
        current = self.head
        while(current != None):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def ReverseRecrusive(self,item):
        if item.next == None:
            self.head = item
            return
        self.ReverseRecrusive(item.next)
        temp = item.next
        temp.next = item
        item.next = None
                
            

    

lin = LinkedList()
#adding to list 
lin.InsertNodeAtTheFrontOfTheList(5)
lin.InsertNodeAtTheFrontOfTheList(25)
lin.InsertNodeAtTheFrontOfTheList(4)
lin.InsertNodeAtTheFrontOfTheList(3)
lin.InsertNodeAtTheEndOfTheList(20)
lin.PrintBackWard()
print("\n\n\n")
lin.PrintForward()
print("\n\n")
lin.Size()

print("\n\n\n")

#clearing list and checking print and clr funcs while list is empty 
lin.Clear()
lin.PrintBackWard()
lin.PrintForward()
lin.DeleteAtBack()
lin.DeleteAtFront()

#adding to the empty list and reversing 
lin.InsertNodeAtTheFrontOfTheList(5)
lin.InsertNodeAtTheFrontOfTheList(25)
lin.InsertNodeAtTheFrontOfTheList(4)
lin.InsertNodeAtTheFrontOfTheList(3)
lin.InsertNodeAtTheEndOfTheList(20)
lin.PrintForward()  

print("\n\n\n")
lin.ReverseNoneRecrusive()
lin.PrintForward()

print("\n\n\n")
lin.ReverseRecrusive(lin.head)
lin.PrintForward()


