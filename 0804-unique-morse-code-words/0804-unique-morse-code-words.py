class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # Create a dictionary that maps letters to Morse code
        join = dict(zip(alphabets,morse_code))

        answer = set()

        for word in words:
            j = ""

            for i in word:
                j += join[i]

            answer.add(j)

        return len(answer)
  