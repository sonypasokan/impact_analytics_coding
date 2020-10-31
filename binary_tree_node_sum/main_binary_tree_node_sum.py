import argparse
import json
from os import path

from binary_tree_operation import BinaryTreeSum

class Parser:
    
    def get_json_data(self):
        """Method to get the json."""
        json_file_path = self.__get_json_file_from_user()
        json_data = self.__validate_input_and_get_json(json_file_path)
        return self.__json_parser(json_data)

    # Private methods
    def __json_parser(self, json_data):
        """Method that parses JSON and gets main node(root node)
        and Dictionary of nodes.
        @json_data: JSON object."""
        if not json_data:
            print("Error: JSON cannot be empty.")
            exit(1)
        root_node = json_data["tree"]["root"]
        node_map = dict()
        for node_info in json_data["tree"]["nodes"]:
            node_map[node_info["id"]] = node_info
        return root_node, node_map
    
    def __get_json_file_from_user(self):
        json_file_path = input("Enter the JOSN file path: ")
        return json_file_path
    
    def __validate_input_and_get_json(self, json_file_path):
        """Method to validate the input read from CLI
        and reads the JSON object.
        @args: ArgumentParser object"""
        error_message = "Error: Please provide valid JSON file as input."
        if not json_file_path:
            print(error_message)
            exit(1)
        if not path.exists(path.abspath(json_file_path)) or not json_file_path.endswith(".json"):
            print(error_message)
            exit(1)
        with open(json_file_path, 'r') as fp:
            json_data = json.load(fp)
        return json_data

        
def main():
    root_id, node_map = Parser().get_json_data()
    bts = BinaryTreeSum()
    root = bts.build_binary_tree(root_id, node_map)
    output = bts.BinaryTreeNodeDepthSum(root)
    print("Sum of depth of nodes =", output)


if __name__ == "__main__":
    main()