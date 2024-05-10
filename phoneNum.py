phoneNum = int(9965007)

areaCode = phoneNum / 10000
lineNum = phoneNum % 10000


print(f'{areaCode}-{lineNum}')