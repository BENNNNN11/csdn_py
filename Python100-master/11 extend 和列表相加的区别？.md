# Python100


## extend 和列表相加的区别？

两者看起来效果一致

```
>>> l = [1, 2, 3]
>>> j = [4, 5, 6]
>>> l + j
[1, 2, 3, 4, 5, 6]
```
extend 是直接在 l 列表里加入元素，相加会生成一个新元素，并不会对 l 做修改。
