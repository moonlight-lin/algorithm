'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) == 0:
            return []
            
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda a : a[0])
        
        result = []
        
        merge = None
        for interval in intervals:
            if merge is None:
                merge = interval
                continue
                
            if merge[1] >= interval[0]:
                if merge[1] < interval[1]:
                    merge[1] = interval[1]
            else:
                result.append(merge)
                merge = interval
        
        result.append(merge)
        return result