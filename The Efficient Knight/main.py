# Chessboard representation #
#-------------------------
#0| 0| 1| 2| 3| 4| 5| 6| 7|
#-------------------------
#1| 8| 9|10|11|12|13|14|15|
#-------------------------
#2|16|17|18|19|20|21|22|23|
#-------------------------
#3|24|25|26|27|28|29|30|31|
#-------------------------
#4|32|33|34|35|36|37|38|39|
#-------------------------
#5|40|41|42|43|44|45|46|47|
#-------------------------
#6|48|49|50|51|52|53|54|55|
#-------------------------
#7|56|57|58|59|60|61|62|63|
#-------------------------

# Function to calculate the minimum number of moves between 2 chess tiles
def knightMoves(src, dest):
  # Converting to coordinates
  source = (src % 8, src // 8)
  destination = (dest % 8, dest // 8)
  # Storing all possible moves through board and all visited tiles
  possibleMoves = []
  visited = []
  found = False
  first = 0
  if(found == False):
    # Adds starting tiles to array of moves and visited array
    possibleMoves.append([source])
    visited.append(source)
    while(found == False):
      # Iterates through each array of moves to calculate next move
      for i in range(len(possibleMoves)):
        currMoves = possibleMoves[i][:]
        currTile = currMoves[len(currMoves) - 1]
        # Only continues if current tile is NOT destination tile
        if currTile != destination:
          # Calculates all possible moves from current tile and stores in 'newTiles'
          x = currTile[0]
          y = currTile[1]
          xChange = [2, -2]
          yChange = [1, -1]
          newTiles = []
          for j in xChange:
            for k in yChange:
              newTiles.append((x+j, y+k))
              newTiles.append((x+k, y+j))
          # Only adds moves 'possibleMoves' array if it is allowed
          for l in newTiles:
            # Knight cannot leave board
            if(l[0] < 0 or l[1] < 0 or l[0] > 7 or l[1] > 7):
              pass
            # Knight cannot visited already visited tile
            elif l in visited:
              pass
            else:
              visited.append(l)
              # Adds new allowed moves to 'possibleMoves' array
              if(first == 0):
                possibleMoves[i].append(l);
                first += 1
              else:
                newBranch = currMoves[:]
                newBranch.append(l)
                possibleMoves.append(newBranch)
          first = 0
        # If current tile is the destination, while loop is exited
        elif currTile == destination:
          found = True
  # Minimum path is calculated
  minPath = smallestPath(possibleMoves, destination)
  return minPath

# Function to find smallest path between start and destination tile
def smallestPath(movesArray, destination):
  finalMoves = []
  # Adds all paths that lead to destination to 'finalMoves'
  for i in movesArray:
    if(i[len(i)-1] == destination):
      finalMoves.append(i)
  length = 100
  # Finds smallest array
  for i in finalMoves:
    if(len(i) - 1 < length):
      length = len(i) - 1
  return length