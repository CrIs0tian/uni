class nodo:
    def __init__(self, name: str, priority: int ):  
        self.name = name 
        self.priority = priority
    def print(self): 
        return f"nome = {self.name}, value = {self.priority}"
        
class heap: 
    def __init__(self): 
        self.H= [] 
        self.i_last_node = 0 
    def min(self): 
        return self.H[0]
    def min_i(self, i, j): 
        if self.H[i].priority<self.H[j].priority: 
            return i 
        else: 
            return j
    def father(self, i): 
        return (i-1) // 2 
    def left_child(self, i): 
        return (i*2) + 1 
    def right_child(self, i): 
        return (i*2) +2
    def swap(self, i, j):
        self.H[i], self.H[j] = self.H[j] , self.H[i]
    def move_up(self, i): 
        while self.father(i)>0 and self.H[i] < self.H[self.father(i)]: 
                self.swap(f, i) 
                i = self.father(i)
                
    def move_down(self, i, r, l): #parametri = i, r = right_child(i), l=left_child(i) 
        while(r<=self.i_last_node or l<= self.i_last_node): 
            if(r>self.i_last_node):
                min = l
            elif(l>self.i_last_node):
                min = r
            else:
                min = self.min_i(r, l) 
            if (self.H[min].priority<self.H[i].priority): 
                swap(i , min)
                i = min
                r = self.right_child(i) 
                l = self.left_child(i)
            else: 
                break
    def insert(self, node:classmethod): 
        self.H.append(node) 
        self.i_last_node += 1 
        self.move_up(self.i_last_node)
    def delete_min(self): 
        self.swap(0, self.i_last_node)
        self.H.pop(self.i_last_node) 
        self.i_last_node-=1 
        self.move_down(0, self.left_child(0), self.right_child(0))
    def incr_key_min(self,i:int, d:int):
        self.H[i].priority += d
        self.move_down(i, self.right_child(i), self.left_child(i))
     

    
        


                     



            
            

      
                
                        
                
                

                
        



    
    








      




