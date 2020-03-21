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
    def getValue(self):
        return self.value
    def getParent(self):
        return self.nodeParent
    def setLHS(self, LHS):
        self.nodeLHS = LHS
    def setRHS(self, RHS):
        self.nodeRHS = RHS
    def setValue(self, value):
        self.value = value
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent

class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insert(self, value, node = None):
        if node is None:
            node = self.root
        '''
        Insert는 root부터 시작해서 아래로 내려가는 구조. 윗줄에서 self.root를 node로 설정한 다음 아래에 있는 조건문들을 통과하면서 recursion을 통한 삽입
        '''
        if self.root is None:
            self.root = TreeNode(value, None)
            return
        if value == node.getValue():
            return
        if value > node.getValue():
            if node.getRHS() is None:
                node.setRHS(TreeNode(value, node)) #TreeNode(value, node)로 parent가 node이고 값이 value인 TreeNode를 생성하고 node.setRHS를 통해 node의 RHS로 설정
            else:
                self.insert(value, node.getRHS()) #recursion
        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.getLHS())


    def search(self, value, node = None):
        if node is None:
            node = self.root
        if value == node.getValue():
            return True
        if value > node.getValue():
            if node.getRHS() is None:
                return False
            else:
                return self.search(value, node.getRHS())
        if value < node.getValue():
            if node.getLHS() is None:
                return False
            else:
                return self.search(value, node.getLHS())

    def delete(self, value, node = None):
        if node is None:
            node = self.root
        if node.getValue() < value:
            return self.delete(value, node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        if node.getValue() == value:
            if node.getLHS() is not None and node.getRHS() is not None:
                nodeMin = self.findMin(node.getRHS())
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                '''#nodeMin은 LHS(더 작은 자식노드)가 자명하게 없기 때문에 자식 둘이 있는 경우에서 탈출하고, recursion으로 delete 함수실행시 
                위의 자식 둘이 있는 경우에 안걸리고 내려감.
                즉 찾고자 하는 value에 도착한 동시에 자식이 둘이 있는 경우에서 벗어나기 전까지는 delete함수의 recursion이 반복 되어도 아래로 내려가지 못한다
                이제 양쪽에 자식노드가 있는경우는 없고, 없거나 한쪽만 있기 때문에 parent를 설정해서 reference의 변경과정을 거쳐 삭제가 이루어지게 됨
                '''
                return

            #여기부터 reference 수정을 통한 실질적인 삭제과정인 동시에 재귀함수 탈출
            parent = node.getParent()
            if node.getLHS() is not None:
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return
            if node.getRHS() is not None:
                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent)
                else:
                    parent.setRHS(node.getRHS())
                    node.getRHS().setParent(parent)
                return
            if node == self.root:
                self.root = None
            elif parent.getLHS == node:
                parent.setLHS(None)
            else:
                parent.setRHS(None)
            return

    def findMax(self, node = None):
        if node is None:
            node = self.root
        ret = []
        if node.getLHS() is not None:
            return node
        return self.findMax(node.getRHS())

    def findMin(self, node = None):
        if node is None:
            node = self.root
        if node.getLHS() is None:
            return node
        return self.findMin(node.getLHS())

    def traverseLevelOrder(self):
        ret = []
        Q = Queue()
        Q.enqueue(self.root)
        while not Q.isEmpty():
            currentNode = Q.dequeue()
            if currentNode is None:
                continue
            ret.append(currentNode.getValue())
            if currentNode.getLHS() is not None:
                Q.enqueue(currentNode.getLHS())
            if currentNode.getRHS() is not None:
                Q.enqueue(currentNode.getRHS())
        return ret

    def traverseInOrder(self, currentNode = None):
        if currentNode is None:
            currentNode = self.root
        ret = []
        if currentNode.getLHS() is not None:
            ret = ret + self.traverseInOrder(currentNode.getLHS())
        ret.append(currentNode.getValue())#LHS가 없는 제일 말단으로 가야 이 LINE에 도달
        if currentNode.getRHS() is not None:
            ret = ret + self.traverseInOrder(currentNode.getRHS())
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
