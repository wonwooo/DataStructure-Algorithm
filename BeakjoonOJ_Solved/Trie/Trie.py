class Trie:
    head = {}
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]

        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False



