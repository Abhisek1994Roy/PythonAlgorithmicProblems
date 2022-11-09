class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a_list = list(range(1, n + 1))
        index = 0

        def findwinner(k, index, a_list, val):
            if len(a_list) == 1:
                val = a_list[0]
                return val

            position_to_delete = (index + k) % len(a_list)

            a_list.pop(position_to_delete)
            return findwinner(k, position_to_delete, a_list, val)

        return findwinner(k - 1, index, a_list, 0)