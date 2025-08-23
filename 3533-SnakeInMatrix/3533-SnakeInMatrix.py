# Last updated: 8/22/2025, 11:34:02 PM
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0 # Left Right
        j = 0 # Up Down

        for command in commands:
            if command == 'RIGHT':
                i += 1
            elif command == 'LEFT':
                i -= 1 
            elif command == 'UP':
                j -= 1
            elif command == 'DOWN':
                j += 1

            print(command)
            print(i, j)
            
        return ((j * n) + i)
