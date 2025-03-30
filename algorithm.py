def knapsack_all_solutions_last_column(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    trace = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                without_item = dp[i - 1][w]
                with_item = dp[i - 1][w - weights[i - 1]] + values[i - 1]

                if with_item > without_item:
                    dp[i][w] = with_item
                    trace[i][w] = [comb + [i - 1] for comb in trace[i - 1][w - weights[i - 1]]]
                    if not trace[i][w]:  
                        trace[i][w] = [[i - 1]]
                elif with_item == without_item:
                    dp[i][w] = with_item
                    trace[i][w] = trace[i - 1][w] + [
                        comb + [i - 1] for comb in trace[i - 1][w - weights[i - 1]]
                    ]
                else:
                    dp[i][w] = without_item
                    trace[i][w] = trace[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                trace[i][w] = trace[i - 1][w]

    last_column_max_value = [dp[i][capacity] for i in range(n + 1)]
    last_column_all_solutions = [trace[i][capacity] for i in range(n + 1)]

    return last_column_max_value, last_column_all_solutions

weights = [1, 2, 4, 4, 6, 3]
values = [6, 11, 1, 12, 19, 12]
capacity = 8

last_column_values, last_column_solutions = knapsack_all_solutions_last_column(capacity, weights, values)

print(last_column_values)

for solutions in last_column_solutions:
    print(solutions)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def count_children(node):
    if not node:
        return 0
    return len(node.children)

root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 2")
grandchild1 = TreeNode("Grandchild 1")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
child1.add_child(grandchild1)

print(f"Number of children in root: {count_children(root)}")
print(f"Number of children in child1: {count_children(child1)}")
print(f"Number of children in child2: {count_children(child2)}")
print(f"Number of children in grandchild1: {count_children(grandchild1)}")