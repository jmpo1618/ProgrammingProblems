class Solution(object):
    def _levelOrder(self, current, level, result):
        if current is not None:
            if len(result) - 1 < level:
                result.append([current.val])
            else:
                result[level].append(current.val)
            self._levelOrder(current.left, level + 1, result)
            self._levelOrder(current.right, level + 1, result)

    def levelOrder(self, root):
        result = []
        self._levelOrder(root, 0, result)
        return result
