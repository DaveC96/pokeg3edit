# Docs:
# https://bulbapedia.bulbagarden.net/wiki/Character_encoding_in_Generation_III
#
# This should probably be rewritten as a proper codec. (#TODO)
import sys
import string

POKESTR_LUT = {
#   ASCII   Pokestr bytes
                "0" : 0xA1, "1" : 0xA2, "2" : 0xA3, "3" : 0xA4, "4" : 0xA5, "5" : 0xA6, "6" : 0xA7,
    "7" : 0xA8, "8" : 0xA9, "9" : 0xAA, "!" : 0xAB, "?" : 0xAC, "." : 0xAD, "-" : 0xAE,
    
    "," : 0xB8,             "/" : 0xBA, "A" : 0xBB, "B" : 0xBC, "C" : 0xBD, "D" : 0xBE, "E" : 0xBF,
    "F" : 0xC0, "G" : 0xC1, "H" : 0xC2, "I" : 0xC3, "J" : 0xC4, "K" : 0xC5, "L" : 0xC6, "M" : 0xC7,
    "N" : 0xC8, "O" : 0xC9, "P" : 0xCA, "Q" : 0xCB, "R" : 0xCC, "S" : 0xCD, "T" : 0xCE, "U" : 0xCF,
    "V" : 0xD0, "W" : 0xD1, "X" : 0xD2, "Y" : 0xD3, "Z" : 0xD4, "a" : 0xD5, "b" : 0xD6, "c" : 0xD7,
    "d" : 0xD8, "e" : 0xD9, "f" : 0xDA, "g" : 0xDB, "h" : 0xDC, "i" : 0xDD, "j" : 0xDE, "k" : 0xDF,
    "l" : 0xE0, "m" : 0xE1, "n" : 0xE2, "o" : 0xE3, "p" : 0xE4, "q" : 0xE5, "r" : 0xE6, "s" : 0xE7,
    "t" : 0xE8, "u" : 0xE9, "v" : 0xEA, "w" : 0xEB, "x" : 0xEC, "y" : 0xED, "z" : 0xEE
}

def encode(instring: str) -> bytearray:
    for char in instring:
        if char not in POKESTR_LUT:
            raise ValueError(f"Text ({instring}) contains invalid characters")
    #   --
    encoded = bytearray()
    for char in instring:
        encoded.append(POKESTR_LUT[char])
    #   --
    encoded.append(0xFF)    # Terminator
    return encoded


def decode(instring: bytearray) -> str:
    decoded = []
    for byte in instring:
        if byte == 0xFF:
            break
        else:
            keys = list()
            items = POKESTR_LUT.items()
            for item in items:
                if item[1] == byte:
                    decoded.append(item[0])
    return "".join(decoded)