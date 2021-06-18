import collections
import requests
import sys

endpoint = 'http://127.0.0.1:5000'
if len(sys.argv) == 2:
    endpoint = sys.argv[1]
url = endpoint + '/test'

TestCase = collections.namedtuple('TestCase', ['input', 'expected'])
test_cases = [TestCase("hello,world", "l,r"), TestCase("iamyourlyftdriver", "muydv")]
for tc in test_cases:
    d = {'string_to_cut': tc.input}
    r = requests.post(url, data=d)
    print("input: {}, output: {}".format(d, r.json()))
    assert(r.json()['return_string'] == tc.expected)
