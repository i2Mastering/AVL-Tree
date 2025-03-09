# AVL Tree Implementation

This project implements an AVL tree, a self-balancing binary search tree, using Python. The AVL tree supports insertion, deletion, searching, rotations, and different traversal methods.

## Features
- **Insertion**: Inserts nodes while maintaining balance.
- **Deletion**: Removes nodes and rebalances the tree.
- **Searching**: Checks if a value exists in the tree.
- **Rotations**: Performs left and right rotations to maintain balance.
- **Traversal Methods**: Supports pre-order, in-order, and post-order traversals.

## How It Works
The AVL tree maintains balance by tracking the height of nodes and using rotations when necessary. The key operations include:
- **`insert_node(root, data)`**: Inserts a node while maintaining balance.
- **`delete_node(root, data)`**: Deletes a node and rebalances the tree.
- **`getBalance(root)`**: Calculates the balance factor to determine if rebalancing is needed.
- **`leftRotate(z)`** & **`rightRotate(z)`**: Rotations to restore balance.
- **`printPreOrder(root)`**, **`printInOrder(root)`**, **`printPostOrder(root)`**: Tree traversal methods.

## Installation
Ensure you have Python installed and run the script directly in a terminal or Python environment.

## Usage
Run the script:

```bash
python script.py
```

The script prompts for user input to insert or delete nodes. Enter a number greater than 0 to insert/delete, and a number ≤ 0 to exit.

## Example Interaction
```
Enter a number greater than 0: 10
Enter a number greater than 0: 20
Enter a number greater than 0: 30
Our current tree:
   20
  /   \
 10    30
Enter a number greater than 0: -1
You entered a non-positive integer. Exiting program.
```

## License
This project is open-source and free to use.
