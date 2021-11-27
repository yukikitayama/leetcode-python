class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class WrappableInt:
    def __init__(self, x):
        self.value = x

    def getValue(self):
        return self.value

    def increment(self):
        self.value += 1


class Codec:
    def serialize(self, root: 'Node') -> str:
        serializedList = []
        # 1 is the first ID to root node
        self._serializeHelper(root, serializedList, WrappableInt(1), None)
        serialized = ''.join(serializedList)

        # print(f'serialized: {serialized}')

        return serialized

    def _serializeHelper(self, root, serializedList, identity, parentId):
        if not root:
            return

        # ID of the current node
        # chr() return a string
        # chr(1): '\x01', chr(49) = chr(1 + 48): '1', chr()
        serializedList.append(chr(identity.getValue() + 48))

        # Value of the current node
        serializedList.append(chr(root.val + 48))

        # Parent ID of the current node
        # Only root node has parentId: None, so assign 'N'
        serializedList.append(chr(parentId + 48) if parentId else 'N')

        # Serialize in DFS manner, not level order traversal
        parentId = identity.getValue()
        for child in root.children:
            identity.increment()
            self._serializeHelper(child, serializedList, identity, parentId)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None

        return self._deserializeHelper(data)

    def _deserializeHelper(self, data):

        # Make a hashmap with key node ID and value tuple of parent ID and Node object
        # But the below for loop does not yet connect each node
        nodesAndParents = {}
        # range() step by 3 because it serialized by ID, value, and Parent ID
        for i in range(0, len(data), 3):
            # ord('1'): 49, 49 - 48 = 1
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))

        # Connect child node with parent node
        # start: 3 because current node is child, with which we connect the parent
        # so the data[0:3] is root (parent) data, so we skip
        for i in range(3, len(data), 3):

            # Get current node
            identity = ord(data[i]) - 48
            # [0]: parentId, [1]: Node object
            node = nodesAndParents[identity][1]

            # Get parent node
            parentId = ord(data[i + 2]) - 48
            parentNode = nodesAndParents[parentId][1]

            # Attach
            parentNode.children.append(node)

        # From hashmap get Node object by using the root node ID
        return nodesAndParents[ord(data[0]) - 48][1]


root = Node(1)
root.children = [Node(3), Node(2, []), Node(4, [])]
root.children[0].children = [Node(5, []), Node(6, [])]
codec = Codec()
codec.serialize(root)

