#funcoes
from datetime import datetime


def saudacao():
    # hora = datetime.now().hour
    hora =23
    if hora>=0 and hora<=12:
        print("Bom Dia!")
    elif hora>17:
        print("Boa Noite!")
    else:
        print("Boa Tarde!")

saudacao()