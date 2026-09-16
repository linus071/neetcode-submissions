class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(root):
            # BASE CASE: Explicit null markers are REQUIRED to preserve tree shape
            if not root:
                res.append("N")
                return
            
            # PREORDER: Process Root -> Left -> Right
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        # O(N) string joining (Avoids O(N^2) repeated string concatenation)
        return ",".join(res)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0  # Global index pointer keeps time complexity at O(N)

        def dfs():
            # GOTCHA 1: "N" indicates an empty leaf slot. Advance pointer and return None.
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            # GOTCHA 2: Current element is guaranteed to be the root of this subtree.
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Always increment after consuming a value

            # GOTCHA 3: MUST process left BEFORE right to match Preorder DFS symmetry!
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()