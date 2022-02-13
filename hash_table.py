class Hash_Table(): #implementing a hash table that works just like a dictionary
  def __init__(self):
    self.MAX = 100 #constant, that's why the caps lock
    self.arr = [None for i in range(self.MAX)] #list comprehension, for each item in the range from 0 to 100 (100 not included), create the array and give no value to each position
  
  def get_hash(self, key): #get the hase based on the word sent
    h = 0 #zero the value for hash
    for char in key: #do this for every character in the key
      h += ord(char) #get the unicode value for the character and add it to the total value of h
    return h % self.MAX #return the value of h mod by max slots in the array

  def __setitem__(self, key, val): #python standard operator
    h = self.get_hash(key)
    self.arr[h] = val
  
  def __getitem__(self, key): #python standard operator
    h = self.get_hash(key)
    return self.arr[h]

  def __delitem__(self,key): #python standard operator
    h = self.get_hash(key)
    self.arr[h] = None

t = Hash_Table()
t['October 3'] = 55 
print(t['October 3'])