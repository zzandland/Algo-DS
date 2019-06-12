from typing import Dict, List, Tuple


def remove_repeating_nums(nums: List[int]) -> List[int]:
    """
    >>> remove_repeating_nums([1,3,3,3,2,2,2,3,1])
    [1, 1]
    >>> remove_repeating_nums([1,3,3,3,2,2,4,4,4,3,2,4,1])
    [1, 2, 4, 1]
    """

    if len(nums) == 0:
        return []
    num_blocks = generate_num_blocks(nums)
    mem_dict: Dict[str, List[int]] = {}

    return BFS(num_blocks, mem_dict)


def generate_num_blocks(nums: List[int]) -> List[Tuple[int, int]]:
    prev, cnt = nums[0], 1
    output = []

    for i in range(1, len(nums)):
        if prev == nums[i]:
            cnt += 1
        else:
            output.append((prev, cnt))
            cnt = 1
            prev = nums[i]
    output.append((prev, cnt))

    return output


def BFS(num_blocks: List[Tuple[int, int]],
        mem_dict: Dict[str, List[int]]) -> List[int]:
    str_key = str(num_blocks)

    if str_key not in mem_dict:
        min_list = revert(num_blocks)

        if len(num_blocks) > 1:
            for i, block in enumerate(num_blocks):

                if block[1] > 1:
                    if 0 < i < len(num_blocks) - 1 and num_blocks[
                            i - 1][0] == num_blocks[i + 1][0]:
                        combined = [
                            (num_blocks[i - 1][0],
                             num_blocks[i - 1][1] + num_blocks[i + 1][1])
                        ]
                        tmp = BFS(
                            num_blocks[:i - 1] + combined + num_blocks[i + 2:],
                            mem_dict)
                    else:
                        tmp = BFS(num_blocks[:i] + num_blocks[i + 1:],
                                  mem_dict)

                    if len(tmp) < len(min_list):
                        min_list = tmp
        mem_dict[str_key] = min_list

    return mem_dict[str_key]


def revert(num_blocks: List[Tuple[int, int]]) -> List[int]:
    output = []

    for block in num_blocks:
        for _ in range(block[1]):
            output.append(block[0])

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
