
def get_bfs(root):
    bfs = []
    queue = []
    queue.append(root)

    while len(queue) > 0:
        bfs.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return bfs


def connect_nodes(node, index, slots, right):
    if node is None:
        return

    if right:
        node.leftNeighbour = (
            slots[index].value if slots[index] is not None else None
        )
    else:
        node.rightNeighbour = (
            slots[index].value if slots[index] is not None else None
        )

    slots[index] = node
    if right:
        connect_nodes(node.right, index + 1, slots, right)
        connect_nodes(node.left, index + 1, slots, right)
    else:
        connect_nodes(node.left, index + 1, slots, right)
        connect_nodes(node.right, index + 1, slots, right)


def connect_nodes_util(root, right=True):
    slots = [None for i in range(100)]
    connect_nodes(root, 0, slots, right)


def search(node, root_node, value):
    if node is not None:
        if node.value == value:
            root_node.found_node = node

        search(node.right, root_node, value)
        search(node.left, root_node, value)
