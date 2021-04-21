import numpy as np

def calculate(list):
  if len(list) is not 9:
    raise ValueError('List have to be nine numbers long')

  numbers = np.array(list).reshape(3,3)
  
  operations = {
      "mean": [
          np.mean(numbers, axis=0).tolist(),
          np.mean(numbers, axis=1).tolist()
      ]
  }

  return operations