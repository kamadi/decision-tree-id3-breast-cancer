from data import InputData
from node import NodeCreator
from utils import TestUtil


def test(is_from_beginning=True, training_percent=70):
    print("-----")
    print()
    if is_from_beginning:
        s = "from beginning"
    else:
        s = "from end"

    print("Training data are " + str(training_percent) + "% " + s)

    data = InputData.read("res/breast-cancer-wisconsin.data.txt")

    training_data_length = int((len(data) * training_percent) / 100)

    if is_from_beginning:

        training_data = data[:training_data_length]

        test_data_length = len(data) - training_data_length

        test_data = data[-test_data_length:]
    else:
        training_data = data[-training_data_length:]

        test_data_length = len(data) - training_data_length

        test_data = data[test_data_length:]

    node = NodeCreator.create_node(training_data)

    NodeCreator.create_child_node(node)

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


test(training_percent=60)
test(training_percent=70)
test(training_percent=80)
test(training_percent=90)

test(False, training_percent=60)
test(False, training_percent=70)
test(False, training_percent=80)
test(False, training_percent=90)
