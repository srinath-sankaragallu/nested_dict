from functools import reduce
class dict(dict):
    def __init__(self,*args,**kwrds):
        super().__init__(*args,**kwrds)
    #method implementation one
    def nested_keys(self,nested_keys, value):
        if not isinstance(nested_keys, list):
            raise ValueError("Nested keys must be provided in list not in {} !".format(type(nested_keys)))
        if nested_keys:
            nested_keys = list(nested_keys)
            last_key = nested_keys.pop()
            cur = self
            for key in nested_keys:
                cur = cur.setdefault(key, dict())
            cur[last_key] = value
    #method implementation two
    def nested_keys1(self,nested_keys, value):
        if not isinstance(nested_keys,list):
            raise ValueError("Nested keys must be provided in list not in {} !".format(type(nested_keys)))
        if nested_keys:
            last_key = nested_keys.pop()
            reduce(lambda m,k: m.setdefault(k, dict()) , nested_keys, self)[last_key] = value
      
def main():
  d = dict()
  d.nested_keys('abcd',10)
  d.nested_keys('ab12',12)
  print(d) #output will be : {'a': {'b': {'c': {'d': 10}, '1': {'2': 12}}}}
  
  
if __name__ == '__main__':
  main()
