from pprint import pprint
# first, get the file of classifiers
# curl https;//pypi.python.org/pypi?%3Aaction=list_classifiers > \
# pypi_classifiers.txt

orig = open("./pypi_classifiers.txt").read()
orig = orig.split('\n')
orig = [x.split(' :: ') for x in orig]
#get rid of empty list due to newline at EOF
orig.pop(-1)

tree = {}


def treebuilder(branch, arr):
    if len(arr) == 1:
        branch[arr[0]] = {}
        return
    if arr[0] not in branch.keys():
        branch[arr[0]] = {}
    treebuilder(branch[arr[0]], arr[1:])

for line in orig:
    treebuilder(tree, line)

pprint(tree)
