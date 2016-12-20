#!/usr/bin/env python

class Rogue:
    def compute_next(self, prev_row):
        max_cols = len(prev_row)
        cur_row = []
        for i in xrange(max_cols):
            left = '.'
            if i > 0: 
                left = prev_row[i-1]
            
            center = prev_row[i]
            
            right = '.'
            if i < max_cols-1:
                right = prev_row[i+1]

            is_trap = \
                (left == '^' and center == '^' and right != '^') or \
                (center == '^' and right == '^' and left != '^') or \
                (left == '^' and center != '^' and right != '^') or \
                (left != '^' and center != '^' and right == '^')
            if is_trap:
                cur_row.append('^')
            else:
                cur_row.append('.')
        return ''.join(cur_row)
        

    def compute_safe(self, tiles):
        """ Returns number of safe tiles """
        return len(filter(lambda x: x == '.', tiles))



if __name__ == '__main__':
    # Read Input
    tiles = ''
    with open('d18.txt') as fp:
        tiles = fp.read().strip()

    r = Rogue()
    # Initialise with number of safe tiles in the input
    num_safe = r.compute_safe(tiles)

    for x in xrange(400000-1): # Change this to match number of lines to be output
        tiles = r.compute_next(tiles)
        num_safe += r.compute_safe(tiles)
    
    print num_safe