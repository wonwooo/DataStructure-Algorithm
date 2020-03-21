from Tree.Queue import Queue

class TreeNode:
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None

    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent

    def getLHS(self):
        return self.nodeLHS

    def getRHS(self):
        return self.nodeRHS

    def setRHS(self, node):
        self.nodeRHS = node

    def setLHS(self, node):
        self.nodeLHS = node

    def setParent(self, nodeParent): #추후 reference 변경이 일어나기 때문에 메소드로 생성
        self.nodeParent = nodeParent

    def getParent(self):
        return self.nodeParent

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value, node = None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = TreeNode(value, None) #root는 Parent None으로 설정
            return #안써주면 아래로 내려간다
        if value > node.getValue():
            if node.getRHS() is None: #escape condition
                node.setRHS(TreeNode(value, node))
            else:
                self.insert(value, node.getRHS())
        if value < node.getValue():
            if node.getLHS() is None: #escape condition
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.getLHS())
        if value == node.getValue():
            pass


    def search(self, value, node = None):
        if node is None:
            node = self.root

        if value < node.getValue():
            if node.getLHS() is None: #escape
                return False
            else:
                return self.search(value, node.getLHS())
        if value > node.getValue():
            if node.getRHS() is None:
                return False
            else:
                return self.search(value, node.getRHS())

        if value == node.getValue():
            return True


    def delete(self, value, node = None): #Max in LHS로 구현
        #일단 value 찾을때까지 recursion
        if node is None:
            node = self.root

        if value < node.getValue():
            if node.getLHS() is None:
                return
            else:
                self.delete(value, node.getLHS())
        if value > node.getValue():
            if node.getRHS() is None:
                return
            else:
                self.delete(value, node.getRHS())

        if value == node.getValue(): #3가지 case

            #Case1. LHS와 RHS 모두 있음
            if node.getRHS() is not None and node.getRHS() is not None:
                #LHS의 Max를 찾아서 대체
                maxValue = self.findMax()
                node.setValue(maxValue)
                self.delete(maxValue, node.getLHS())

            '''
            1) Value를 찾았으나 자식이 둘이라서 MAX를 찾아 교체하는 과정이라면 LHS가 있거나 없고, 
            2) 아니라면 Value를 찾았고 RHS/LHS 둘 중 하나만 있는 경우에 여기까지 내려옴
            이제 node.RHS만 있는경우, node.LHS만 있는 경우, 둘다 없는 경우 신경쓰면된다
            '''
            #Case 2. LHS, RHS 둘 중 한곳에만 자식노드가 있음
            parent = node.getParent()

            if node.getLHS() is not None:
                '''여기 걸리는 경우는 2가지
                1)원래 지우고자 하는 node의 LHS의 Max를 지우는 과정에서 걸리는 경우 : node는 반드시 parent의 RHS에 있다.
                2)Max를 지우는 경우가 아닌경우 : node는 parent의 LHS, RHS 어느쪽도 가능하다
                따라서 두 경우를 신경쓰지 않고 node가 parent의 LHS인지, RHS인지 모두 조건문을 써줘야 한다'''
                if node == self.root:  # node가 root면 parent가 없다
                    self.root = node.getLHS()
                    node.getLHS().setParent(None)

                if parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)

            elif node.getRHS() is not None:
                if node == self.root:  # node가 root면 parent가 없다
                    self.root = node.getRHS()
                    node.getRHS().setParent(None)

                if parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)

            #Case3. 자식노드가 없음
            else:
                if node == self.root:
                    self.root = None
                if parent.getLHS == node:
                    parent.setLHS(None)
                else:
                    parent.setRHS(None)


    def findMax(self , node = None):
        if node is None:
            node = self.root
        if node.getRHS() is None:
            return node
        elif node.getRHS() is not None:
            return self.findMax(node.getRHS)

    def findMin(self, node = None):
        if node is None:
            node = self.root
        if node.getsLHS() is None:
            return node
        elif node.getLHS() is not None:
            return self.findMin(node.getLHS())

    def traverseLevelOrder(self):
        ret = []
        Q = Queue()
        Q.enqueue(self.root)
        while not Q.isEmpty():
            currentNode = Q.dequeue()
            ret.append(currentNode.getValue())
            if currentNode.getLHS() is not None:
                Q.enqueue(currentNode.getLHS())
            elif currentNode.getRHS() is not None:
                Q.enqueue(currentNode.getRHS())
        return ret

    def traverseInOrder(self, currentNode = None):
        ret = []
        if currentNode is None:
            currentNode = self.root
        if currentNode.getLHS() is not None:
            ret = ret + self.traverseInOrder(currentNode.getLHS())
        else:
            ret.append(currentNode.getValue())
            if currentNode.getRHS() is not None:
                ret = ret + self.traverseInOrder(currentNode.getRHS())
        return ret

    def traversePostOrder(self, currentNode = None):
        ret = []
        if currentNode is None:
            currentNode = self.root
        if currentNode.getLHS() is not None:
            ret = ret + self.traversePostOrder(currentNode.getLHS())
        if currentNode.getRHS() is not None:
            ret = ret + self.traversePostOrder(currentNode.getRHS())
        ret.append(currentNode.getValue())
        return ret

    def traversePreOrder(self, currentNode = None):
        ret = []
        if currentNode is None:
            currentNode = self.root
        ret.append(currentNode.getValue())
        if currentNode.getLHS() is not None:
            ret = ret + self.traversePreOrder(currentNode.getLHS())
        if currentNode.getRHS() is not None:
            ret = ret + self.traversePreOrder(currentNode.getRHS())

        return ret

tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(0)
tree.insert(5)
tree.insert(1)
tree.insert(4)
tree.insert(5)
tree.insert(1)
tree.insert(9)
tree.insert(8)


print(tree.root.getValue())

print(tree.traverseInOrder())
print(tree.traversePreOrder())
print(tree.traversePostOrder())
print(tree.traverseLevelOrder())
