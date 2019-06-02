from typing import Dict


def count_substr(target: str, match: str) -> int:
    """TODO: Docstring for count_substr.
    :returns: TODO

    """

    if len(match) > len(target):
        return 0
    c_map = generate_map(match)
    output, i = 0, len(match) - 1

    while i < len(target):
        dist = next_dist(c_map, target, match, i)

        if dist == -1:
            output += 1
            i += 1
        else:
            i += dist

    return output


def generate_map(match: str) -> Dict:
    """TODO: Docstring for generate_map.
    :returns: TODO

    """
    c_map = {}

    for i, char in enumerate(match):
        c_map[char] = max(1, len(match) - i - 1)

    return c_map


def next_dist(c_map: Dict, target: str, match: str, i: int) -> int:
    """TODO: Docstring for .

    :arg1: TODO
    :returns: TODO

    """

    for j in range(0, len(match)):
        t_char = target[i - j].lower()
        m_char = match[-1 - j].lower()

        if t_char != m_char:
            if t_char not in c_map:
                if j == 0:
                    return len(match)

                return c_map[target[i]]

            return c_map[t_char]

    return -1


t = "Bobby works aBobt Zume"
m = "Bob"
print(count_substr(t, m))
