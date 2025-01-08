def countPrefixSuffixPairs(words):
    """
    :type words: List[str]
    :rtype: int
    """
    n = len(words)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            str1 = words[i]
            str2 = words[j]
            # Skip if str1 is longer than str2 since it can't be both a prefix and suffix
            if len(str1) > len(str2):
                continue

            if str2.startswith(str1) and str2.endswith(str1):
                count += 1

    return count


test_cases = [
    (["a", "aba", "ababa", "aa"], 4),
    (["pa", "papa", "ma", "mama"], 2),
    (["abab", "ab"], 0),
    (["abc", "abcabc"], 1),  # String that's both prefix and suffix
    (["", "", ""], 3),  # Multiple empty strings
    ([""], 0),  # Edge case: single empty string
    (["a", "a", "a"], 3),  # All same single character
    (["abc", "def", "ghi"], 0),  # No matches
    (["aa", "aaa", "aaaa"], 3),  # Multiple matches with repeating chars
    (["a", "aa", "aaa"], 3)  # Some prefix/suffix pairs
]

for test_case in test_cases:
    words, expected = test_case
    actual = countPrefixSuffixPairs(words)
    try:
        assert actual == expected, f"Input: {words}\nExpected: {expected}\nActual: {actual}\nFailed ❌"
        print(
            f"Input: {words}\nExpected: {expected}\nActual: {actual}\nPassed ✅")
    except AssertionError as e:
        print(e)
