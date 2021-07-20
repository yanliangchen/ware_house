'''
这题若是想清楚了，其实是相当简单，无非是找出各种 a+b+c=1000 的组合，然后验证 a**2 + b**2 = c**2 就行了。
遍历范围方面，因为 a<b<c，最小的 a 最大也就是 332，所以取值范围可设为 range(1, 1000//3)。
b 肯定比 a 大，而且撑死了也超不过 500，所以取为 range(a+1, 1000//2)。而一旦 a, b 都确定，c 自然也就确定了。
话说、什么“毕达哥拉斯三元组”啊？不就是“勾股定律”里的“勾三股四弦五”吗……
果然古代中国人都不怎么外交的，所以西方人都不知道，这定律早就被中国人发现了……
'''

for a in range(1,1000//3):
    for b in range(a+1,1000//2):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)