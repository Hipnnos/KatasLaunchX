def agua_restante(astronautas, agua_restante, dias_restantes):
    for argumento in [astronautas, agua_restante, dias_restantes]:
        try:
            argumento / 10
        except TypeError:
            raise TypeError(
                f"Todos los argumentos deben ser de tipo int, pero se recibio: '{argumento}'")
    uso_diario = astronautas * 11
    uso_total = uso_diario * dias_restantes
    agua_restante_total = agua_restante - uso_total
    if agua_restante_total < 0:
        raise RuntimeError(
            f"No hay suficiente agua para {astronautas} astronautas despues {dias_restantes} días!")
    return f"Agua total que queda después {dias_restantes} días es: {agua_restante_total} litros"


try:
    print(agua_restante("3", "200", None))
except RuntimeError as err:
    print(err)
