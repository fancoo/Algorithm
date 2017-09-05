class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_list = []
        s_list.append(s)

        if self.isParenthesesValid(s):
            return s_list

        # pre-cut


        part_set = set()
        part_set.add(s)
        second_set = part_set
        flag = 0
        min_list = []
        while (len(second_set)):
            second_set = set()
            for item in part_set:
                for j in xrange(len(item)):
                    if (item[j] != '(') and (item[j] != ')'):
                        continue
                    less_part_s = item[0:j] + item[j + 1:]
                    if (less_part_s):
                        if '(' in less_part_s and ')' in less_part_s:
                            second_set.add(less_part_s)
                            if self.isParenthesesValid(less_part_s):
                                flag = 1
                                if less_part_s not in min_list:
                                    min_list.append(less_part_s)
            if (flag == 1):
                return min_list
            part_set = second_set

        if not len(min_list):
            clean_s = s.replace("(", '').replace(")", '')
            min_list.append(clean_s)
        return min_list

    def isParenthesesValid(self, s):
        flag = 0
        symbol_list = list(s)
        for symbol in symbol_list:
            if (symbol != '(') and (symbol != ')'):
                continue
            if symbol == '(':
                flag += 1
            if symbol == ')':
                flag -= 1
            if flag < 0:
                return False
        if flag == 0:
            return True
        return False


'''
Test Case
"()())()"
"(a)())()"
")("
"(((k()(("
"()(((((((()"
")()()i)())b(())h))))"
"("
"x("
'''