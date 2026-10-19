class Solution:
    def numberOfOneBits(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            answer.append(self.numberOfOneBits(i))
        return answer

        