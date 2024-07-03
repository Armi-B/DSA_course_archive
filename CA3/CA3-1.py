import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self, value):
            self.value = value


    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        self.check_index(index)
        while index != 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index].value > self.heap[index].value:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        self.check_index(index)
        while (2 * index + 1) < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = left_child_index
            if (right_child_index < len(self.heap) 
                and self.heap[right_child_index].value < self.heap[left_child_index].value):
                min_index = right_child_index
            if self.heap[index].value > self.heap[min_index].value:
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
                index = min_index
            else:
                break

    def heap_push(self, value):
        new_node = self.Node(value)
        self.heap.append(new_node)
        self.bubble_up(len(self.heap) - 1)


    def heap_pop(self):
        if len(self.heap) == 0:
            raise Exception(EMPTY)
        min_val = self.heap[0].value
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) >0 :
            self.bubble_down(0)
        return min_val

    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception('invalid index')
        self.check_index(index)
        if (2 * index + 1) < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = left_child_index
            if (right_child_index < len(self.heap) 
                and self.heap[right_child_index].value <= self.heap[left_child_index].value):
                min_index = right_child_index
        return min_index

    def heapify(self, *args):
        for arg in args:
            self.heap_push(arg)
    
    def check_index(self, index):
        if isinstance(index, int):
            if index<0 or index > (len(self.heap)-1):
                raise Exception(OUT_OF_RANGE_INDEX)
        else:
            raise Exception(INVALID_INDEX)



class HuffmanTree:

    class Node:
        def __init__(self, val, char, left=None, right=None):
            self.letter = char
            self.value = val
            self.left = left
            self.right = right
            self.treeDirection = ''

    def __init__(self):
        self.letters = []
        self.reps = []
        self.codes = None
        self.root = None

    def set_letters(self, *args):
        self.codes = {}
        self.letters = args
        for char in self.letters:
            self.codes[char]=None

    def set_repetitions(self, *args):
        self.reps = args

    def calc_codes(self, node, beforeCode=""):
        code = beforeCode + node.treeDirection
        if not node.right and not node.left:
            self.codes[node.letter] = code
        else:
            if node.right:
                self.calc_codes(node.right, code)
            if node.left:
                self.calc_codes(node.left, code)

    def build_huffman_tree(self):
        nodes = list(zip(self.reps, self.letters))
        nodes = [self.Node(i, j) for i, j in nodes]
        nodes.sort(key=lambda x: (x.value, x.letter), reverse=True)
        while len(nodes) > 1:
            nodes.sort(key=lambda x: (x.value), reverse=True)
            right = nodes[-1]
            left = nodes[-2]
            right.treeDirection = '1'
            left.treeDirection = '0'
            new_head = self.Node(right.value+left.value, right.letter+left.letter,left, right)
            nodes = nodes[:-2]
            nodes = [new_head] + nodes
            self.root = new_head
        self.calc_codes(node=self.root)

    def get_huffman_code_cost(self):
        cost = 0
        index = 0
        for i in self.codes:
            cost = cost + self.reps[index] * len(self.codes[i])
            index = index+1
        return cost

    def set_vals(self, text):
        chars = {}
        self.codes={}
        for i in text:
            chars[i] = chars.get(i, 0) + 1
        self.reps = list(chars.values())
        self.letters = list(chars.keys())
        for char in self.letters:
            self.codes[char]=None

    def text_encoding(self, text):
        self.set_vals(text)
        self.build_huffman_tree()

class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = self.Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = self.Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = self.Node(key)
            else:
                self._insert_recursive(current.right, key)

    def inorder(self):
        nodes = []
        self._inorder_recursive(self.root, nodes)
        inres = ''
        for e in nodes:
            inres = inres + str(e) + " "
        print(inres)
    
    def _inorder_recursive(self, root, nodes):
        if root:
            self._inorder_recursive(root.left, nodes)
            nodes.append(root.key)
            self._inorder_recursive(root.right, nodes)


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
