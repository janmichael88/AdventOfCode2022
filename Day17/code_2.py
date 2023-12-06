'''
this is simulation problem, the hardest part of coding the game API.....
we are given the following blocks

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

and an input of ><><>, which idnicates the movemnt of the block 1 unit
blocks always appear 3 units above the highest block
return the height of the block after 2022 blocks have fallen

no way in hell im going to be able to code up a game state i've never seen before
better to just learn it
https://github.com/camaron-ai/adventofcode-2022/blob/main/day17/main.py
'''
from dataclasses import dataclass
from email.header import decode_header
from typing import List
from collections import defaultdict

RAW_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

#we are going to use masking to respersnet states for the game
#this of these as bit positions
LEFT_DISTANCE = 2
HEIGHT_DISTANCE = 3
WIDTH = 7
RIGHT_EDGE_MASK = 1
LEFT_EDGE_MASK = 1 << (WIDTH - 1)

#mask to shift rocks
def shift_mask(mask: int, direction: int):
    if direction > 0:
        return mask >> 1
    elif direction < 0:
        return mask << 1

@dataclass
class Rock:
    masks: List[int]

    def shift(self, direction: int) -> 'Rock':
        #if we were to shift a rock in the positive direction check if causing a shift forces meet an edge
        #if it were to reach an edge, just return the rock's mask
        if any(m & RIGHT_EDGE_MASK for m in self.masks) and direction == 1:
            return self
        elif any(m & LEFT_EDGE_MASK for m in self.masks) and direction == -1:
            return self
        #otherwise shift the rock and return the new mask
        shifted_masks = [shift_mask(mask, direction) for mask in self.masks]
        return Rock(shifted_masks)

    @staticmethod
    def from_binary(bit_matrix: List[int]) -> 'Rock':
        #convert bit masks to intergers taking into account the stating positions 
        masks = []
        for bits in bit_matrix:
            x = 0
            for i, b in enumerate(bits):
                x += b << (WIDTH - LEFT_DISTANCE - i - 1)
            masks.append(x)
        return Rock(masks)
            

ROCK_M = [
    [[1, 1, 1, 1]],
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
    [[1], [1], [1], [1]],
    [[1, 1], [1, 1]],
]

ROCKS = [Rock.from_binary(m) for m in ROCK_M]

'''
for r in ROCKS:
    print(r)
'''