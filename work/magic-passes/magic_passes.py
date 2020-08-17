from typing import List


class MagicPasses:
    
    def get_magic_count(self, number: int) -> List:
        """Given a number it returns the magic count including the magic words
        'abracadabra' for numbers multiple of three, 'alakazam' for numbers
        multiple of five, and 'abracadabraalakazam' for numbers multiple of
        three and five

        Params:
            - number: int

        Return:
            List of numbers and strings
        """
        numbers_list = range(number + 1)[1:]
        magic_count = list()

        for number in numbers_list:
            if self._is_multiple_of_three(number) and self._is_multiple_of_five(number):
                magic_count.append("abracadabraalakazam")
                continue

            if self._is_multiple_of_three(number):
                magic_count.append("abracadabra")
                continue

            if self._is_multiple_of_five(number):
                magic_count.append("alakazam")
                continue

            magic_count.append(number)

        return magic_count
    
    def _is_multiple_of_three(self, number: int) -> bool:
        """Given a number it returns True if the number is
        multiple of three

        Params:
            - number: int

        Return:
            Boolean
        """
        return number % 3 == 0
    
    def _is_multiple_of_five(self, number: int) -> bool:
        """Given a number it returns True if the number is
        multiple of five

        Params:
            - number: int

        Return:
            Boolean
        """
        return number % 5 == 0
