import random
import tkinter as tk
class LaForêt:
	def __init__(self, width,height, vitessePropa):
		self.vitessePropa = vitessePropa
		self.width = width
		self.height = height
		self.forest = [[' ' for i in range(self.width+2)]]
		self.creation_liste()
		
		self.root = tk.Tk()
		self.can = tk.Canvas(self.root, width = self.width*10, height = self.height*10)
		self.can.pack()
		self.print_forest()
		
		self.root.mainloop()

	def creation_liste(self):
		variableBool = True
		for y in range(self.height):
			listeTree = [' ']
			for x in range(self.width):
				if random.randrange(4) == 3:
					listeTree.append(' ')
				else:
					if random.randrange(round(self.width*self.height/4)) == 1:
						listeTree.append('1')
						variableBool = False
					else:
						listeTree.append('0')
			listeTree.append(' ')
			self.forest.append(listeTree)
		if variableBool:
			self.forest[round(self.hight/2)][round(self.width/2)] = '1'
		self.forest.append([' ' for i in range(self.width+2)])

	def print_forest(self):
		self.can.delete('all')
		for y in range(1, self.height + 1):
			for x in range(1, self.width + 1):
				if self.forest[y][x] == '0':
					self.can.create_rectangle(x*10-10, y*10-10, x*10, y*10, fill = 'green')
				elif self.forest[y][x] =='1':
					self.can.create_rectangle(x*10-10, y*10-10, x*10, y*10, fill = 'red')
		self.can.after(self.vitessePropa, self.propagation_feu)

	def propagation_feu(self):
		self.forest1 = []
		for element in self.forest:
			self.forest1.append(list(element))
		for y in range(1, self.height + 1):
			for x in range(1, self.width + 1):
				if self.forest1[y][x] == '1':
					if self.forest1[(y+1)][x] == '0':
						self.forest[(y+1)][x] = '1'
					if self.forest1[(y-1)][x] == '0':
						self.forest[(y-1)][x] = '1'
					if self.forest1[y][(x+1)] == '0':
						self.forest[y][(x+1)] = '1'
					if self.forest1[y][(x-1)] == '0':
						self.forest[y][(x-1)] = '1'
		if self.forest != self.forest1:
			self.print_forest()

LaForêt(100,50,10)
