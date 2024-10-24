from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            self._add(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _add(self, car, currentNode):
        if car.make == currentNode.car.make:
            if car.model < currentNode.car.model:
                if currentNode.hasLeftChild():
                    self._add(car, currentNode.left)
                else:
                    newNode = CarInventoryNode(car)
                    currentNode.left = newNode
                    newNode.parent = currentNode
            elif car.model > currentNode.car.model:
                if currentNode.hasRightChild():
                    self._add(car, currentNode.right)
                else:
                    newNode = CarInventoryNode(car)
                    currentNode.right = newNode
                    newNode.parent = currentNode
            else:
                currentNode.cars.append(car)
        elif car.make < currentNode.car.make:
            if currentNode.hasLeftChild():
                self._add(car, currentNode.left)
            else:
                newNode = CarInventoryNode(car)
                currentNode.left = newNode
                newNode.parent = currentNode
        else:
            if currentNode.hasRightChild():
                self._add(car, currentNode.right)
            else:
                newNode = CarInventoryNode(car)
                currentNode.right = newNode
                newNode.parent = currentNode
		    
    def doesCarExist(self, car):
        if self.root:
            res = self._doesCarExist(car, self.root)
            if res:
                for i in res.cars:
                    if i == car:
                        return True
        return False

    def _doesCarExist(self, car, currentNode):
        if not currentNode:
            return None
        elif car.make == currentNode.make:
            if car.model < currentNode.model:
                return self._doesCarExist(car, currentNode.left)
            elif car.model > currentNode.model:
                return self._doesCarExist(car, currentNode.right)
            else:
                return currentNode
        elif car.make < currentNode.car.make:
            return self._doesCarExist(car, currentNode.getLeft())
        elif car.make > currentNode.car.make:
            return self._doesCarExist(car, currentNode.getRight())

    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, currentNode):
        if currentNode is None:
            return ""
        ret = ""
        if currentNode:
            for car in currentNode.cars:
                ret += str(car) +"\n"
            ret += self._preOrder(currentNode.getLeft())
            ret += self._preOrder(currentNode.getRight())
        return ret

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        if currentNode is None:
            return ""
        ret = ""
        if currentNode:
            ret += self._inOrder(currentNode.getLeft())
            for car in currentNode.cars:
                ret += str(car) +"\n"
            ret += self._inOrder(currentNode.getRight())
        return ret

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):
        if currentNode is None:
            return ""
        ret = ""
        if currentNode:
            ret += self._postOrder(currentNode.getLeft())
            ret += self._postOrder(currentNode.getRight())
            for car in currentNode.cars:
                ret += str(car) +"\n"
        return ret

    def getBestCar(self, make, model):
        make = make.upper()
        model = model.upper()
        maxVal = None
        car = Car(make, model, 0, 0)
        if make is None or model is None:
            return None
        res = self.root
        while res is not None:
            if res.make == make and res.model == model:
                for i in res.cars:
                    if maxVal is None or i.year > maxVal.year or \
                       (i.year == maxVal.year and i.price > maxVal.price):
                        maxVal = i
                return maxVal
            elif res.make < make or (res.make == make and \
                                         res.model < model):
                res = res.right
            else:
                res = res.left
                
    def getWorstCar(self, make, model):
        make = make.upper()
        model = model.upper()
        minVal = None
        car = Car(make, model, 0, 0)
        if make is None or model is None:
            return None
        res = self.root
        while res is not None:
            if res.make == make and res.model == model:
                for i in res.cars:
                    if minVal is None or i.year < minVal.year or \
                       (i.year == minVal.year and i.price < minVal.price):
                        minVal = i
                return minVal
            elif res.make < make or (res.make == make and \
                                         res.model < model):
                res = res.right
            else:
                res = res.left
            
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, currentNode):
        totalPrice = 0
        if currentNode:
            for i in currentNode.cars:
                totalPrice += i.price
            totalPrice += self._getTotalInventoryPrice(currentNode.getLeft())
            totalPrice += self._getTotalInventoryPrice(currentNode.getRight())
        return totalPrice

    def getSuccessor(self, make, model):
        car = Car(make, model, 0, 0)
        res = self._doesCarExist(car, self.root)
        succ = None
        if res is None:
            return None
        elif res.right:
            succ = res.right.findMin()
        else:
            if res.parent:
                if res.parent.left == res:
                    succ = res.parent
                else:
                    res.parent.right = None
                    succ = self.getSuccessor(res.parent.make, res.parent.model)
                    res.parent.right = res
        return succ

    def removeCar(self, make, model, year, price):
        car = Car(make, model, year, price)
        res = self._doesCarExist(car, self.root)

        if res is None:
            return False
        else:
            for i in res.cars:
                if i == car:
                    res.cars.remove(i)
                    if len(res.cars) == 0:
                        if self.root and res == self.root and not\
                           self.root.hasAnyChildren():
                            self.root = None
                        elif self.root and self.root.hasAnyChildren():
                            self._removeCar(res)
                    return True
        return False
    
    def _removeCar(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right= None
        elif currentNode.hasBothChildren():
            succ = self.getSuccessor(currentNode.make, currentNode.model)
            succ.spliceOut()
            currentNode.make = succ.make
            currentNode.model = succ.model
            currentNode.car = succ.car
            currentNode.cars = succ.cars
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.left = currentNode.left
                elif currentNode.isRightChild():
                    currentNode.left.parent = currentNode.parent
                    currentNode.parent.right= currentNode.left
                else:
                    currentNode.replaceNodeData(currentNode.left.make,
                                                currentNode.left.model,
                                                currentNode.left.cars,
                                                currentNode.left.left,
                                                currentNode.left.right)
            else:
                if currentNode.isLeftChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.left = currentNode.right
                elif currentNode.isRightChild():
                    currentNode.right.parent = currentNode.parent
                    currentNode.parent.right = currentNode.right
                else:
                    currentNode.replaceNodeData(currentNode.right.make,
                                                currentNode.right.model,
                                                currentNode.right.cars,
                                                currentNode.right.left,
                                                currentNode.right.right)
