
# try:
#     print('try...')
#     a = 100 / 0
#     print('result:',a)
# except ValueError as e:
#     print('ValueError',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError', e)
#     #raise  把错误上抛到上一层，让上一层处理
# else:
#     print('unknown error!')
# finally:
#     print('不好意思，出错了')


# a = 100 / 0
# print('end')

'''
    调用栈
'''

# def foo(s):
#     return 100/int(s)
#
# def bar(s):
#     return foo(s)*2
#
# # 在python中，如果py是单独运行，__name__=='__main__', 如果py文件被其他模块引入调用的时候就不等于 import
# if __name__ == '__main__':
#     '''
#         测试 给我们自己调用
#     '''
#     bar('0')


def foo(s):
    return 100/int(s)

def bar(s):
    return foo(s)*2

# 如果py是单独运行，__name__=='__main__',
# 如果py文件被其他模块引入调用的时候就不等于
if __name__ == '__main__':
    '''
        测试 给我们自己调用
    '''
    try:
        bar('0')
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')