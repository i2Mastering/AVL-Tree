class TreeNode:
    """
    Represents a node in an AVL tree.
    
    Attributes:
        data (int): Value stored in the node.
        left (TreeNode): Reference to the left child.
        right (TreeNode): Reference to the right child.
        height (int): Height of the node for balancing purposes.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """
    Implements an AVL tree with insertion, deletion, searching, rotations, and traversal.
    """
    def insert_node(self, root, data):
        """
        Inserts a node into the AVL tree and rebalances it if necessary.
        
        Args:
            root (TreeNode): The root node of the AVL tree.
            data (int): The value to be inserted.
        
        Returns:
            TreeNode: The new root of the balanced AVL tree.
        """
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete_node(self, root, data):
        """
        Deletes a node from the AVL tree and rebalances it if necessary.
        
        Args:
            root (TreeNode): The root node of the AVL tree.
            data (int): The value to be deleted.
        
        Returns:
            TreeNode: The new root of the balanced AVL tree.
        """
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root

    def leftRotate(self, z):
        """
        Performs a left rotation around node `z`.
        """
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        """
        Performs a right rotation around node `z`.
        """
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        """
        Returns the height of a node.
        """
        return root.height if root else 0

    def getBalance(self, root):
        """
        Returns the balance factor of a node.
        """
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def getMinValueNode(self, root):
        """
        Returns the node with the smallest value in the tree.
        """
        while root.left:
            root = root.left
        return root

    def searchNode(self, root, data):
        """
        Searches for a node with the given value.
        Returns True if found, otherwise False.
        """
        if not root:
            return False
        if data == root.data:
            return True
        if data < root.data:
            return self.searchNode(root.left, data)
        return self.searchNode(root.right, data)

    def printPreOrder(self, root):
        """
        Prints the AVL tree in PreOrder traversal.
        """
        if root:
            print(root.data, end=" ")
            self.printPreOrder(root.left)
            self.printPreOrder(root.right)

    def printInOrder(self, root):
        """
        Prints the AVL tree in InOrder traversal.
        """
        if root:
            self.printInOrder(root.left)
            print(root.data, end=" ")
            self.printInOrder(root.right)

    def printPostOrder(self, root):
        """
        Prints the AVL tree in PostOrder traversal.
        """
        if root:
            self.printPostOrder(root.left)
            self.printPostOrder(root.right)
            print(root.data, end=" ")

if __name__ == "__main__":
    myTree = AVLTree()
    root = None
    while True:
        userNum = int(input("Enter a number greater than 0: "))
        if userNum > 0:
            if myTree.searchNode(root, userNum):
                root = myTree.delete_node(root, userNum)
            else:
                root = myTree.insert_node(root, userNum)
        else:
            print("You entered a non-positive integer. Exiting program.")
            break
