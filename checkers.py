
class Board:

	def __init__(self):
		#initialize 2d array populated by 'None' in all fields
		self.board = [[None for i in range(8)] for j in range(8)]
		#spots where red pieces start
		self.startRed = [(1,2), (1,4), (1,6), (1,8), (2,1), 
			(2,3), (2,5), (2,7), (3,2), (3,4) , (3,6) , (3,8)]
		#spots where black pieces start
		self.startblack = [(8,1), (8,3), (8,5), (8,7), (7,2),
			(7,4), (7,6), (7,8), (6,1), (6,3), (6,5), (6,7)]

	def populateboard(self):
		#'element[index] - 1' to keep inside bounds of 8x8 
		for element in (self.startblack):
			self.board[element[0] - 1][element[1] - 1] = 'B' #black
		for element in (self.startRed):
			self.board[element[0] - 1][element[1] - 1] = 'R' #red

	def printboard(self):
		print("-"*40)
		for col in range(0,8):
			for row in range(0,8):
				if (self.board[col][row] == None):
					print(" | ", ' ' , end='')
				else:
					print(" | ", self.board[col][row], end='')
			print(" |",'\n')
			print("-"*42)

		#print(board) to command line
		# black_circle = '\N{black circle}'
		# black_circle_utf8 = black_circle.decode('utf8')
				


class pieces:
	# team = {
	# 	'R' = 'red',
	# 	'B' = 'blue'
	# }

	# piece = {
	# 'b' : 'blue',
	# 'bk': 'blue king',
	# 'r' : 'red',
	# 'rk': 'red king'
	# }
	pass

class actions:
	def movement(self, board, currCoordinate, newCoordinate):

		assert checkEdge(newCoordinate)
		assert board[newCoordinate[0] - 1][newCoordinate[1] - 1] == None

		if team == 'red':
			#move down
			#check if not occupied
			board[newCoordinate[0] - 1][newCoordinate[1] - 1] = 'R' 
			board[currCoordinate[0] - 1][currCoordinate[1] - 1] = None
			pass
		elif team == 'blue':
			#move up
			#check if not going to edge
			#check if not occupied
			pass
		else:
			#king so can move either up and down
			#check if not going to edge
			#check if not occupied
			pass

	def capture():
		#check if not going to edge
		#check if place over is not occupied
		pass

	def checkEdge(newCoordinate):
		#returns true if going out of bounds
		return ((newCoordiante[0] < 8) and (newCoordinate[1] > 0))


class checkPossibleMoves:
	pass

if __name__ == "__main__":
	b = Board()
	b.populateboard()
	b.printboard()



	# test = input("write something: ")
	# print(test)

#":black_circle:"
#":red_circle:"
