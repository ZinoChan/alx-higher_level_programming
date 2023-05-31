#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        """
        Initializes a Node object.

        Args:
            data (int): The data value to be stored in the node.
            next_node (Node, optional): The reference to the next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        int: The data value stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data value of the node.

        Args:
            value (int): The new data value to be set.

        Raises:
            TypeError: If the value provided is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Node: The reference to the next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node reference of the node.

        Args:
            value (Node): The new reference to the next node.

        Raises:
            TypeError: If the value provided is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList object.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        current_node = self.__head
        result = []
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value in sorted order in the linked list.

        Args:
            value (int): The value to be inserted.

        Algorithm:
            1. Create a new node with the given value.
            2. If the linked list is empty or the value is less than the head's data,
               set the new node's next_node reference to the head and update the head to the new node.
            3. Otherwise, iterate through the linked list until finding the appropriate position
               to insert the new node.
            4. Set the new node's next_node reference to the current node's next_node,
               and update the current node's next_node reference to the new node.

        Complexity Analysis:
            - Time Complexity: O(n) in the worst case, where n is the number of nodes in the linked list.
              This is because we may need to iterate through the entire linked list to find the insertion position.
            - Space Complexity: O(1), as we only use a constant amount of additional space.

        Raises:
            TypeError: If the value provided is not an integer.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (
                current_node.next_node is not None
                and current_node.next_node.data < value
            ):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
