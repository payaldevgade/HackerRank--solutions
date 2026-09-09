
import operator


def person_lister(f):
    def inner(people):
        people.sort(key=operator.itemgetter(2))
        return [f(person) for person in people]

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


n = int(input("Enter number of people: "))

people = []

for i in range(n):
    people.append(input(f"Enter person {i + 1}: ").split())

print(*name_format(people), sep="\n")
