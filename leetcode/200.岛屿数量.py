#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # 图的基本算法
        # 本题为计算图中的联通图的总数
        # 在一个无向图中找连通图的数量

        # 本题就是在一个无向图中寻找连通分量的总数

        # 图的DFS depth
        # 1. 找到一个顶点为起始点
        # 2. 


        # 图的BFS breadth

        # class Solution {
            # public:
            # int numIslands(vector<vector<char>>& grid) {
            #     int nr = grid.size();
            #     if (!nr) return 0;
            #     int nc = grid[0].size();

            #     int num_islands = 0;
            #     for (int r = 0; r < nr; ++r) {
            #     for (int c = 0; c < nc; ++c) {
            #         if (grid[r][c] == '1') {
            #         ++num_islands;
            #         grid[r][c] = '0'; // mark as visited
            #         queue<pair<int, int>> nei***ors;
            #         nei***ors.push({r, c});
            #         while (!nei***ors.empty()) {
            #             auto rc = nei***ors.front();
            #             nei***ors.pop();
            #             int row = rc.first, col = rc.second;
            #             if (row - 1 >= 0 && grid[row-1][col] == '1') {
            #             nei***ors.push({row-1, col}); grid[row-1][col] = '0';
            #             }
            #             if (row + 1 < nr && grid[row+1][col] == '1') {
            #             nei***ors.push({row+1, col}); grid[row+1][col] = '0';
            #             }
            #             if (col - 1 >= 0 && grid[row][col-1] == '1') {
            #             nei***ors.push({row, col-1}); grid[row][col-1] = '0';
            #             }
            #             if (col + 1 < nc && grid[row][col+1] == '1') {
            #             nei***ors.push({row, col+1}); grid[row][col+1] = '0';
            #             }
            #         }
            #         }
            #     }
            #     }

            #     return num_islands;
            # }
            # };

            # 广度优先：
            
            # 遍历数组从第一个点开始找到第一个不为0的点
            
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # start BFS

                    queue = [(i, j)]
                    # order > left - up - right - down
                    while queue:
                        v_i, v_j = queue.pop(0)
                        grid[v_i][v_j] = "0"
                        if v_j > 0:                                                                               
                            if grid[v_i][v_j - 1] == "1": queue.append((v_i, v_j - 1)); grid[v_i][v_j - 1] = "0"  
                        if v_i > 0:                                                                               
                            if grid[v_i - 1][v_j] == "1": queue.append((v_i - 1, v_j)); grid[v_i - 1][v_j] = "0"  
                        if v_j < len(grid[0]) - 1:                                                                
                            if grid[v_i][v_j + 1] == "1": queue.append((v_i, v_j + 1)); grid[v_i][v_j + 1] = "0"  
                        if v_i < len(grid) - 1:                                                                   
                            if grid[v_i + 1][v_j] == "1": queue.append((v_i + 1, v_j)); grid[v_i + 1][v_j] = "0"  
                    
                    result += 1

        return result


# @lc code=end

"""
https://github.com/adamyanna/StayCompetitiveAlgorithm/tree/main/roadmap/6_graphs
"""