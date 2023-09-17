class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # #이거는 한번만 선택하는 경우
        # min_price = prices[0]
        # max_profit = 0
        # for i in range(len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i]-min_price)
        # return max_profit

        # #메모리 초과
        # costs = []
        # def choose(cost, i, price):
        #     if i>len(prices)-1:
        #         return cost

        #     if price >= 0:
        #         costs.append(choose(cost, i+1, price)) #팔지 않는다.
        #         costs.append(choose(cost+prices[i]-price,i+1,-1)) #판다
        #     else:
        #         costs.append(choose(cost, i+1, prices[i]))
        #         costs.append(choose(cost, i+1, -1))
                

        # choose(0,0,-1)       
        # return max(costs) 


        n = len(prices)
        memo = [[-1] * 2 for _ in range(n)]
        
        def choose(i, has_stock):
            if i >= n:
                return 0
            
            if memo[i][has_stock] != -1:
                return memo[i][has_stock]
            
            if has_stock:
                memo[i][has_stock] = max(prices[i] + choose(i+1, False), choose(i+1, True))
            else:
                memo[i][has_stock] = max(-prices[i] + choose(i+1, True), choose(i+1, False))
            
            return memo[i][has_stock]
        
        return choose(0, False)

