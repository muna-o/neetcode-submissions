class Solution:
    def reverseBits(self, n: int) -> int:
        binary_representation = bin(n)
        reverse_representation = binary_representation[::-1]

        reverse_representation = reverse_representation[0:-2]


        length = len(reverse_representation)
        reverse_representation = reverse_representation + '0' * (32 - length)

        return int(reverse_representation, 2)
        