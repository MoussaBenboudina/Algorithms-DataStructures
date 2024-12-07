
def isValid(weights, x, W):

    if W < 0: return False 

    n = len(weights) 
    sumWeight = 0 

    for i in range(0, n): 
        sumWeight += weights[i] * x[i]
        if sumWeight > W:
            return False;
        
    return sumWeight <= W 




def fitness(values, x):
    n = len(values);
    sum = 0
    for i in range(0, n):
        sum += values[i] * x[i]
    return sum




def greedy_by_value(weights , values , x , W) :

    if len(weights) == 0 or len(values) == 0 or W <= 0: 
       print(' weight and values cannot be empty')
       return;
 
    n = len(weights)
  

    sorted_pairs = sorted(zip(values, weights), reverse=True)
    values_sorted, weights_sorted = zip(*sorted_pairs)
    values_sorted ,   weights_sorted = list(values_sorted) , list(weights_sorted)
 

    for i in range(0 , n) : 
      x[i] = 1;
      if not isValid(weights_sorted , x, W) :
          x[i] = 0;
  

    print(x)
    return x , fitness(values , x) ;





def greedy_by_ratio (weights , values , x , W) :

    if len(weights) == 0 or len(values) == 0 or W <= 0: 
       print(' weight and values cannot be empty')
       return;

    n = len(weights);
    ratio = []

    for i in range(0 , n) :
        ratio.append(values[i] / weights[i]);
    
    sorted_pairs = sorted(zip(values, weights , ratio),key=lambda x : x[2] , reverse=True);
    values_sorted , weight_sorted , ratio_sorted = zip(*sorted_pairs);
    values_sorted , weight_sorted , ratio_sorted =   list(values_sorted) , list(weight_sorted) , list(ratio_sorted) 
    # print("values_sorted :" , values_sorted , "\nweight_sorted  : " , weight_sorted  , "\nratio_sorted : " , ratio_sorted ) 
    for i in range(0 , n) :
        x[i] = 1;
        if not isValid(weights , x , W) :
            x[i] = 0;
      
    
    return  x , fitness(values , x);




    

def generate_random_solution(weights , values , W):
    
    if len(weights) == 0 or len(values) == 0 or W <= 0: 
       print(' weight and values cannot be empty')
       return;

    import random
    n = len(weights)
    while  True : 
        random_binary = list(map(int , bin(random.randint(0, (1 << n) - 1))[2:].zfill(n)))
        if isValid(weights , random_binary ,W) :
             return fitness(values , random_binary) , random_binary



def Exhaustive(weights, values, W):
    
    if len(weights) == 0 or len(values) == 0 or W <= 0: 
       print(' weight and values cannot be empty')
       return;

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



def dynamic_programming (weights, values, W) :

    n = len(weights);
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1,n + 1) :
        for j in range(1 , W +1) :
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j];
   
    return dp ,dp[-1][-1]
            








import random
import time

n = 20
weights = [random.randint(1, 10) for _ in range(n)]
values = [random.randint(1, 50) for _ in range(n)]
x = [0] * len(values)
W = 50

print("weights:", weights)
print("values:", values)
print("max weight:", W)


try:
    print('_' * 100, "\nExhaustive (optimal global) :")
    start_time = time.time()
    best_solution, max_value = Exhaustive(weights, values, W)
    end_time = time.time()
    print("best solution:", best_solution, "\nmax value:", max_value, "\nComplexity : O(2^n)")
    print(f"execution time: {end_time - start_time:.6f} seconds")

    print('_' * 100, "\nGreedy by value :")
    start_time = time.time()
    best_solution, max_value = greedy_by_value(weights, values, x, W)
    end_time = time.time()
    print("best solution:", best_solution, "\nmax value:", max_value, "\nComplexity : O(nlog(n))")
    print(f"execution time: {end_time - start_time:.6f} seconds")

    print('_' * 100, "\nGreedy by ratio :")
    start_time = time.time()
    best_solution, max_value = greedy_by_ratio(weights, values, x, W)
    end_time = time.time()
    print("best solution:", best_solution, "\nmax value:", max_value, "\nComplexity : O(nlog(n))")
    print(f"execution time: {end_time - start_time:.6f} seconds")


    print('_' * 100, "\nDybnamic programing :")
    start_time = time.time()
    solution , val = dynamic_programming(weights, values, W);
    end_time = time.time()
    print("\nvalue:", val , "\nComplexity : O(n * W)")
    print(f"executiom time: {end_time - start_time:.6f} seconds")


    print('_' * 100, "\nRandom :")
    start_time = time.time()
    val, solution = generate_random_solution(weights, values, W)
    end_time = time.time()
    print("solution:", solution, "\nvalue:", val)
    print(f"executiom time: {end_time - start_time:.6f} seconds")

except Exception as e:
    print("error :", e)
