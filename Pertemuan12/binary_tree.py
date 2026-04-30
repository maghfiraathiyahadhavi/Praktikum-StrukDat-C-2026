# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Class Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. Insert Manual 
    def insert_manual(self):
        print("[INFO] Membangun Struktur Gudang...")

        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
        print("[INFO] Struktur berhasil dibuat.\n")

    # 2. Preorder (Root - Left - Right)
    def traverse_preorder(self, node):
        if node:
            print(node.data, end=" - ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    # 3. Inorder (Left - Root - Right)
    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print(node.data, end=" - ")
            self.traverse_inorder(node.right)

    # 4. Postorder (Left - Right - Root)
    def traverse_postorder(self, node):
        if node:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print(node.data, end=" - ")

    # 5. Ambil Leaf Nodes
    def get_leaf_nodes(self, node, leaves):
        if node:
            if node.left is None and node.right is None:
                leaves.append(node.data)
            self.get_leaf_nodes(node.left, leaves)
            self.get_leaf_nodes(node.right, leaves)


# MAIN PROGRAM
tree = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("======================================")

tree.insert_manual()

print("HASIL AUDIT:")

print("1. Pre-Order :", end=" ")
tree.traverse_preorder(tree.root)
print("\b\b ")  

print("2. In-Order :", end=" ")
tree.traverse_inorder(tree.root)
print("\b\b ")

print("3. Post-Order :", end=" ")
tree.traverse_postorder(tree.root)
print("\b\b ")

# Leaf Nodes
leaves = []
tree.get_leaf_nodes(tree.root, leaves)

print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaves))
print("======================================")
print("Audit Selesai!")