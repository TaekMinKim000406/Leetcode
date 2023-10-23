class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        # self.current = []
        # self.available=[i for i in range(n)]
        self.n = n
        self.students = []



    def seat(self):
        """
        :rtype: int
        """
        if len(self.students)==0:
            # self.available.remove(0)
            # self.current.append(0)
            self.students.append(0)
            return 0    
        # elif len(self.available)==0:
        #     return
        else:
            max_distance, seat = self.students[0], 0
            for i in range(1, len(self.students)):
                distance = (self.students[i] - self.students[i-1]) // 2
                if distance > max_distance:
                    max_distance = distance
                    seat = self.students[i-1] + distance
            if self.n - 1 - self.students[-1] > max_distance:
                seat = self.n - 1
            bisect.insort(self.students, seat)  # 새로운 학생을 좌석 리스트에 삽입
            return seat
        #     distance = [-1]
        #     index = [-1]    
        #     for ind in self.available:
        #        dis = [len(self.available)]
        #        for ind2 in self.current:
        #            dis[0] = min(dis[0], abs(ind2-ind))
        #        if dis[0]>distance[0]:
        #            distance[0] = dis[0]
        #            index[0] = ind 
        #     self.available.remove(index[0])
        #     self.current.append(index[0])
        #     return index[0]

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.students.remove(p)
        # if p in self.current:
        #     self.current.remove(p)
        #     self.available.append(p)
        #     self.available.sort()

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)