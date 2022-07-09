import random
lotto = []
qty = int(input("구매 수량을 입력해주세요"))
cnt = 1
while cnt <= qty:
    i = 1
    while i <= 45:
        lotto.append(i)
        i += 1
    lottosize = len(lotto) # 45
    i = 1
    while i <= 6:
        lottosize -= 1
        idx = random.randint(0, lottosize)
        lottonum = lotto.pop(idx)
        print(lottonum, end=", ")
        i += 1
    lotto.clear()
    cnt += 1
    print()