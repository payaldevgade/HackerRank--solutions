
import xml.etree.ElementTree as etree


def get_attr_number(node):
    score = len(node.attrib)

    for child in node:
        score += get_attr_number(child)

    return score


n = int(input("Enter number of XML lines: "))

xml = ""

for _ in range(n):
    xml += input()

root = etree.fromstring(xml)

print("Total attributes:", get_attr_number(root))

