import re

meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}

def convertir_fecha(fecha):
    if re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', fecha):
        mes, dia, anio = fecha.split('/')
        mes = mes.zfill(2)
        dia = dia.zfill(2)
        return f"{anio}-{mes}-{dia}"
    
    elif re.match(r'^[a-zA-Z]+ \d{1,2}, \d{4}$', fecha):
        partes = fecha.split()
        mes_texto = partes[0]
        dia = partes[1].strip(',')
        anio = partes[2]
        mes = meses.get(mes_texto)
        if mes:
            dia = dia.zfill(2)
            return f"{anio}-{mes}-{dia}"
    
    return "Formato de fecha no reconocido."

fecha_input = input("Ingrese una fecha (MM/DD/AAAA o Mes, Día, AAAA): ")

fecha_convertida = convertir_fecha(fecha_input)

print("Fecha convertida:", fecha_convertida)