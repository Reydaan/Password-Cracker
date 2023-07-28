letras = ["","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

combinacoes = []

primeira = 0
segunda = 0
terceira = 0
quarta = 0
quinta = 0
sexta = 0
sétima = 0
oitava = 0
nona = 0

while primeira < 26:
    primeiraletra = letras[primeira]
    while segunda  < 26:
        segundaletra = letras[segunda]
        while terceira  < 26:
            terceiraletra = letras[terceira]
            while quarta  < 26:
                quartaletra = letras[quarta]
                while quinta  < 26:
                    quintaletra = letras[quinta]
                    while sexta  < 26:
                        sextaletra = letras[sexta]
                        while sétima  < 26:  
                            sétimaletra = letras[sétima] 
                            while oitava  < 26:
                                oitavaletra = letras[oitava]
                                while nona  < 26:
                                    nonaletra = letras[nona]
                                    i = primeiraletra+segundaletra+terceiraletra+quartaletra+quintaletra+sextaletra+sétimaletra+oitavaletra+nonaletra
                                    with open('resultado.txt','a') as resultado:
                                        resultado.write(str(i) + "\n")
                                    nona = nona + 1
                                nona = 1
                                oitava = oitava + 1
                            oitava = 1
                            sétima = sétima + 1
                        sétima = 1
                        sexta = sexta + 1
                    sexta = 1
                    quinta = quinta + 1
                quinta = 1
                quarta = quarta + 1
            quarta = 1
            terceira = terceira + 1
        terceira = 1
        segunda = segunda + 1
    segunda = 1
    primeira = primeira + 1
resultado.close()

