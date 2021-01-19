# Python100



## 打印出两个列表的笛卡尔积

解法1:使用生成器表达式产生笛卡尔积，可以帮忙省掉运行 for 循环的开销。

```
>>> colors = ['blacks', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s'%(c, s) for c in colors for s in sizes):
    print(tshirt)

blacks S
blacks M
blacks L
white S
white M
white L
```
解法2:使用 itertools 里的 product 生成器函数。


```
>>> import itertools
>>> list(itertools.product(['blacks', 'white'], ['S', 'M', 'L']))
[('blacks', 'S'), ('blacks', 'M'), ('blacks', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
```