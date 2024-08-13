class BloxorzSearch:
  def __init__(self):
    self.visited = []
  
  def isStateVisited(self, block):
    for b in self.visited:
      if b.x1 == block.x1 and b.x2 == block.x2 and b.y1 == block.y1 and b.y2 == block.y2:
        return True
    return False;

  def checkAndMove(self, block, queue):
    if block.isValidPosition():
      if self.isStateVisited(block):
        return False

      queue.append(block)
      
      self.visited.append(block)
      return True

    return False

  def printPath(self, goalBlock):
    path = [goalBlock]
    temp = goalBlock.parent

    while temp != None:
      path = [temp] + path
      temp = temp.parent

    for b in path:
      print(b.nextStep)
      b.printLoc()


  def BFS(self, block):
    queue = []
    queue.append(block)
    self.visited.append(block)

    step = 1

    while queue:
      currentBlock = queue.pop(0)

      print("Step %d" %(step))
      print(currentBlock.nextStep)
      currentBlock.printGameBoard()

      step = step + 1

      if currentBlock.isGoalReached():
        print("")
        print("Success. The final path is :")
        self.printPath(currentBlock)
        return True
      else:
        self.checkAndMove(currentBlock.getRightChild(), queue)
        self.checkAndMove(currentBlock.getLeftChild(), queue)
        self.checkAndMove(currentBlock.getTopChild(), queue)
        self.checkAndMove(currentBlock.getDownChild(), queue)

    return False



    
  

