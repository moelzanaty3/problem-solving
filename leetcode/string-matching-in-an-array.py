def stringMatching(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # solution 1

    # seen = set()
    # for i in range(len(words)):
    #     for j in range(len(words)):
    #         if i != j and words[j] in words[i]:
    #             seen.add(words[j])
    # return list(seen)

    # solution 2

    # Join all words with a special delimiter to create one string
    combined = '$'.join(words)
    # Find all words that appear more than once in the combined string
    # (excluding their own complete occurrence)
    return [w for w in words if combined.count(w) > 1]


test_cases = [
    (["mass", "as", "hero", "superhero"], ["as", "hero"]),
    (["leetcode", "et", "code"], ["et", "code"]),
    (["blue", "green", "bu"], [])
]

for test_case in test_cases:
    words, expected = test_case
    actual = stringMatching(words)
    try:
        # Sort both lists to handle valid alternative orderings
        assert sorted(actual) == sorted(
            expected), f"Input: {words}\nExpected: {expected}\nActual: {actual}\nFailed ❌"
        print(
            f"Input: {words}\nExpected: {expected}\nActual: {actual}\nPassed ✅")
    except AssertionError as e:
        print(e)
