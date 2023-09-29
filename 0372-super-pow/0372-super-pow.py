class Solution(object):
    def superPow(self, a, b):
        return (a % 1337)**(1140 + int(''.join(map(str, b))) % 1140) % 1337
        # """
        # :type a: int
        # :type b: List[int]
        # :rtype: int
        # """
        # if a>2**31-1:
        #     return 0
        # po = b[0]
        # for i in range(1,len(b)):
        #     po *=10
        #     po+=b[i]
        # print(po)    
        # return pow(a,po)
  