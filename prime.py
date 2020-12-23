for i in range (100):
    p=[]
    for j in range (2,i):
        if i%j ==0 :
            p.append(j)
    if len(p)==0:
        print (i)
        
