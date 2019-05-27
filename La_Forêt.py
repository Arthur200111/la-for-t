import random
import tkinter as tk
class LaForêt:
	def __init__(self, width,height):
		self.forest = []
		self.width = width
		self.height = height
		self.creation_liste()

		self.root = tk.Tk()

		self.can = tk.Canvas(self.root, width = self.width*10, height = self.height*10)
		self.can.pack()
		
		self.print_forest()

		self.root.bind('<Button-1>', self.propagation_feu)

		self.root.mainloop()

	def creation_liste(self):
		variableBool = True
		for y in range(self.height):
			listeTree = []
			for x in range(self.width):
				arbre = random.randrange(4)
				if arbre == 3:
					listeTree.append(' ')
				else:
					if random.randrange(5) == 1:
						listeTree.append('1')
					else:
						listeTree.append('0')
			self.forest.append(listeTree)
		print(self.forest)

	def print_forest(self):
		self.can.delete('all')
		for y in range(self.height):
			for x in range(self.width):
				if self.forest[y][x] == '0':
					self.can.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill = 'green')
				elif self.forest[y][x] =='1':
					self.can.create_rectangle(x*10, y*10, x*10+10, y*10+10, fill = 'red')

	def propagation_feu(self, event):
		forest1 = [i for i in self.forest]
		for y in range(self.height):
			for x in range(self.width):
				if self.forest[y][x] == '1':
					if forest1[(y+1)%self.height][x] == '0':
						self.forest[(y+1)%self.height][x] = '1'
					if forest1[(y-1)%self.height][x] == '0':
						self.forest[(y-1)%self.height][x] = '1'
					if forest1[y][(x+1)%self.width] == '0':
						self.forest[y][(x+1)%self.width] = '1'
					if forest1[y][(x-1)%self.width] == '0':
						self.forest[y][(x-1)%self.width] = '1'
						if id(forest1) == id(self.forest):
							print('ok')


		self.print_forest()

LaForêt(10,5)