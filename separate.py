import os
import sys

array = sys.argv
array.pop(0)
print(array)
inicial = 1
final = 1

for nomeDoPdf in array:
    stringArguments = 'pdfseparate -f {} -l {} \"{}\" \"%d-{}\"'.format(inicial,final,nomeDoPdf,nomeDoPdf)
    print(stringArguments)
    os.system(stringArguments)
    inicial +=1
    final+=1
