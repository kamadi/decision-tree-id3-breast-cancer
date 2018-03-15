import sys

from data import InputType, InputData
from utils import calculate_entropy, calculate_total_entropy


class Node(object):

    def __init__(self, type, data=None):
        self.type = type
        self.data = data
        self.children = []  # type: list(Node)
        self.arr = []
        self.result = None
        self.length = 0

    def add_child(self, value):
        self.children.append(value)

    def add_item(self, value):
        self.arr.append(value)
        self.length = len(self.arr)

    def equals(self, item):
        return (self.type is InputType.CLUMP_THICKNESS and self.data == item.clump_thickness) or \
               (self.type is InputType.UNIFORMITY_OF_CELL_SIZE and self.data == item.uniformity_of_cell_size) or \
               (self.type is InputType.UNIFORMITY_OF_CELL_SHAPE and self.data == item.uniformity_of_cell_shape) or \
               (self.type is InputType.MARGINAL_ADHESION and self.data == item.marginal_adhesion) or \
               (self.type is InputType.SINGLE_EPITHELIAL_CELL_SIZE and self.data == item.single_epithelial_cell_size) or \
               (self.type is InputType.BARE_NUCLEI and self.data == item.bare_nuclei) or \
               (self.type is InputType.BLAND_CHROMATIN and self.data == item.bland_chromatin) or \
               (self.type is InputType.NORMAL_NUCLEOLI and self.data == item.normal_nucleoli) or \
               (self.type is InputType.MITOSES and self.data == item.mitoses)


class NodeCreator:

    @staticmethod
    def create_node(arr):

        def get_positive_key(type, index):
            return type.value + str(InputData.BENIGN) + str(index)

        def get_negative_key(type, index):
            return type.value + str(InputData.MALIGNANT) + str(index)

        def get_key(item, type, index):
            return item.value + str(type) + str(index)

        positive_count = 0
        negative_count = 0

        max = -sys.maxsize - 1
        max_class = None

        count_map = {}

        for i in range(1, 11):

            for item in list(InputType):
                count_map[get_positive_key(item, i)] = 0
                count_map[get_negative_key(item, i)] = 0

        for item in arr:
            if item.type == InputData.BENIGN:
                positive_count += 1
            else:
                negative_count += 1

            for input_type in list(InputType):
                key = get_key(input_type, item.type, item.get_value(input_type))
                count_map[key] = count_map[key] + 1

        # print(positive_count, negative_count)

        if positive_count == 0 and negative_count == 0:
            result = Node(None)
            result.result = InputData.MALIGNANT
            return result

        if positive_count > 0 and negative_count == 0:
            result = Node(None)
            result.result = InputData.BENIGN
            return result

        if negative_count > 0 and positive_count == 0:
            result = Node(None)
            result.result = InputData.MALIGNANT
            return result

        # print(count_map)

        total = len(arr)

        entropy_total = calculate_entropy(positive_count, negative_count)

        ig_map = {}

        for item in list(InputType):
            ig_map[item] = entropy_total

        for i in range(1, 11):

            for item in list(InputType):
                value = calculate_total_entropy(count_map[get_positive_key(item, i)],
                                                count_map[get_negative_key(item, i)], total)

                ig_map[item] = ig_map[item] - value

        # print(ig_map)

        for key, value in ig_map.items():
            if value > max:
                max = value
                max_class = key

        # print(max)

        node = Node(max_class)
        node.arr = arr

        for i in range(1, 11):
            child = Node(max_class, i)
            for item in arr:
                if i == item.get_value(max_class):
                    child.add_item(item)
            if child.length == 0:
                child.result = -1
            node.add_child(child)

        return node

    @staticmethod
    def create_child_node(node):
        for child in node.children:
            child_node = NodeCreator.create_node(child.arr)
            if child_node.result is not None:
                child.result = child_node.result
            else:
                child.children.append(child_node)

            for item in child.children:
                NodeCreator.create_child_node(item)
