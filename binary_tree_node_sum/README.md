# Problem Statement
Find the sum of depths of all nodes of a Binary Tree.
If the node is the left child of parent and is at even depth, then it's depth should be doubled.

# Main file
Main file is: main_binary_tree_node_sum.py

# Python Version
3.8.5

# How to run
Run the program as
> python3 main_binary_tree_node_sum.py

It will ask you to enter the JSON file path. Once pressed enter, it will return the sum of depth if the given JSON file is valid. Else, the program will exit with an error message.

## Example to run a JSON file
> python3 main_binary_tree_node_sum.py

Now the program will ask you for a JSON file path:
> Enter the JOSN file path:

As an example, provide input_1.json as follows:
> Enter the JOSN file path: input_1.json

Then the output will be displayed:
> Sum of depth of nodes = 20

# Function that calculates Sum of depths of all nodes
The function that calculates the Sum of depths of nodes is present in binary_tree_operation/BinaryTreeSum class.
Function name: BinaryTreeNodeDepthSum
