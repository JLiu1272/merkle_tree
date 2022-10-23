from typing import List
import hashlib


class Node: 
    def __init__(self, hash = "") -> None:
        self.hash = hash 
        self.left = None
        self.right = None

class MerkelTreeUtilities: 
    def __init__(self) -> None:
        self.tree = None 
    
    """
    Functions to create Merkle Tree 
    """
    def merge_hashnodes(self, left_hashnode: Node, right_hashnode: Node) -> Node:
        combined_hash = left_hashnode.hash + right_hashnode.hash 
        new_root = Node(combined_hash) 
        new_root.left = left_hashnode 
        new_root.right = right_hashnode 
        return new_root 

    def merge(self, hashnodes: List[Node]) -> Node: 

        if len(hashnodes) == 1:
            return hashnodes[0] 
        
        new_hashnodes = []
        for i in range(0, len(hashnodes), 2):
            left_hashnode = hashnodes[i]

            if i + 1 >= len(hashnodes):
                new_hashnodes.append(left_hashnode)
            else:
                right_hashnode = hashnodes[i + 1]
                new_root = self.merge_hashnodes(left_hashnode, right_hashnode)
                new_hashnodes.append(new_root)
        
        return self.merge(new_hashnodes)

    def contents_to_hashnodes(self, contents: List[str]):
        hashnodes = []

        for content in contents: 
            hash = hashlib.sha256(content.encode()).hexdigest()
            hashnodes.append(Node(content)) 
        
        return hashnodes
    
    def create_merkle_tree(self, contents: List[str]):
        hashnodes = self.contents_to_hashnodes(contents)
        merkle_tree = self.merge(hashnodes)
        self.tree = merkle_tree 
        return merkle_tree
    
    """
    Functions to display merkle tree
    """
    def traverse_merkle_tree(self, merkle_tree: Node):

        if merkle_tree == None:
            return 
        
        print("Hash: ", merkle_tree.hash)
        self.traverse_merkle_tree(merkle_tree.left)
        self.traverse_merkle_tree(merkle_tree.right)

def main():
    contents = ["cat", "kitten", "dog", "turtle", "dinasour"]

    merkelTreeUtilities = MerkelTreeUtilities()
    merkle_tree = merkelTreeUtilities.create_merkle_tree(contents)
    merkelTreeUtilities.traverse_merkle_tree(merkle_tree)

if __name__=="__main__":
    main()


    

        


