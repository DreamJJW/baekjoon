N = int(input())
tree = {}
for i in range(N):
    root_node, left_node, right_node = list(map(str, input().split()))
    tree[root_node] = left_node, right_node


def pre_order(root_node):
    if root_node != '.':
        print(root_node, end='')
        pre_order(tree[root_node][0])
        pre_order(tree[root_node][1])


def in_order(root_node):
    if root_node != '.':
        in_order(tree[root_node][0])
        print(root_node, end='')
        in_order(tree[root_node][1])


def post_order(root_node):
    if root_node != '.':
        post_order(tree[root_node][0])
        post_order(tree[root_node][1])
        print(root_node, end='')


pre_order('A')
print('')
in_order('A')
print('')
post_order('A')
