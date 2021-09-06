from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        return self.repeat_serialize(root, '')

    def repeat_serialize(self, root: TreeNode, string: str):
        if root is None:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = self.repeat_serialize(root.left, string)
            string = self.repeat_serialize(root.right, string)
        return string

    def deserialize(self, data: str) -> TreeNode:
        data_list = data.split(',')
        root = self.repeat_deserialize(data_list)
        return root

    def repeat_deserialize(self, data_list: List[str]) -> Optional[TreeNode]:
        if data_list[0] == 'None':
            data_list.pop(0)
            return None

        root = TreeNode(int(data_list[0]))
        data_list.pop(0)
        root.left = self.repeat_deserialize(data_list)
        root.right = self.repeat_deserialize(data_list)
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
ser = Codec()
deser = Codec()
serialized = ser.serialize(root)
print(f'Serialized: {serialized}')
root = deser.deserialize(serialized)
print(root.val)
print(root.left.val, root.right.val)
print(root.left.left.val, root.left.right.val)