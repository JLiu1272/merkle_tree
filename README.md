# Merkle Tree

This is a simple program that takes a set of contents and generates a Merkle Tree out of it.  

For example, given a set of strings ["cat", "kitten", "dog", "turtle", "dinasour"], the final result would be "catkittendogturtlediasour". 

The above result is not the hash of the content. This makes it easier to demonstrate that the merkle tree is working as expected.

# Merkle Tree Use Case 

## Create a Digital Footprint for Content

## Content Verification

Merkle Tree is useful for verifying that the content provided is not compromised. It does this by checking the hash. If the content are identical, then the hash should also be identical. If the hash differs, it means the content given to you is not what you expected. Doing hash verification is significantly faster than checking on a per file basis.  