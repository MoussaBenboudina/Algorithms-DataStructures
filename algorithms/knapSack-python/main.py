
def isValid(weights, x, W):
    if W <= 0: return False
    n = len(weights)
    sumWeight = 0
    for i in range(0, n):
        sumWeight += weights[i] * x[i]
        if sumWeight > W:
            return False
    return sumWeight <= W




def fitness(values, x):
    n = len(values)
    sum = 0
    for i in range(0, n):
        sum += values[i] * x[i]
    return sum




def greedy_by_value(weight , values , x , W) :
  
  sorted_pairs = sorted(zip(values, weights), reverse=True)
  values_sorted, weights_sorted = zip(*sorted_pairs)
  values_sorted = list(values_sorted)
  weights_sorted = list(weights_sorted)

  n = len(weight)
  max_value = 0;
  for i in range(0 , n) : 
      x[i] = 1;
      if not isValid(weights_sorted , x, W) :
          x[i] = 0;
      else :
          max_value += values_sorted[i]

  print(x)
  return x , max_value;




def generate_random_solution(weights , values , W):
    import random
    n = len(weights)
    while  True : 
        random_binary = list(map(int , bin(random.randint(0, (1 << n) - 1))[2:].zfill(n)))
        if isValid(weights , random_binary ,W) :
             return fitness(values , random_binary) , random_binary




def Exhaustive(weights, values, W):
    if W == 0: return 0

    n = len(weights)
    result = []

    for i in range(0, pow(2, n)):
        result.append(bin(i)[2:].zfill(n))
        result[i] = list(map(int, result[i]))

    x_is_valid = list(filter(lambda x: isValid(weights, x, W), result))

    n = len(list(x_is_valid))
    max_value = 0
    best_solution = []
    for x in x_is_valid:
        if fitness(values, x) > max_value:
            max_value = fitness(values, x)
            best_solution = x

    return best_solution, max_value






try:
    weights = [10, 35, 23, 20]
    values = [10, 20, 40, 30]
    x = [0] * len(values)
    W = 50

    print('_' * 100, "\nExhaustive")
    best_solution, max_value = Exhaustive(weights, values, W)
    print("best solution:", best_solution, "\nmax value:", max_value)

    print('_' * 100, "\nGreedy by value :")
    best_solution, max_value = greedy_by_value(weights, values, x, W)
    print("best solution:", best_solution, "\nmax value:", max_value)

    print('_' * 100 , "\nRandom binary generation :")
    val , solution = generate_random_solution(weights, values)
    print("solution:", solution, "\nvalue:", val)

    

except Exception as e:
    print("An error occurred:", e)
