import sys

class Node:
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None
    self.equity = None

class BST:
  def __init__(self):
    self.root = None

  def _insert(self,data,root):
    if root == None:
      root = Node(data)
      return root
    if root.data > data:
      root.left = self._insert(data,root.left)
    elif root.data < data:
      root.right = self._insert(data,root.right)
    return root

  def insert(self,data):
    if self.root == None:
      self.root = Node(data)
    else:
      self._insert(data,self.root)

  def get_equity(self,node):
    if node == None:
      return 0

    if self.is_leaf(node):
      return 1.0

    if node.left == None:
      return float(1 - abs(1-(self.get_avg(node.right)/self.get_max(node.right))))

    if node.right == None:
      return float(1 - abs((self.get_avg(node.left)/self.get_max(node.left))-1))
      
    return float(1 - abs((self.get_avg(node.left)/self.get_max(node.left))-(self.get_avg(node.right)/self.get_max(node.right))))

  def is_leaf(self,node):
    if node.left == None and node.right == None:
      return True
    else:
      return False

  def get_avg(self,node):
    if node == None:
      return 0

    sum = node.data + self.get_sum(node.left) + self.get_sum(node.right)
    count = 1 + self.get_count(node.left) + self.get_count(node.right)

    return sum/count

  def get_sum(self,node):
    if node == None:
      return 0

    return node.data + self.get_sum(node.left) + self.get_sum(node.right)

  def get_count(self,node):
    if node == None:
      return 0

    return 1 + self.get_count(node.left) + self.get_count(node.right)

  def get_max(self,node):
    if node == None:
      return 0

    while node.right != None:
      node = node.right

    return node.data

def inorder(root,nodes):
  if root == None:
    return
  
  inorder(root.left,nodes)
  nodes.append(root)
  inorder(root.right,nodes)

# 🔹 Input from command line
file = sys.argv[1]

arr = []
with open(file,"r") as f:
  for line in f:
    arr.append(int(line))

bst = BST()
for i in arr:
  bst.insert(i)

nodes = []

inorder(bst.root,nodes)

max_equity = []
max_val = -1

for i in nodes:
  if(bst.is_leaf(i) == False):
    equity = bst.get_equity(i)
    if equity > max_val:
      max_val = equity

for i in nodes:
  if(bst.is_leaf(i) == False):
    equity = bst.get_equity(i)
    if equity == max_val:
      max_equity.append((i.data,equity))

for i in max_equity:
  print(i[0]," ",i[1])