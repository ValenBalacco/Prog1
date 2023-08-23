def main():
    fecha = input("Ingrese la fecha: ").strip()
    dia, mes = fecha.split(", ")[0].lower(), int(fecha.split(", ")[1].split("/")[1])
    dias_semana = {"lunes": "inicial","martes": "intermedio","miércoles": "avanzado","jueves": "práctica hablada","viernes": "inglés para viajeros" }
    if dia not in dias_semana:
        print("Error Día de la semana incorrecto.")
        return
    if (mes > 12):
        print("Error Fecha inválida.")
        return
    nivel = dias_semana[dia]
    if nivel in ["inicial", "intermedio", "avanzado"]:
        examenes = input("¿Hubo exámenes?: ").strip().lower()
        if examenes == "si":
            aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
            no_aprobados = int(input("Ingrese la cantidad de alumnos no aprobados: "))
            total_alumnos = aprobados + no_aprobados
            porcentaje_aprobados = (aprobados / total_alumnos) * 100
            print(f'Porcentaje de aprobados: '+str(porcentaje_aprobados)+'%')
    elif nivel == "práctica hablada":
        asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if asistencia > 50:
            print("Asistió la mayoría.")
        else:
            print("No asistió la mayoría.")
    elif nivel == "inglés para viajeros" and (mes == 1 or mes == 7):
        alumnos_nuevo_ciclo = int(input("Comienzo de nuevo ciclo, Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel_por_alumno = int(input("Ingrese el arancel por cada alumno: "))
        ingreso_total = alumnos_nuevo_ciclo * arancel_por_alumno
        print(f'Ingreso total: $'+str(ingreso_total))
if __name__ == "__main__":
    main()