import collections
import requests
import sys

assert(len(sys.argv) == 2)
route = '/test'
url = sys.argv[1] + route
# The input should not be empty.
assert(url != route)

TestCase = collections.namedtuple('TestCase', ['input', 'expected'])
test_cases = [TestCase("hello,world", "l,r")]
for tc in test_cases:
    r = requests.post(url, data={'string_to_cut': tc.input})
    print(r.text)
