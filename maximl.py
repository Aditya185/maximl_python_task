from collections import defaultdict 
  


def minString(str): 
      
    n = len(str) 
      
   
    dist_count = len(set([x for x in str])) 
      
    curr_count = defaultdict(lambda: 0) 
    count = 0
    start = 0
    min_len = n 
      
   
    for j in range(n): 
        curr_count[str[j]] += 1
          
      
        if curr_count[str[j]] == 1: 
            count += 1
              
      
        if count == dist_count: 
            while curr_count[str[start]] > 1: 
                if curr_count[str[start]] > 1: 
                    curr_count[str[start]] -= 1
                      
                start += 1
                  
           
            len_window = j - start + 1
              
            if min_len > len_window: 
                min_len = len_window 
                start_index = start 
  
    
    return min_len
                                   

if __name__=='__main__': 
      s = input()
      print(minString(s))

