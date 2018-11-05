
class Board:

	def __init__(self):
		#initialize 2d array populated by 'None' in all fields
		self.board = [[None for i in range(8)] for j in range(8)]
		#spots where red pieces start
		self.startRed = [(0,1), (0,3), (0,5), (0,7), (1,0), 
			(1,2), (1,4), (1,6), (2,1), (2,3) , (2,5) , (2,7)]
		#spots where black pieces start
		self.startblack = [(7,0), (7,2), (7,4), (7,6), (6,1),
			(6,3), (6,5), (6,7), (5,0), (5,2), (5,4), (5,6)]

		self.pieces = {
		}

	def populateboard(self):
		#'element[index] - 1' to keep inside bounds of 8x8 

		for element in (self.startblack):
			self.pieces[element] = {
				'team' : 'black',
				'position' : element,#black,
				'king' : False,
				'valid': True #if piece is still in play or not
			}
			self.board[element[0]][element[1]] = self.pieces[element] #black

		for element in (self.startRed):
			self.pieces[element] = {
				'team' : 'red',
				'position' : element,	#red,
				'king' : False,
				'valid': True #if piece is still in play or not
			}
			self.board[element[0]][element[1]] = self.pieces[element] #red


	def printboard(self):
		print("-"*40)
		for col in range(0,8):
			for row in range(0,8):
				if (self.board[col][row] == None):
					print(" | ", ' ' , end='')
				else:
					print(" | ", self.board[col][row]['team'], end='')
			print(" |",'\n')
			print("-"*42)				

def movement(board, pieces, currCoordinate, newCoordinate):

	assert checkEdge(newCoordinate)
	assert checkOccupied(board, newCoordinate)

	board[newCoordinate[0]][newCoordinate[1]] = pieces[currCoordinate]
	board[currCoordinate[0]][currCoordinate[1]] = None	


def capture(board, pieces, currCoordinate, newCoordinate):
	assert checkEdge(newCoordinate)
	assert checkOccupied(board, newCoordinate)

	pass


def checkEdge(newCoordinate):
	#returns true if going out of bounds
	return ((newCoordinate[0] < 8) and (newCoordinate[1] > 0))


	#returns true if new coordinate is already populated
def checkOccupied(board, newCoordinate):
	try:
		return (board[newCoordinate[0]][newCoordinate[1]] == None)
	except:
		return False

def checkPossibleMoves(board, pieces):
	
	moves = {}

	for i in pieces:
		if pieces[i]['team'] == 'red' and pieces[i]['valid'] == True:

			coordinate = pieces[i]['position']

			#check down left
			coordinateCheck = (coordinate[0] - 1,coordinate[1] - 1)
			if checkEdge(coordinateCheck) and checkOccupied(board, coordinateCheck):
				moves[i] = {
					'team' : 'red',
					'old-position' : coordinate,
					'new-position' : (coordinate[0] + 1 , coordinate[1] - 1)
				}
				print ("red")
			#check down right
			coordinateCheck = (coordinate[0] - 1,coordinate[1] + 1)
			if checkEdge(coordinateCheck) and checkOccupied(board, coordinateCheck):
				moves[i] = {
					'team' : 'red',
					'old-position' : coordinate,
					'new-position' : (coordinate[0] + 1 , coordinate[1] + 1)
				}
				print ("red")		

		elif pieces[i]['team'] == 'black' and pieces[i]['valid'] == True:
			#print ("black")
			#check up left
			#check up right

	print(moves)
	return moves


if __name__ == "__main__":
	b = Board()
	b.populateboard()
	b.printboard()

	checkPossibleMoves(b.board, b.pieces)

	movement(b.board, b.pieces, (5,4), (4,5))
	b.printboard()



	# test = input("write something: ")
	# print(test)
