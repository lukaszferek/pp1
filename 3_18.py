#as few coins as possible
amount = int(input('enter amount, it should be a natural number: '))

five = amount // 5
two = (amount - 5 * five) // 2
one = (amount - 5 * five - 2 * two) // 1

print(f'5 zł - {five}\n2 zł - {two}\n1 zł - {one}')