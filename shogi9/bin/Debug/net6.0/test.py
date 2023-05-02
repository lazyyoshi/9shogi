
import clr

clr.AddReference("System")
clr.AddReference("shogi9")

import shogi9
import System

board = shogi9.Board()

a = board.pop()
print(a)
b = board.push()
print(b)

print("\n")
