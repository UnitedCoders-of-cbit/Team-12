import string


def encrytpting(ms, fn):

    com5 = ms.replace(" ", "")
    com5 = com5.replace("’", "")
    com5 = com5.replace("\n", "")
    com5 = com5.replace("'", "")
    com5 = com5.lower()
    sonu = com5.translate(str.maketrans('', '', string.punctuation))

    rehan = open(fn, "w")
    rehan.write(sonu)
    print("Successfully Written Data")
    return sonu
