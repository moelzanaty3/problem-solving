def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    merged = ""
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
    return merged


test_cases = [("abc", "pkr", "apbkcr"), ("ab", "pqrs",
                                         "apbqrs"), ("abcd", "pq", "apbqcd")]

for test_case in test_cases:
    word1, word2, expected = test_case
    actual = mergeAlternately(word1, word2)
    try:
        assert actual == expected, f"Input: {word1}, {word2}\nExpected: {expected}\nActual: {actual}\nFailed ❌"
        print(
            f"Input: {word1}, {word2}\nExpected: {expected}\nActual: {actual}\nPassed ✅")
    except AssertionError as e:
        print(e)
