class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        
        merged = False
        
        temp = []
        
        for i in intervals:
            #start값이 크지만 제일 가까운 위치를 찾아서 추가한다.
            if not merged and newInterval[0] < i[0]:
                temp.append(newInterval)
                merged = True
            
            temp.append(i)

        #case: 겹치지 않는 경우    
        if not merged:
            temp.append(newInterval)

        res = []
         

        for i in temp:
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(i[1], res[-1][-1])
            
            else:
                res += [i]
        return res




        # if len(intervals)==0:
        #     return [newInterval]

        # before = intervals

        # for i in range(len(intervals)):
        #     start = intervals[i][0]
        #     end = intervals[i][1]
        #     #case1: 겹치지 않는경우
        #     if i<len(intervals)-1 and end<newInterval[0] and newInterval[0]<intervals[i+1][0]:
        #         intervals.append(newInterval)
        #         break
        #     elif i == len(intervals)-1 and end<newInterval[0]:
        #         intervals.append(newInterval)
        #         break
        #     elif i == 0 and  newInterval[0] < intervals[i][0]:
        #         intervals.append(newInterval)
        #         break
        #     elif end<newInterval[0] or start>newInterval[1]:
        #         continue
        #     #case2: 포함하는 경우
        #     elif end>=newInterval[1] and start<=newInterval[0]:
        #         break
        #     #case3: 일부만 겹치는 경우 
        #     elif end>=newInterval[1]:
        #         intervals[i][0]=newInterval[0]
        #     elif start<=newInterval[0]:
        #         intervals[i][1]=newInterval[1]
        # print(intervals)
        # #범위 조정
        
        # if len(intervals)==1:
        #     return intervals

        # end_value = intervals[len(intervals)-1][1]
        # i = 0
        # while True:
        #     if intervals[i][1]>=intervals[i+1][0]:
        #         intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
        #         intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
        #         intervals.remove(intervals[i+1])
        #     else:    
        #         i+=1 
        #     if intervals[i][1] == end_value or intervals[i+1][1] == end_value:
        #         break
            


        # return intervals

