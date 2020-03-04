void RMQ(int num) //预处理->O(nlogn)
{
    for(int j = 1; j < 20; ++j)    // 这里j的范围根据具体题目数据定义
        for(int i = 1; i <= num; ++i)    // num为数组内整数的个数
            if(i + (1 << j) - 1 <= num)
            {
                maxsum[i][j] = max(maxsum[i][j - 1], maxsum[i + (1 << (j - 1))][j - 1]);
                minsum[i][j] = min(minsum[i][j - 1], minsum[i + (1 << (j - 1))][j - 1]);
            }
}