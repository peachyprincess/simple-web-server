import collections

def get_every_third_letter(s):
    every_third_letter = [s[3 * i - 1] for i in range(1, len(s) // 3 + 1)]
    return "".join(every_third_letter)

TestCase = collections.namedtuple('TestCase', ['input', 'expected'])
test_cases = [TestCase("pig", "g"), TestCase("apple", "p"), TestCase("6chars", "hs")]
for tc in test_cases:
    got = get_every_third_letter(tc.input)
    assert(got == tc.expected)
