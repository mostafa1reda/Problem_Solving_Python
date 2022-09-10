def solution(l,t):
        
    result = [-1,-1]
    dict={}
    
    for index,e in enumerate(l):       
        if(e== t):
            return index,index
        for i in list(dict):
            new = (i+e)
            if( new <= t ):
                dict[i+e] = dict[i] + 1
                del dict[i]
            if(new>t):
                del dict[i]
            if(new==t):
                result = [index +1  - dict[t] ,index ]             
                del dict[t]
                return result

        if(e<t):
            dict[e]=1    

    return result

################TEST CASES######################
# solution([1,15,3,4],15)
# solution([2,3,3,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8],12)
# solution([2,3,3,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8,3,3,7,8,9,3,2,1,10,9,2,2,8,18,10,2,2,8],12)
# solution([1,2,3,4],15)
# solution([1,268,52,595],269)

##################### OLD SOLUTIONS VERSIONS (NON OPTIMIZED) #######################################
#1 --STATIC
"""
def solution(Nlist,key):
    total=0
    dummy_list = []
    for i in Nlist:
        total += i
        #if total == key:
        curr_ind = Nlist.index(i)
        dummy_list.append(curr_ind)
        #print(curr_ind)
        #print(dummy_list)
        yield total
        if total == key:
            max_ind = Nlist.index(i)
            if max_ind == max(dummy_list):
                print([int(x) for x in str(dummy_list[0])+str(dummy_list[-1])])
        #elif total != key:
            #print([-1,-1])
"""
#2 --Does NOT Return the first shortest path  
"""
def solution(l,t):
    #l=[1,2,2,3,2,2,1]

    result = [-1,-1]
    #t = 5
    dict={}
    best_match = 1000

    for index,e in enumerate(l):       

        for i in list(dict):
            new = (i+e)
            if( new <= t ):
                dict[i+e] = dict[i] + 1
                del dict[i]
            if(new>t):
                del dict[i]
            if(new==t):
                if(dict[t]<best_match):
                    best_match = dict[t]
                    result = [index +1  - dict[t] ,index ]             
                    del dict[t]

        if(e<t):
            dict[e]=1    

    return result
"""    
