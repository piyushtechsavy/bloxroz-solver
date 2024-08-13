class GameArea:
  def __init__(self,maxRow, maxCol):
    self.maxRow = maxRow
    self.maxCol = maxCol
    self.gameBoard = [[0 for i in range(maxCol)] for j in range(maxRow)] 
    

  def setGoalPosition(self, goalX, goalY):
    self.gameBoard[goalX][goalY] = 9

  def printGameBoard(self, block):
    for i in range(self.maxRow):
      print("",end='  ')
      for j in range(self.maxCol):
        if self.gameBoard[i][j] == 0:
          print(" ", end=' ')
        elif (i== block.x1 and j == block.y1) or (i== block.x2 and j == block.y2):
          print("X", end=' ')
        else:
          print(self.gameBoard[i][j], end=' ')
      print("")    

  def initializeLevel1(self):
    tilePositions = [(0,0),(0,1),(0,2),
    (1,0),(1,1),(1,2),(1,3),(1,4),(1,5),
    (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),
    (3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),
    (4,5),(4,6),(4,8),(4,9),
    (5,6),(5,7),(5,8)]
    
    for x,y in tilePositions:
      self.gameBoard[x][y] = 1

    self.setGoalPosition(4,7)  
    