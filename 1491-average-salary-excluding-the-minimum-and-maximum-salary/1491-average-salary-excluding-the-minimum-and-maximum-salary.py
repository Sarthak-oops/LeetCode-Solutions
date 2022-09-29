class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        maxi=max(salary)
        mini=min(salary)
        s=sum(salary)
        s=s-maxi-mini
        avg=s/(n-2)
        return avg