import sys
import copy
import math

# Read in input file
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

# Parse input file into list of dictionaries
data = []
header = lines[0].strip().split('\t')
for line in lines[1:]:
    values = line.strip().split('\t')
    data.append(dict(zip(header, values)))

# Define the target variable and list of attributes
target_variable = header[-1]
attribute_list = header[:-1]

def calc_entropy(data):
    # Compute the entropy of a dataset
    counts = {}
    for row in data:
        if row[target_variable] not in counts:
            counts[row[target_variable]] = 0
        counts[row[target_variable]] += 1
    entropy = 0
    for count in counts.values():
        p = count / len(data)
        entropy -= p * math.log2(p)
    return entropy

def infor_gain(data, attribute):
    # Compute the information gain of splitting on a given attribute
    values = set([row[attribute] for row in data])
    gain = calc_entropy(data)
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        p = len(subset) / len(data)
        gain -= p * calc_entropy(subset)
    return gain

def id3(data, attribute_list):
    # Recursively build decision tree using ID3 algorithm
    if len(set([row[target_variable] for row in data])) == 1:
        return data[0][target_variable]
    if len(attribute_list) == 0:
        counts = {}
        for row in data:
            if row[target_variable] not in counts:
                counts[row[target_variable]] = 0
            counts[row[target_variable]] += 1
        return max(counts, key=counts.get)
    best_attribute = max(attribute_list, key=lambda x: infor_gain(data, x))
    tree = {best_attribute: {}}
    for value in set([row[best_attribute] for row in data]):
        subset = [row for row in data if row[best_attribute] == value]
        subtree = id3(subset, [a for a in attribute_list if a != best_attribute])
        tree[best_attribute][value] = subtree
    return tree

# Build decision tree and print it
tree = id3(data, attribute_list)
print(tree)
