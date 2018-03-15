from data import InputData, InputType
from node import NodeCreator
from utils import TestUtil

arr = InputData.read("res/input.txt")

node = NodeCreator.create_node(arr)

NodeCreator.create_child_node(node)

test_data = InputData.read("res/test.txt")

correct = 0
wrong = 0

test_util = TestUtil()

for item in test_data:
    result = test_util.test(node, item)
    if result == item.type:
        correct += 1
    else:
        wrong += 1

print("correct", correct, "wrong", wrong)
print("accuracy", correct / (correct + wrong))
