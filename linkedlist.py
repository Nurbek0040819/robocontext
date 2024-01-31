class Node:
    # Node bu tugun
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self,new_data):
        '''listning boshiga tugun qoshamiz'''
        # yangi node yaratamiz
        new_node = Node(new_data)

        # yangi node tugunimizni bosh tugunga boglaymiz va shu orqali boshiga element qoshamiz
        new_node.next = self.head
        self.head = new_node 

    def insertAfter(self,prev_node,new_data):
        '''biron tugundan keyin tugun qoshamiz'''
        if prev_node is None:
            print('mavjud emas')
            return 
            '''yangi tugun qoshvoldik'''
            new_node = Node(new_data)
            '''yangi tugunni kiyingi tugunga boglaymiz'''
            new_node.next = prev_node.next
            '''avvalgi tugunni yangiga '''
            prev_node.next = new_node

    def deletenode(self,key):
        temp = self.head
        if (temp and temp == key):
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
                prev = temp
                temp = temp.next
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None
