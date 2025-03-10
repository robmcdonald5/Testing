class Solution:
    def candy(self, ratings: List[int]) -> int:
        demand_list = [1] * len(ratings)
        
        # left to right pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                demand_list[i] = demand_list[i-1] + 1

        # right to left pass
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                demand_list[i] = max(demand_list[i], demand_list[i+1] + 1)

        return sum(demand_list)