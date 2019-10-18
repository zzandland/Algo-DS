'''
'''


def split_palindrome(str1: str, str2: str) -> bool:
    """
    >>> split_palindrome("abcbbbb", "xxxbcba")
    True
    """

    if len(str1) != len(str2):
        return False

    def helper(a: str, b: str) -> bool:
        left, right = 0, len(str1) - 1
        cross_failed = False

        while right > left:
            if cross_failed:
                if a[left] != a[right]:
                    return False
            else:
                if a[left] != b[right]:
                    if a[left] == a[right]:
                        cross_failed = True
                    else:
                        return False
            left += 1
            right -= 1

        return True

    return helper(str1, str2) or helper(str2, str1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
