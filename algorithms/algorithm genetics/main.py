

import random

def algorithme_genitice (values , W , weights , number_population) :
  
  n = len(values)


  def fitness (s) : 
    if len(s) == 0 : return 0;
    n = len(s);
    sum = 0;
    for i in range(n) :
        sum += s[i] * values[i];
    return sum;



  def is_valid (s) :
    sum = 0;
    n = len(s);
    for i in range(n) :
      sum += s[i] * weights[i];
      if sum > W :return False;
    return sum <= W;


       
  def generate_random_population(num_population) :
    Population = [];
    while len(Population) < num_population  :
        random_num = random.randint(0, 2 ** n - 1 );
        chromosome = bin(random_num)[2:].zfill(n);
        chromosome = [int(digit) for digit in str(chromosome)]
        if is_valid(chromosome) : 
            Population.append(chromosome)

    print("popultion : " , Population)        
    return sort_by_value(Population);



  y = 0;
  def sort_by_value (Population) :
     nonlocal y
     values = map(lambda c : fitness(c) ,Population)
     values = list(values)
     
     zipped = sorted(zip(values, Population), reverse=True)
     sorted_values , sorted_population = zip(*zipped);
     sorted_population , sorted_values= list(sorted_population) , list(sorted_values)
     y = y + 1;
     
     print("_" * 150)
     print("Generation {}".format(y) , " : \n Population : ", sorted_population[:number_population]  ,"\n values : " , sorted_values[:number_population])
     
     return sorted_population[:number_population] 
     

  def apply_crossover(Population) :
      
      n = len(Population[0])
      for i in range(0 , n , 2) :
        p1 = Population[i]
        p2 = Population[i + 1]
        k = random.randint(1, len(p1) - 1);
        c1 = []
        c2 = []

        for j in range(n) :
          if j < k :
            c1.append(p1[j])
            c2.append(p2[j])
          else :
            c1.append(p2[j])
            c2.append(p1[j])
        if is_valid(c1):  
            Population.append(c1)
        if is_valid(c2): 
            Population.append(c2)
  
        sorted_population = sort_by_value(Population)
        return sorted_population[:number_population]



  population = generate_random_population(number_population)
  x = 0;
  while True:
    x+=1;
    population = apply_crossover(population);
    
    if abs(fitness(population[0]) - fitness(population[-1])) / fitness(population[0]) < 0.01 or x > 30 :
       break;
     
     
  



W = 60;
weights = [5 , 20 , 22 , 8 , 10  , 15]
values =  [10 , 42 , 45 , 19 , 21 , 78 ]
number_population = 6;

algorithme_genitice(values , W , weights , number_population);

 
        




  
        
        
        
        
     
     