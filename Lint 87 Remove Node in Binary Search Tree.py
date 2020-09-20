#Lint 87 Remove Node in Binary Search Tree

    def removeNode(self, root, val): #一刷想法 先用层序遍历找到val 然后按照先序遍历 找到右子树的最小值进行替代 (未果)
        if not root: return
        if root.val == val: return None
        last_node, direction, curr = self.findval(root, val)
        if not curr: return
        
        if not curr.left and not curr.right:
            if direction == 0: last_node.left = None
            if direction == 1: last_node.right == None
            return root
            
        stack, dest = [last_node, curr], curr    
        if dest.right: #若有右, 找到右子树的最小值进行替代
            dest = dest.right
            while dest:
                stack.append(dest)
                dest = dest.left
            if direction == 0: #再向下比较难进行
                return

    def findval(self, root, val):
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                if node.left:
                    if node.left.val == val:
                        return node, 0, node.left
                    else:
                        tmp.append(node.left) 
                if node.right:
                    if node.right.val == val:
                        return node, 1, node.right
                    else:
                        tmp.append(node.right)
            stack = tmp
        return None, None, None


    def removeNode(self, root, val): #inorder遍历 再重新建树 AC-87%
        if not root: return
        self.found, res = False, []
        self.inorder(root, val, res) #inorder遍历 排除val 结果放入list中
        if not self.found: #如果没找到val直接返回
            return root
        return self.build_tree(res) #根据res再重新建树 DC法

    def inorder(self, root, val, res):
        if not root: return
        self.inorder(root.left, val, res)
        if root.val == val:
            self.found = True
        else:
            res.append(root.val)
        self.inorder(root.right, val, res)

    def build_tree(self, res):
        if not res:
            return None
        if len(res) == 1:
            return TreeNode(res[0])
        l, r = 0, len(res)-1
        mid = (l + r) // 2
        res_tree = TreeNode(res[mid])
        leftree = self.build_tree(res[:mid])
        rightree = self.build_tree(res[mid+1:])
        res_tree.left = leftree
        res_tree.right = rightree
        return res_tree
