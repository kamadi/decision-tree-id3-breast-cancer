from data import InputData
from node import NodeCreator


def create_child_node(node):
    for child in node.children:
        # if len(child.arr) == 0:
        # print("")
        child_node = NodeCreator.create_node(child, child.arr)
        if child_node.result is not None:
            child.result = child_node.result
        else:
            child.children.append(child_node)

        for item in child.children:
            create_child_node(item)


def test(node, item):
    if node.result is not None:
        # pprint(vars(item))
        return node.result
    else:
        for child in node.children:
            if child.data is not None:

                    return test(child, item)
            else:
                for child_node in child.children:
                    return test(child_node, item)

arr = InputData.read("res/input.txt")

print(arr)

node = NodeCreator.create_node(None, arr)

print(node)
create_child_node(node)



test_data = InputData.read("res/test.txt")

for item in test_data:
    result = test(node, item)
    print(result,item.type)
