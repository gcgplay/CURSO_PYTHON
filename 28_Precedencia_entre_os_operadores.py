#Precedência entre os operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# conta_1 = 1 + 1 ** 5 + 5 #7
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) #2^10 = 1024
print(conta_1)