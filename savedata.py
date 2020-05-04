# Handy docs:
# https://bulbapedia.bulbagarden.net/wiki/Save_data_structure_in_Generation_III

class Datablock:
    MAXSIZE = 3968
    def __init__(self, blockid: int, blockname: str, offset: int, length: int):
        self.id     = blockid
        self.name   = blockname
        self.offset = offset
        self.length = length
        self.data   = bytearray()

class Data_trainerinfo(Datablock):
    def __init__(self):
        super().__init__()
        self.memorymap = {
        #   Attribute Name      Offset      Size (bytes)
            "playername"    :   [0x0000,    7],
            "playergender"  :   [0x0008,    1],
            "trainerid"     :   [0x000A,    4],
            "timeplayed"    :   [0x000E,    5],
            "options"       :   [0x0013,    3],
            "gamecode"      :   [0x00AC,    4],
            "securitykey"   :   [0x0AF8,    4]
        }

#TODO:  Memory map accurate for FRLG, need different mappings for RSE.
class Data_teamanditems(Datablock):
    def __init__(self):
        super().__init__()
        self.memorymap = {
        #   Attribute Name      Offset      Size (bytes)
            "teamsize"      :   [0x0034,    4   ],
            "teampokemon"   :   [0x0038,    600 ],
            "money"         :   [0x0290,    4   ],
            "coins"         :   [0x0294,    2   ],
            "pcitems"       :   [0x0298,    120 ],
            "itempocket"    :   [0x0310,    168 ],
            "keyitempocket" :   [0x03B8,    120 ],
            "ballitempocket":   [0x0430,    52  ],
            "tmcase"        :   [0x0464,    232 ],
            "berrypocket"   :   [0x054C,    172 ]
        }

class Data_rivalinfo(Datablock):
    def __init__(self):
        super().__init__()
        self.memorymap = {
        #   Attribute Name      Offset      Size (bytes)
            "rivalname"     :   [0x0BCC,    8   ],
        }

class Data_pcbuffer(Datablock):
    def __init__(self):
        super().__init__()
        self.memorymap = {
        #   Attribute Name      Offset      Size (bytes)
            "currentbox"    :   [0x0000,    4   ],
            "box_a_contents":   [0xDEAD,    3968],      #TODO
            "box_b_contents":   [0xDEAD,    3968],      #TODO
            "box_c_contents":   [0xDEAD,    3968],      #TODO
            "box_d_contents":   [0xDEAD,    3968],      #TODO
            "box_e_contents":   [0xDEAD,    3968],      #TODO
            "box_f_contents":   [0xDEAD,    3968],      #TODO
            "box_g_contents":   [0xDEAD,    3968],      #TODO
            "box_h_contents":   [0xDEAD,    3968],      #TODO
            "box_i_contents":   [0xDEAD,    2000],      #TODO
            "box_a_name"    :   [0x8344,    9   ],
            "box_b_name"    :   [0x834D,    9   ],
            "box_c_name"    :   [0x8356,    9   ],
            "box_d_name"    :   [0x835F,    9   ],
            "box_e_name"    :   [0x8368,    9   ],
            "box_f_name"    :   [0x8371,    9   ],
            "box_g_name"    :   [0x837A,    9   ],
            "box_h_name"    :   [0x8383,    9   ],
            "box_i_name"    :   [0x838C,    9   ],
            "box_a_back"    :   [0x83C2,    1   ],
            "box_b_back"    :   [0x83C3,    1   ],
            "box_c_back"    :   [0x83C4,    1   ],
            "box_d_back"    :   [0x83C5,    1   ],
            "box_e_back"    :   [0x83C6,    1   ],
            "box_f_back"    :   [0x83C7,    1   ],
            "box_g_back"    :   [0x83C8,    1   ],
            "box_h_back"    :   [0x83C9,    1   ],
            "box_i_back"    :   [0x83D0,    1   ],
        }

class Savedata:
    OFFSETS = {
    #   Name                Offset          Length (bytes)
        "save_a"        :   [0x000000,      57344],
        "save_b"        :   [0x00E000,      57344],
        "halloffame"    :   [0x01C000,      8192 ],
        "mysterygift"   :   [0x01E000,      4096 ],
        "recordedbattle":   [0x01F000,      4096 ]  	
    }

    def __init__(self, file: str):
        with open(file, "r") as f:
            self.savedata = f.read()
        
        self.data = [
            Datablock(blockid=0, blockname="trainerinfo",   offset=0x0000, length=3884),
            Datablock(blockid=1, blockname="team&items",    offset=0xDEAD, length=3968),
            Datablock(blockid=2, blockname="gamestate",     offset=0xBEEF, length=3968),
            Datablock(blockid=3, blockname="miscdata",      offset=0xDEAD, length=3968),
            Datablock(blockid=4, blockname="rivalinfo",     offset=0xD0D0, length=3848),
            Datablock(blockid=5, blockname="pcbuffer_a",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_b",    offset=0xBEEF, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_c",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_d",    offset=0xD0D0, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_e",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_f",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_g",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_h",    offset=0xDEAD, length=3968),
            Datablock(blockid=5, blockname="pcbuffer_i",    offset=0xDEAD, length=2000),
        ]
    
    def read(self, block: Datablock):
        block.data = bytearray()                    # Initialise to empty
        for byte in range(block.length):            # Copy from save file
            block.data.append(block[offset+byte])