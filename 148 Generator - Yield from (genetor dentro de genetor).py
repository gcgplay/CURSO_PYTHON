# 148 Generator - Yield from (genetor dentro de genetor)
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1()) #começa o gen 2, vai para gen 1 e volta para gen 2
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()

# COMECOU GEN2
# COMECOU GEN1
# 1
# 2
# 3
# ACABOU GEN1
# 4
# 5
# 6
# ACABOU GEN2

# COMECOU GEN2
# COMECOU GEN3
# 10
# 20
# 30
# ACABOU GEN3
# 4
# 5
# 6
# ACABOU GEN2
# COMECOU GEN2
# 4
# 5
# 6
# ACABOU GEN2