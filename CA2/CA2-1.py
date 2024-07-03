import sys
import re

class Queue:
    # این تابع هنگام ایجاد یک شی صدا زده میشود.
    def __init__(self):
        self.q = []
        self.size = 0
    # یک عنصر به ته صف وارد میکتد.
    def enqueue(self, value):
        self.q.append(value)
        self.size += 1
    # یک عنصر از سر صف خارج میکتد.
    def dequeue(self):
        self.size += -1
        return self.q.pop(0)
    def isEmpty(self):
        return self.size == 0
    def getInOneLine(self):
        queue = ""
        for e in self.q:
            queue = queue + str(e) + " "
        print(queue)
    def getSize(self):
        return self.size
    
class Stack:
    def __init__(self, size=10):
        self.items = []
        self.size = size
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def put(self,value):
        self.items[-1] = value
    def peek(self):
        return self.items[-1]
    def expand(self):
        self.size *= 2
    def getInOneLine(self):
        stack = ""
        for e in self.items:
            stack = stack + str(e) + " "
        print(stack)
    def getSize(self):
        return len(self.items)
    def getCapacity(self):
        return self.size
    
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def getList(self):
        curr = self.head
        res = ""
        while not curr == None:
            res = res + str(curr.value) + " "
            curr = curr.next
        print(res)
    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def reverse(self):
            prev_node = None
            curr_node = self.head
            while curr_node is not None:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            self.head, self.tail = self.tail, self.head


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    #شی از نوع runner میسازیم
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()