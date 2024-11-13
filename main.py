



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, current):
        newRoot = current.left
        t2 = newRoot.right

        newRoot.right = current
        current.left = t2

        current.height = max(self.get_height(current.left), self.get_height(current.right)) + 1
        newRoot.height = max(self.get_height(newRoot.left), self.get_height(newRoot.right)) + 1

        return newRoot

    def left_rotate(self, current):
        newRoot = current.right
        t2 = newRoot.left

        newRoot.left = current
        current.right = t2

        current.height = max(self.get_height(current.left), self.get_height(current.right)) + 1
        newRoot.height = max(self.get_height(newRoot.left), self.get_height(newRoot.right)) + 1

        return newRoot

    def insert(self, node, data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        else:
            # Duplicate data is not inserted in the tree
            return node

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def search(self, node, key):
        if not node:
            return False
        if key == node.data:
            return True
        elif key < node.data:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def inorder_traversal(self, node):
        if node is not None:
            yield from self.inorder_traversal(node.left)
            yield node
            yield from self.inorder_traversal(node.right)

def get_words_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = []
    word = ''
    for char in text:
        if char.isalpha():
            word += char.lower()
        else:
            if word != '':
                words.append(word)
                word = ''
    if word != '':
        words.append(word)
    return words

def read_dictionary_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return words

def print_inorder_with_balance(avl_tree):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        balance = avl_tree.get_balance(node)
        print(f'Word: {node.data}, Balance: {balance}')
        inorder(node.right)
    inorder(avl_tree.root)

def main():
    print("Starting")
    
    dictionary_filename = 'dictionarywords.txt.txt' 
    dictionary_words = read_dictionary_file(dictionary_filename)

    avl_tree = AVLTree()
    for word in dictionary_words:
        avl_tree.root = avl_tree.insert(avl_tree.root, word)

    
    document_filename = 'document.txt' 
    document_words = get_words_from_file(document_filename)

   
    misspelled_words = set()
    for word in document_words:
        if not avl_tree.search(avl_tree.root, word):
            misspelled_words.add(word)

    
    misspelled_list = sorted(misspelled_words)
    print("Misspelled words:")
    for word in misspelled_list:
        print(word)

    
    print("\nAVL Tree (Inorder Traversal with Balance):")
    print_inorder_with_balance(avl_tree)

if __name__ == '__main__':
    main()
