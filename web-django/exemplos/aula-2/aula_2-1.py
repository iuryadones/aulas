import aulatwo
from aulatwo import fibonacci
from . import aulatwo
from glob import glob
import re

print(glob('*'))

print(aulatwo.fibonacci(100))
print(fibonacci(100))

dic = {'end': '\n\n\n\n'}
print(dir(aulatwo),**dic)
print('test')
#help(aulatwo)


