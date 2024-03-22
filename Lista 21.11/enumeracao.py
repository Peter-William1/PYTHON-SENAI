list = []

list.append(9)

list.append(3)    
                
list.append(1)

list.append(2)

class Listaor():
  def __init__(self,list):
    self.list_to_organize = list
    self.list_organized = []

  def menor (self):   
     for i in range(len(self.list_to_organize)):
        if i+1 < len(self.list_to_organize):
          if self.list_to_organize[i] < self.list_to_organize[i+1]:
                self.list_organized.append(self.list_to_organize[i])
                print(self.list_to_organize[i])
          
        
lista = Listaor([6,3,67,223,1])

lista.menor()
