class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        visited = []
        visiting = []
        for path in paths:
            visited.append(path[0])
            visiting.append(path[1])
        for city in visiting:
            if city not in visited:
                return city
        
