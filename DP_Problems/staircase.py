def ways(steps,target):
    dp = [0]*(target+1)
    dp[0]=dp[1]=1
    for i in range(2,target+1):
        for x in steps:
            if x<=i:
                dp[i] = dp[i] + dp[i-x]
    print(dp[target])
steps = [1,2]
ways(steps,7)