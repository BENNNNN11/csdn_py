# Python100



## 新建一个Latin-1字符集合，该集合里的每个字符的Unicode名字里都有“SIGN”这个单词，用集合推导式完成。


```
>>> from unicodedata import name
>>> {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
{'§', '%', '#', '+', '¬', '£', '<', '$', '=', 'µ', '®', '÷', '©', '±', '°', '¤', '¥', '¶', '×', '>', '¢'}
```
