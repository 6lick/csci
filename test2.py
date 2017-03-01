key=[]
codebook = {}
class minheap(object):
	def __init__(self):
		self.heap = []
	def insert(self,value, f):
		self.heap.append(f)
		self.org()
		key.append(value)
		key[value]=value
		codebook=dict(zip(key,self.heap))
		
		#print(codebook)
	
		
				
	def deletemin(self):
		a = self.heap[0]
		del self.heap[0]
		codebook.pop
		self.org()
		return a
		
	def org(self):
		#for i in range(0,len(self.heap)):
			#key.append(i)
			#key[i]=i
			#codebook=dict(zip(key,self.heap))
			#print(codebook)
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
				
		
		
	def view(self):
		for i in range(len(self.heap)):
			print(self.heap[i])
				
		
		

        
def string2freq(x):
        S=[x[0]]
        f=[1]
        for i in range(1,len(x)):
				found = False
				for j in range(0,len(S)):
						if x[i]==S[j]:
								
								f[j]=f[j] + 1
								found = True
								j = len(S)

								
				if found == False:
						S.append(x[i])
						f.append(1)
				
				
				
                    
        return S,f



def huffmanEncode(S,f):
	H = minheap()
	for i in range(len(S)):
			H.insert(i, f[i])
	for k in range(len(S),2*len(S)-2):
			i = H.deletemin()
			j = H.deletemin()
			f.append(f[i] + f[j])
			H.insert(k, f[k])
	return codebook
	
def main():
		x = string2freq("Hello World")
		
		print(huffmanEncode(x[0],x[1]))

if __name__ == "__main__":main()			
				 
	
