def boyer_moore(txt: str, pat: str) -> int:
    """
    >>> boyer_moore("AABAACAADAABAABA", "AABA")
    4
    """
    m, n, output = len(pat), len(txt), 0
    c_dict = [-1] * 256

    for i, c in enumerate(pat):
        c_dict[ord(c)] = i

    for i in range(n - m + 1):
        j = m - 1

        while j >= 0:
            if txt[i + j] != pat[j]:
                break
            j -= 1

        if j == -1:
            output += 1

            if i + m < n:
                i += m - c_dict[ord(txt[i + m])]
            else:
                return output
        else:
            i += j - c_dict[ord(txt[i + j])]

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()
