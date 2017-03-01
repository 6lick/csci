
class minheap(object):
	def __init__(self):
		self.heap = []
	def insert(self,value, f):
		self.heap.append(f)
		self.org()
	
		
				
	def deletemin(self):
		a = self.heap[0]
		del self.heap[0]
		self.org()
		return a
		
	def org(self):
		for i in range(len(self.heap)):
			if (2*i)+1 >= len(self.heap):
				return
			if self.heap[(2*i)+1] < self.heap[i]:
				temp = self.heap[i]
				self.heap[i] = self.heap[(2*i)+1]
				self.heap[(2*i)+1] = temp
			if (2*i)+2 == len(self.heap):
				return
			if self.heap[(2*i)+2] < self.heap[i]:
				temp = self.heap[i]
				self.heap[i] = self.heap[(2*i)+2]
				self.heap[(2*i)+2] = temp
		key=[]		
		for i in range(0,len(self.heap)):
			key.append(i)
			key[i]=i
		codebook=dict(zip(key,self.heap))
		
	def view(self):
		for i in range(len(self.heap)):
			print(self.heap[i])

def main():
       H = minheap()
       H.insert(1, 9)
       H.insert(1, 10)
       H.insert(1, 1)
       H.insert(1, 6)
       H.insert(1, 5)
       H.insert(1, 17)
       H.insert(1, 2)
       H.deletemin()
       H.deletemin()
