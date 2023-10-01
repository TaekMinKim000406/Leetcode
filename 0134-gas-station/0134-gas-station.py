class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0  # 총 가스 양
        current_gas = 0  # 현재 가스 양
        start_index = 0  # 시작 인덱스

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            # 현재 가스 양이 음수가 되면 출발 지점을 현재 인덱스의 다음으로 설정
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        # 총 가스 양이 0 이상인 경우 출발 지점이 존재함
        if total_gas >= 0:
            return start_index
        else:
            return -1


        # #시간 초과
        # index = []
        # for i in range(len(gas)):
        #     if cost[i]>gas[i]:
        #         continue

        #     cur_gas = 0
        #     for j in range(0,len(gas)):
        #         cur_gas += gas[(i+j)%len(gas)]   
        #         cur_gas -= cost[(i+j)%len(gas)]
                 
        #         if cur_gas<0:
        #             break
        #     if cur_gas>=0:
        #         index.append(i)

        # if len(index)>0:
        #     return index[0]
        # else:
        #     return -1    