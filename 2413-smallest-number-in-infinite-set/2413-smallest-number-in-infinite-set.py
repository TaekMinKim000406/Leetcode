class SmallestInfiniteSet(object):

    def __init__(self):
        self.nums = [i for i in range(1,1001)]
        
    def popSmallest(self):
        """
        :rtype: int
        """

        self.nums.sort()
        return self.nums.pop(0)
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.nums:
            self.nums.append(num)


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)