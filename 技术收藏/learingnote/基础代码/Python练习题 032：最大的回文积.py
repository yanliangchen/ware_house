'''
所谓的“回文积”（Palindrome Product），指的是某个数字，正着念、倒着念都一样，而且这个数字是另外两个数字之乘积。
比如：9009 = 91 × 99，9009就是个回文数，而且是91和99的乘积，暂且就称之为回文积。本题就是求解两个三位数之积中的最大回文数。

思路也很简单：用两个 for 循环轮番找出所有“两个三位数之积中的所有回文数”，用 max() 找出最大的那个即可。
    而判断回文数，最简单的就是用 str() 把数字转化为字符，如果 str == str[::-1]，就判断为是回文，因为 str[::-1] 的作用就是把 str 倒着写。
'''

lst = []
for i in range(100, 999):
    for j in range(100, 999):
        if str(i*j) == str(i*j)[::-1]:
            lst.append(i*j)
print(max(lst))