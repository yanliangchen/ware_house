'''
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

# x = input('请输入一个5位数：')
# if x[0] == x[4] and x[1] == x[3]:
#     print('%s是个回文数' % x)
# else:
#     print('%s不是回文数' % x)



'''
一旦用户输入的不是5位数，那就瞎了！用切片的方法就可以很巧妙地解决问题。代码更新如下：
'''
x = input('请输入任意位数的数字：')
if x == x[::-1]:
    print('%s是个回文数' % x)
else:
    print('%s不是回文数' % x)