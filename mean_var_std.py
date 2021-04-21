import numpy as np

def calculate(list):
  if len(list) is not 9:
    raise ValueError('List have to be nine numbers long')

  numbers = np.array(list).reshape(3,3)
  print(numbers)
  
  operations = {
      "mean": [
          np.mean(numbers, axis=0).tolist(),
          np.mean(numbers, axis=1).tolist(),
          np.mean(numbers.tolist())
      ],
      "variance": [
          np.var(numbers, axis=0).tolist(),
          np.var(numbers, axis=1).tolist(),
          np.var(numbers.tolist())
      ],
      "standard deviation": [
          np.std(numbers, axis=0).tolist(),
          np.std(numbers, axis=1).tolist(),
          np.std(numbers.tolist())
      ]
  }

  return operations