class Block:
  def __init__(self,initX,initY, gameArea):
    self.x1 = initX
    self.x2 = initX
    self.y1 = initY
    self.y2 = initY
    self.parent = None
    self.nextStep = ""
    self.gameArea = gameArea
  
  def getChildBlock(self):
    copyBlock = Block(self.x1, self.y1, self.gameArea)
    copyBlock.x2 = self.x2
    copyBlock.y2 = self.y2
    copyBlock.parent = self
    return copyBlock

  def getRightChild(self):
    rightChild = self.getChildBlock()
    rightChild.moveRight()
    rightChild.nextStep = "Move Right"
    return rightChild

  def moveRight(self):
    if self.x1 == self.x2 and self.y1 == self.y2:
      self.y1 = self.y1 + 1
      self.y2 = self.y2 + 2
    elif self.x1 == self.x2 and (self.y1 + 1) == self.y2:
      self.y1 = self.y1 + 2
      self.y2 = self.y2 + 1
    elif (self.x1 + 1) == self.x2 and self.y1 == self.y2:
      self.y1 = self.y1 + 1
      self.y2 = self.y2 + 1    

  def getLeftChild(self):
    leftChild = self.getChildBlock()
    leftChild.moveLeft()
    leftChild.nextStep = "Move Left"
    return leftChild

  def moveLeft(self):
    if self.x1 == self.x2 and self.y1 == self.y2:
      self.y1 = self.y1 - 2
      self.y2 = self.y2 - 1
    elif self.x1 == self.x2 and (self.y1 + 1) == self.y2:
      self.y1 = self.y1 - 1
      self.y2 = self.y2 - 2
    elif (self.x1 + 1) == self.x2 and self.y1 == self.y2:
      self.y1 = self.y1 - 1
      self.y2 = self.y2 - 1

  def getDownChild(self):
    downChild = self.getChildBlock()
    downChild.moveDown()
    downChild.nextStep = "Move Down"
    return downChild

  def moveDown(self):
    if self.x1 == self.x2 and self.y1 == self.y2:
      self.x1 = self.x1 + 1
      self.x2 = self.x2 + 2
    elif self.x1 == self.x2 and (self.y1 + 1) == self.y2:
      self.x1 = self.x1 + 1
      self.x2 = self.x2 + 1
    elif (self.x1 + 1) == self.x2 and self.y1 == self.y2:
      self.x1 = self.x1 + 2
      self.x2 = self.x2 + 1

  def getTopChild(self):
    topChild = self.getChildBlock()
    topChild.moveTop()
    topChild.nextStep = "Move Top"
    return topChild

  def moveTop(self):
    if self.x1 == self.x2 and self.y1 == self.y2:
      self.x1 = self.x1 - 2
      self.x2 = self.x2 - 1
    elif self.x1 == self.x2 and (self.y1 + 1) == self.y2:
      self.x1 = self.x1 - 1
      self.x2 = self.x2 - 1
    elif (self.x1 + 1) == self.x2 and self.y1 == self.y2:
      self.x1 = self.x1 - 1
      self.x2 = self.x2 - 2

  def isGoalReached(self):
    if self.x1 == self.x2 and self.y1 == self.y2 and self.gameArea.gameBoard[self.x1][self.y1] == 9:
      return True

    return False     

  def isValidPosition(self):
    if self.x1 < 0 or self.x2 < 0 or self.y1 < 0 or self.y2 < 0:
      return False
    
    if self.x1 >= self.gameArea.maxRow or self.x2 >= self.gameArea.maxRow:
      return False
    
    if self.y1 >= self.gameArea.maxCol or self.y2 >= self.gameArea.maxCol:
      return False   
    
    if self.gameArea.gameBoard[self.x1][self.y1] == 0 or self.gameArea.gameBoard[self.x2][self.y2] == 0:
      return False
    
    return True


  def printGameBoard(self):
    self.gameArea.printGameBoard(self)
    
  def printLoc(self):
    print("(%d, %d),(%d, %d)" %(self.x1, self.y1,self.x2, self.y2))
            

  
