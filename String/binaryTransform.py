num = int(input())

res = ""
for i in range(31, -1, -1):
    res += str((num>>i)&1)

print("binFunction : {} = {}(2)".format(num, bin(num)[2:].zfill(32)))
print("bitShifting : {} = {}(2)".format(num, res))