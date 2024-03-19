class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None
          self.level = None

      def __str__(self):
         return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
            print("----Set root----")
            print(self.root)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        print("Node value " +str(current.info))
                        print("Set left " +str(current.left))
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        print("Node value " +str(current.info))
                        print("Set right ----> " +str(current.right))
                        break
                else:
                    break

def lca(root, v1, v2):
    if (root.info < v1 and root.info > v2) or (root.info > v1 and root.info < v2):
        return root
    elif root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v1 and root.info > v2:
        return lca(root.left, v1, v2)
    elif root.info == v1 or root.info == v2:
        return root

tree = BinarySearchTree()

t = int(input('Enter total number of elements in the list \n'))

arr = list(map(int, input('Enter ' + str(t) + ' values separated by whitespace \n').split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input('Enter two values from the previous list separated by whitespace \n').split()))

ans = lca(tree.root, v[0], v[1])
print("Least common ancestor is: " + str(ans.info))
