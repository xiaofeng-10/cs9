from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.car = car
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None
        self.year = car.year
        self.price = car.price
        self.root = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        if not self.parent:
            return None
        else:
            return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        if not self.left:
            return None
        else:
            return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        if not self.right:
            return None
        else:
            return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        allcars = ""
        for i in self.cars:
            allcars += str(i) + "\n"
        return allcars

    def hasLeftChild(self):
        return self.left
    
    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
            else:
                if self.isLeftChile():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.right
                self.left.parent = self.parent

    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasRightChild():
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def getSuccessor(self):
        succ = None
        if self.right:
            succ = self.right.findMin()
        elif self.parent:
            if self.isLeftChild():
                succ = self.parent
            else:
                self.parent.right = None
                succ = self.parent.getSuccessor()
                self.parent.right = self
        return succ

    def replaceNodeData(self, make, model, cars, lc, rc):
        self.make = make
        self.model = model
        self.cars = cars
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self
