import fileinput

replace_texts ={"728 ": "Z",
                "675 ": "Y",
                "624 ": "X",
                "575 ": "W",
                "528 ": "V",
                "483 ": "U",
                "440 ": "T",
                "399 ": "S",
                "360 ": "R",
                "323 ": "Q",
                "288 ": "P",
                "255 ": "O",
                "224 ": "N",
                "195 ": "M",
                "168 ": "L",
                "143 ": "K",
                "120 ": "J",
                "99 ": "I",
                "80 ": "H",
                "63 ": "G",
                "48 ": "F",
                "35 ": "E",
                "24 ": "D",
                "15 ": "C",
                "8 ": "B",
                "3 ": "A"}
for line in fileinput.input("codigo.txt", inplace=True):
    for search_text in replace_texts:
        replace_text = replace_texts [search_text]
        line = line.replace(search_text, replace_text)
    print(line, end=" ")
