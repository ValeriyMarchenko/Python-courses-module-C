class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_branch = None 
        self.right_branch = None 

    def insert_left(self, next_value):
        if self.left_branch is None:
            self.left_branch = BinaryTree(next_value)
        else:
            new_branch = BinaryTree(next_value)
            new_branch.left_branch = self.left_branch
            self.left_branch = new_branch
        return self

    def insert_right(self, next_value):
        if self.right_branch is None:
            self.right_branch = BinaryTree(next_value)
        else:
            new_branch = BinaryTree(next_value)
            new_branch.right_branch = self.right_branch
            self.right_branch = new_branch
        return self

    def pre_order(self):
        print(self.value)

        if self.left_branch is not None:
            self.left_branch.pre_order()

        if self.right_branch is not None:
            self.right_branch.pre_order()

    def post_order(self):
        if self.left_branch is not None:
            self.left_branch.post_order()

        if self.right_branch is not None:
            self.right_branch.post_order()

        print(self.value)

    def in_order(self):
        if self.left_branch is not None:
            self.left_branch.in_order()

        print(self.value)

        if self.right_branch is not None:
            self.right_branch.in_order()

root = BinaryTree(2).insert_left(7).insert_right(5)
node_7 = root.left_branch.insert_left(2).insert_right(6)
node_5 = root.right_branch.insert_right(9)
node_6 = node_7.right_branch.insert_left(5).insert_right(11)
node_9 = node_5.right_branch.insert_left(4)

root.in_order()