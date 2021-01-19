# Python100


## 怎么用for循环实现把字符串变成Unicode码位的列表


```
>>> st = '!@#$%^&*'
>>> codes = []
>>> for s in st:
    codes.append(ord(s))

>>> codes
[33, 64, 35, 36, 37, 94, 38, 42]
```