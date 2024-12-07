
import copy


def Exhaustive (J) :

    def fetness(s) : # o( n * m)

        n = len(s);
        m = len(J[0]);
        EX = [];
        ST = [[0] * m for _ in range(n)]
    
        for i in range(0 , n) :
            EX.append(J[s[i] - 1])

        for i in range(0 , n) :
           for j in range(0 , m) :
               if i == 0 and j == 0 :
                   ST[i][j] = 0;
               elif i == 0 :
                   ST[i][j] = ST[i][j-1] + EX[i][j-1];
               elif j == 0 : 
                   ST[i][j] = ST[i-1][j] + EX[i-1][j];
               else :
                    ST[i][j] = max(EX[i-1][j] + ST[i-1][j], EX[i][j-1] + ST[i][j-1])

        
        makespan = ST[-1][-1] + EX[-1][-1]; 
        return makespan;

    
    s = list(range(1, len(J) + 1))
    
    min_makspan = fetness(s);
    best_seq = s;
    search_space = []
    def back (path) :
        nonlocal min_makspan;
        nonlocal  best_seq;
        
        if len(path) == len(s):
            search_space.append(copy.deepcopy(path))
            current_fitness = fetness(path)
            
            
            # print(path ,"=>", min_makspan, "\n",path , "=>",  current_fitness , "\n min_makspan :" , min_makspan,"\n" ,'_' * 100)
            if current_fitness <= min_makspan:
                min_makspan = current_fitness

                best_seq = copy.deepcopy(path)
                return;
       
        for num in s:
            if num not in path : 
                path.append(num)  
                back(path);
                path.pop();
        
        
    back([])
    
    return best_seq , min_makspan , search_space ;





def NEH(J) : 
    s = list(range(1, len(J) + 1))

    def fetness(s) : # o( n * m)

        n = len(s);
        m = len(J[0]);
        EX = [];
        ST = [[0] * m for _ in range(n)]
    
        for i in range(0 , n) :
            EX.append(J[s[i] - 1])

        for i in range(0 , n) :
           for j in range(0 , m) :
               if i == 0 and j == 0 :
                   ST[i][j] = 0;
               elif i == 0 :
                   ST[i][j] = ST[i][j-1] + EX[i][j-1];
               elif j == 0 : 
                   ST[i][j] = ST[i-1][j] + EX[i-1][j];
               else :
                    ST[i][j] = max(EX[i-1][j] + ST[i-1][j], EX[i][j-1] + ST[i][j-1])


        
        
        makespan = ST[-1][-1] + EX[-1][-1]; 
        return makespan;

    search_space = [];
    def sort_Jobs_by_time (J) :
        from functools import reduce
        times = list(map(lambda lis: reduce(lambda x , y : x + y , lis) , J))
        sortedTime = sorted(zip(s, times), key=lambda x: x[1], reverse=True)
        L , _ = zip(*sortedTime)
        return list(L);



    def min_sequence (L , j) :
       
        n = len(L)
        min_seq =  L + [j] 
       

        for i in range(0 , n + 1) : # o(n)
            s = L[:i] + [j] + L[i:]
            
          
            search_space.append(s)

            current_makespan = fetness(s)
            if current_makespan < fetness(min_seq) : 
                min_seq = s;
        
        return min_seq;


    n = len(sort_Jobs_by_time(J))
    L = sort_Jobs_by_time(J);
    seq = [L[0]]
    for i in range(1 , n) : # o (n)
        seq = min_sequence(seq , L[i])
 

    # print(" search_space ::" ,  search_space)
    return seq , fetness(seq) , search_space






try :

    J = [[5 ,9, 8, 10, 1], [9, 3, 10, 1, 8] , [9 ,4 ,5 ,8 ,6 ] , [4 ,8, 8, 7, 2]]  

    print("_" * 150 ,"\nExhaustive : ")
    solution , makespan ,search_space  = Exhaustive(J)
    print("searchs Space (Espace de recherche) :" , search_space ,"\nsequence : ", solution , '\nmakespan :', makespan, '\nComplexity : O(n!)')
        
    print( "_" * 150 ,"\nNEH : ")
    solution , makespan , search_space = NEH(J);
    print("searchs Space (Espace de recherche) :" , search_space ,"\nsequence :", solution , '\nmakespan :', makespan, '\nComplexity : O( n^3 * m)')

except Exception as e:
    print("error :", e)
































