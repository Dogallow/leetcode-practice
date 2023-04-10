def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        prefix = ""

        longest_possible_prefix = min([len(word) for word in strs])
        if longest_possible_prefix == 0:
            return ""

        index = 0
        word = 0
        tmp = None
        
        while index < longest_possible_prefix:
            if tmp:
                if tmp != strs[word][index]:
                    return prefix
            
            tmp = strs[word][index]

            word += 1
            if word == len(strs):
                word = 0
                index += 1
                prefix += tmp
                tmp = None
        
        return prefix
