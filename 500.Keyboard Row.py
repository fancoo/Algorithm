class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alphabet_list = [('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'),
                         ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'),
                         ('z', 'x', 'c', 'v', 'b', 'n', 'm')]

        results = []
        for word in words:
            char_list = list(word.lower())
            if len(char_list) == 0:
                continue
            if len(char_list) == 1:
                results.append(word)
                continue
            first = char_list[0]

            contain_index = -1
            for index, alphabet_set in enumerate(alphabet_list):
                if first in alphabet_set:
                    contain_index = index
                    break

            if contain_index >= 0:
                contain_flag = 1
                for char in char_list[1:]:
                    if char not in alphabet_list[contain_index]:
                        contain_flag = 0
                        break
                if contain_flag:
                    results.append(word)
                    continue

        return results

