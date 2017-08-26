class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True

        bin_str = bin(num).replace('0b', '')
        # Though here I do not delete '0' before '1', it's ok and faster(42ms->38ms)
        bin_str = bin_str.replace('1', '', 1)
        if '1' in bin_str:
            return False

        remain_list = list(bin_str)
        zero_len = len(remain_list)
        if zero_len and zero_len % 2 == 0:
            return True
        return False
