anneau1 = [
    "0000000100", 
    "0000000001",
    "0000010010",
    "0000000101",
    "0001111111",
    "1111111111",
    "1111111111",
    "1111111111"
    ]
anneau2 = [
    "0000010100",
    "0000011001",
    "0001111111",
    "1111111111",
    "0000001101",
    "0000001001",
    "0000000111",
    "0000001000",
    ]
anneau3 = [
    "1111111111",
    "0000010100",
    "0000001000",
    "0000001001",
    "0000001110",
    "0000000111",
    "0000010011",
    "0001111111"
]
anneau4 = [
    "0000010100",
    "0000001000",
    "0000001001",
    "0000001110",
    "0000000111",
    "0000010011",
    "0001111111",
    "1111111111"
]

anneau5 = [
    "0000111010",
    "0000001110",
    "0001110110",
    "0000001010",
    "0000011110",
    "0000010111",
    "0000100010",
    "0000001011"
]

alphabet = [
    'a','b','c','d','e',
    'f','g','h','i','j',
    'k','l','m','n','o',
    'p','q','r','s','t',
    'u','v','w','x','y',
    'z'
    ]
def log(msg):
    print(f"LOG >> {msg}")


def to_decimal(t: list) -> int:
    res = []
    for i in range(len(t)):
        res.append(int(t[i], 2))
    return res

def to_lettres(t: tuple[int]) -> tuple[str|int]:
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    for i in range(len(t)):
        if t[i] >= 0 and t[i] <= 27:
            res.append(alphabet[t[i]])
        else:
            res.append(t[i])
    return res

print(f"{to_lettres(to_decimal(anneau1))}\n{to_lettres(to_decimal(anneau2))}\n{to_lettres(to_decimal(anneau3))}\n{to_lettres(to_decimal(anneau4))}\n")
