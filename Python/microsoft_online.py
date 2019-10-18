from typing import List


def reverse_string(str: str, i: int) -> str:
    if i == len(str):
        return ""

    return reverse_string(str, i + 1) + str[i]


def print_digits(num: int) -> None:
    s = []

    while num > 0:
        s.append(num % 10)
        num //= 10

    while len(s) > 0:
        print(s.pop())


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def gen_linked_list(nums: List[int]) -> Node:
    root = node = None

    for num in nums:
        tmp = Node(num)

        if node is not None:
            node.next = tmp
        node = tmp

        if root is None:
            root = node

    return root


def del_prime_LL(root: Node) -> Node:
    max_val, node = 0, root

    while node is not None:
        max_val = max(max_val, node.val)
        node = node.next
    sieve: List[bool] = gen_prime_sieve(max_val)
    print(sieve)
    node, prev = root, None

    while node is not None:
        if not sieve[node.val]:
            if prev is not None:
                prev.next = node.next
            else:
                node = node.next
                root = node

                continue
        else:
            prev = node
        node = node.next

    return root


def gen_prime_sieve(max_val: int) -> List[bool]:
    sieve = [False for _ in range(max_val + 1)]
    sieve[1] = True

    for i in range(2, (max_val + 1) // 2):
        if not sieve[i]:
            j = 2

            while i * j < len(sieve):
                sieve[i * j] = True
                j += 1

    return sieve


root = gen_linked_list([11, 14, 17, 7, 5, 10])
deleted = del_prime_LL(root)

while deleted is not None:
    print(deleted.val)
    deleted = deleted.next
