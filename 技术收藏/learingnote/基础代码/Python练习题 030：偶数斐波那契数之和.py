'''
简单地说，因为这个数列中的任意数字（第1、2个除外），都是前两个数字之和，所以先初始化第1、2个数字 a, b = 0, 1。
    用一个 while 循环来判断：每次只判断 b 是否为偶数（即是否可以被2整除），是的话，就加入 sum 里，然后把 b 赋值给 a，
        而 b 的新值是 a+b，即通过 a+b 确定下一个斐波那契数字，直到 b 超出 4000000 的限值为止。
a, b = b, a+b 这样的写法真是太方便了！根本不需要考虑 b 赋值给 a 后，对 a+b 会有什么样的影响。
'''


sum = 0
a, b = 0, 1
while b < 4000000:
    if b%2 == 0:
        sum += b
    a, b = b, a+b
print(sum)