# Python100



## 怎么查出通过 from xx import xx导入的可以直接调用的方法？

用 __all__ 方法，这个方法查出的是模块下不带_的所有方法，可以直接调用。

```
>>> import random
>>> random.__all__
['Random', 'seed', 'random', 'uniform', 'randint', 'choice', 'sample', 'randrange', 'shuffle', 'normalvariate', 'lognormvariate', 'expovariate', 'vonmisesvariate', 'gammavariate', 'triangular', 'gauss', 'betavariate', 'paretovariate', 'weibullvariate', 'getstate', 'setstate', 'getrandbits', 'choices', 'SystemRandom']

```