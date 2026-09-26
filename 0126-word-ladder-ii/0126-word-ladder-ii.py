class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordset = set(wordList)

        if endWord not in wordset:
            return []

        parent = defaultdict(list) 
        current = {beginWord}
        found = False

        while current and not found:
            #Current level ke words ko remove karo
            wordset -= current

            next_level = set()

            for word in current:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in wordset:
                            next_level.add(new_word)
                            parent[new_word].append(word)
                        elif new_word in next_level:
                            parent[new_word].append(word)

            if endWord in next_level:
                found = True

            current = next_level

        if not found:
            return []

        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for p in parent[word]:
                path.append(p)
                dfs(p)
                path.pop()
        
        dfs(endWord)

        return result