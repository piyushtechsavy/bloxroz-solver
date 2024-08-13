from gamearea import GameArea
from block import Block
from search import BloxorzSearch

g=GameArea(6,10)

g.initializeLevel1()
b = Block(1,1, g)

print("let it begin")
search = BloxorzSearch()
search.BFS(b)


