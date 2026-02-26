import random
import sys

# Generating random values
def random_number_gen(p):
  a = random.randint(1,p-1)
  return a

# Generating even random values
def random_number_gen_even(p):
  a = random.randrange(0,p,2)
  return a

# HashTable
class HashTable:
  def __init__(self,size):
    self.m = size
    self.table = [None]*size
    self.p = 999999937
    self.a = random_number_gen(self.p)
    self.b = random_number_gen_even(self.p)

  def convert(self,word):
    num = 0
    fact = 1
    for i in range(len(word)):
      x = ord(word[i])-ord('a') + 1
      num += x*fact
      fact *= 26
    return num

  def hash(self,key):
    key_converted = self.convert(key)
    return (((self.a*key_converted)+ self.b)%self.p)%self.m

  def insert(self,key,value):
    key_converted = self.convert(key)
    index = self.hash(key)
    if self.table[index] == None:
      self.table[index] = []
    self.table[index].append((key_converted,value))
    return

  def give_value(self,key):
    index = self.hash(key)
    key_converted = self.convert(key)
    id = []
    if self.table[index] is None:
      return id
    for i in self.table[index]:
      if i[0] == key_converted:
        id.append(i[1])
    return id

file = sys.argv[1]
m = int(sys.argv[2])
word1 = sys.argv[3]
word2 = sys.argv[4]

# Initialising table
ht = HashTable(m)

# Checking alphanumeric character
def alpha_numeric(ch):
  if ch >= 'a' and ch <= 'z':
    return True
  if ch >= 'A' and ch <= 'Z':
    return True
  if ch >= '0' and ch <= '9':
    return True
  return False

# Reading the file
with open(file,"r") as f:
  words_list = []
  start = 0
  t = ""
  line_id = 1
  for line in f:
    for i in range(len(line)):
      if alpha_numeric(line[i]):
        start = 1
        if line[i] >= 'A' and line[i] <= 'Z':
          t += chr(ord('a')+ord(line[i])-ord('A'))
        else :
          t += line[i]
        continue
      else:
        if start == 1:
          words_list.append(t)
          t = ""
          start = 0
    if start == 1:
      words_list.append(t)
      t = ""
      start = 0
    for i in range(len(words_list)):
      ht.insert(words_list[i],(line_id,i))
    words_list = [] 
    line_id += 1 

# Printing the output
id_word1 = ht.give_value(word1)
id_word2 = ht.give_value(word2)

same = -1
for i in range(len(id_word1)):
  for j in range(len(id_word2)):
    if id_word1[i][0] == id_word2[j][0] and id_word1[i][1] + 1 == id_word2[j][1]:
      if same == -1 or same != id_word2[j][0]:
        same = id_word2[j][0]
        print(id_word2[j][0])