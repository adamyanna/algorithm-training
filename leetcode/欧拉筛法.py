    prime=[0 for i in range(n+1)]         #全部初始化为0
    common=[]                                   #存放素数
    for i in range(2,n+1):                     #开筛了！！
        if prime[i]==0: 
            common.append(i)      
        for j in common:
            if i*j>n:
                break
            prime[i*j]=1
            if i%j==0:                          #这句是最有意思的地方  下面解释
                break;
    return common