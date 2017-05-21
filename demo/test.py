import random

import initialletter

colores = [
    'dc5449',
    'ee5686',
    'b15cc0',
    '8968c6',
    '6c79c3',
    '518bf5',
    '43bbf6',
    '41c9dc',
    '41aca1',
    '4bb27d',
    '90c458',
    'fdd22d',
    'f5b620',
    'ff9c20',
    'ff7d59',
    '8499a3',
    '967b72',
    'a4acdb',
    'a991d6',
    '73d9e7',
    'b39f99',
    'a3cf74',
    '8499a3',
]
abc = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]



for item in abc:
    # opciones aleatorias
    randomcolor = random.choice(colores)


    # Crea la imagen
    letter = initialletter.InitialLetter(
            text=item.upper(),
            filepath='img/',
            fontsize=65,
            fontfamilyfile='gotham/Gotham-Bold.ttf',
            background=randomcolor,
            color='ffffff',
            canvassize=(120, 120),
            quality=100
    )
    letter.create()
