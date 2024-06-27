def horario (hora):
    hora_do_dia = "{}:00 hs:______________\n".format(hora)
    return hora_do_dia


def main():
    horas= ""
    horas += horario("01")
    horas += horario("02")
    horas += horario("03")
    horas += horario("04")
    horas += horario("05")
    print(horas)

main()    
