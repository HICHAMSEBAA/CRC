Message = input("Enter Your Message : ")
Crc_p = input("Enter Your CRC Polynomial : ")


def DataCrc_P(message, crc_p):
    return list(map(lambda a: eval(a), message.split())), list(map(lambda a: eval(a), Crc_p.split()))


def Append(DATA, crc_p):
    i = 0
    while i < len(CRC_P):
        DATA.append(0)
        i += 1


def CRC(DATA, crc_p):
    Append(DATA, crc_p)
    CRC_ = DATA[0:len(crc_p)]
    for i in range(len(DATA) - len(crc_p)):
        CRC__ = []
        for j in range(len(crc_p)):
            if CRC_[0] == 0:
                if CRC_[j] == 0:
                    CRC__.append(0)
                else:
                    CRC__.append(1)
            else:
                if crc_p[j] == CRC_[j]:
                    CRC__.append(0)
                else:
                    CRC__.append(1)

        CRC_ = CRC__[1:]
        CRC_.append(DATA[len(crc_p) + i])

    return CRC_[:len(CRC_) - 1]


Data, CRC_P = DataCrc_P(Message, Crc_p)
print("********************************")
print("The CRC is {}".format(CRC(Data, CRC_P)))
