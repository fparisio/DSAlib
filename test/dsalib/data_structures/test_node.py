from dsalib.data_structures.node import Node


def test_node_creation():
    value = 42
    node = Node(value)

    assert node.value == value
    assert node.next_node is None


def test_node_with_next_node():
    value1 = 42
    value2 = 13
    node1 = Node(value1)
    node2 = Node(value2, next_node=node1)

    assert node2.value == value2
    assert node2.next_node is not None
    assert node2.next_node.value == value1


def test_node_value_update():
    value1 = 42
    value2 = 13
    node = Node(value1)

    node.value = value2

    assert node.value == value2


def test_node_next_node_update():
    value1 = 42
    value2 = 13
    node1 = Node(value1)
    node2 = Node(value2)

    node2.next_node = node1

    assert node2.next_node is not None
    assert node2.next_node.value == value1
