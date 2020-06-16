#单链表实现
class Node:
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingelLinkList:
    """单链表"""
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def lengh(self):
        """链表长度"""
        # cur游标（指针）用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next

    def add(self,item):
        """链表头部添加元素,头插法"""
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        """链表尾部添加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """指定位置添加元素"""
        pre = self._head
        if pos <= 0:
            self.add(item)
        elif pos >= (self.lengh()-1):
            self.append(item)
        else:
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            #当循环退出后，pre指向pos-1
            node = Node(item)
            node.next = pre.next
            pre.next = node



    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self,item):
        """寻找指定节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False










