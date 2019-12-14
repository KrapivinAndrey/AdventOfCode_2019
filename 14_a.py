import my

class ChemicalFormula:

    def __init__(self, q, formula):
        self.quantity = q
        self.formula = formula.copy()

chemical_schema = {}

def read_formula(schema, formula):

    temp = formula.split(sep='=>')

    right = temp[1].strip().split(sep=' ')
    element = right[1]
    q = int(right[0])

    chemical = []
    for elements in temp[0].strip().split(sep=','):
        el = elements.strip().split(sep=' ')
        chemical.append((el[1], int(el[0])))
    schema[element] = ChemicalFormula(q, chemical)


for formula in my.read_input():
    read_formula(chemical_schema, formula)

exist = {}
for el in chemical_schema.keys():
    exist[el] = 0


def create(element, q):

    if element == 'ORE':  # если тербуется руда - запишем в очередь
        ores.append(q)
        return

    if element in exist:
        zapas = min(q, exist[element])
        q -= zapas
        exist[element] -= zapas

    if q == 0:  # нечего производить
        return

    magic = chemical_schema[element]
    req = q // magic.quantity
    if req * magic.quantity < q:
        req += 1

    for new_el in magic.formula:
        create(new_el[0], new_el[1] * req)

    exist[element] += req * magic.quantity - q


ores = []

fuel = 0
multi = 1000000
prev_sum = 0
delta = 0
while sum(ores) < 1000000000000:

    create('FUEL', multi)
    fuel += multi

    ost = 1000000000000 - sum(ores)
    if prev_sum == 0:
        delta = multi
    else:
        delta = sum(ores) - prev_sum
    prev_sum = sum(ores)
    print("FUEL = {}; OST = {} PREV = {}".format(fuel, ost, delta))
    if ost - delta < 0:
        multi /= 10


print("Ans = {}".format(fuel))
