import numpy as np

def calculate(list):
  if len(list) is not 9:
    raise ValueError('List must contain nine numbers.')

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
      ],
      "max": [
          np.max(numbers, axis=0).tolist(),
          np.max(numbers, axis=1).tolist(),
          np.max(numbers.tolist())
      ],
      "min": [
          np.min(numbers, axis=0).tolist(),
          np.min(numbers, axis=1).tolist(),
          np.min(numbers.tolist())
      ]
  }

  return operations