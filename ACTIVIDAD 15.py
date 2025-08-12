estudiantes ={}
while True:
    print("1. registrar estudiantes")
    print("2. mostrar estudiantes y cursos")
    print("3. buscar estudiantes por carnet")
    print("4. salir")
    opcion=input("elija una opcion")

    if opcion =="1":
        cantidad = int (input("ingrese cantidad de estudiantes"))
        for i in range(cantidad):
            print(f"estudiante{i+1}")
            carnet=input("ingrese carnet: ")
            nombre = input("ingrese nombre: ")
            edad = input("ingrese edad: ")
            carrera = input("ingrese carrera: ")
            correo = input("ingrese correo: ")
            telefono = input("ingrese telefono: ")
            estudiantes[carnet] = {
                "nombre": nombre,
                "edad": edad,
                "carrera": carrera,
                "contacto": {
                    "correo": correo,
                    "telefono": telefono
                },
                "cursos": {}
            }

            cantidad2=int(input("ingrese numero de cursos"))
            for j in range(cantidad2):
                print(f"curso: {j+1}")
                cursoasignado=input("nombre del curso: ")
                notatarea=float(input("nota de tarea"))
                notaparcial = float(input("nota de parcial"))
                notaproyecto = float(input("nota de proyecto"))

                estudiantes[carnet]["cursos"][cursoasignado] = {
                    "tarea": notatarea,
                    "parcial": notaparcial,
                    "proyecto": notaproyecto
                }
    elif opcion == "2":
        print("lista de estudiantes")
        for carnet, datos in estudiantes.items():
            print(f"carnet: {carnet}")
            print(f"nombre: {datos["nombre"]}")
            print(f"edad: {datos["edad"]}")
            print(f"carrera: {datos["carrera"]}")
            print(f"correo: {datos["contacto"]["correo"]}")
            print(f"telefono: {datos["contacto"]["telefono"]}")

            if datos["cursos"]:
                for cursoasignado, notas in datos["cursos"].items():
                    promedio = (notas["tarea"] + notas["parcial"] + notas["proyecto"]) / 3
                    print(f"curso: {cursoasignado}")
                    print(f"tarea: {notas['tarea']}")
                    print(f"parcial: {notas['parcial']}")
                    print(f"proyecto: {notas['proyecto']}")
                    print(f"promedio: {promedio:}")
            else:
                print("ningun curso registrado")

    elif opcion =="3":
        buscar= input("ingrese el numero de carnet a buscar")
        if buscar in estudiantes:
            estudiante=estudiantes[buscar]
            print("estudiante encontrado")
            print(f"nombre: {estudiante["nombre"]}")
            print(f"edad: {estudiante["edad"]}")
            print(f"carrera: {estudiante["carrera"]}")
            print(f"correo: {estudiante["contacto"]["correo"]}")
            print(f"telefono: {estudiante["contacto"]["telefono"]}")

            if estudiante["cursos"]:
                for cursoasignado, notas in estudiante["cursos"].items():
                    promedio = (notas["tarea"] + notas["parcial"] + notas["proyecto"]) / 3
                    print(f"curso: {cursoasignado}")
                    print(f"tarea: {notas['tarea']}")
                    print(f"parcial: {notas['parcial']}")
                    print(f"proyecto: {notas['proyecto']}")
                    print(f"promedio: {promedio:}")
            else:
                print(f"ningun curso registrado ")
        else:
            print("estudiante no encontrado")

    elif opcion == "4":
        print("saliendo del programa")
        break

    else:
        print("error")






