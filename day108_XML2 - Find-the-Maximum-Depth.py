
import xml.etree.ElementTree as etree


maxdepth = 0


def depth(elem, level):
    global maxdepth

    level += 1

    if level > maxdepth:
        maxdepth = level

    for child in elem:
        depth(child, level)


n = int(input("Enter number of XML lines: "))

xml = ""

for _ in range(n):
    xml = xml + input() + "\n"

root = etree.fromstring(xml)

depth(root, -1)

print("Maximum depth:", maxdepth)

