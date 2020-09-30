import os
class Student():
    def __init__(self):
        self.__student = {}
        self.__period_1 = {}
        self.__period_2 = {}
        self.__period_3 = {}
        self.__period_4 = {}
        self.__list_student = []

    def addStudent(self):
        print()
        print("Hola, por favor llena todos los datos a continuación")
        print()
        print("***** Datos Basicos del Estudiante*****")
        print()
        self.__student ={
            'nombre': input("Nombre: "),
            'grado': input("Grado: "),
            'curso': input("Curso: "),
            'asignatura': input("Asignatura: "),
            'periodo': self.addnot()
        }
        self.__list_student.append(self.__student)

    def addnot(self):
        print()
        print("***ingreso de notas periodo 1")
        print()
        self.__period_1 ={
            'nota1':float(input("Ingrese la primera nota : ")),
            'nota2':float(input("Ingrese la segunda nota : ")),
            'nota3':float(input("Ingrese la tercera nota : ")),
            'definitiva':0
        }
        self.__period_1['definitiva'] = (self.__period_1['nota1']+self.__period_1['nota2']+self.__period_1['nota3'])/3,
        
        print()
        print("***ingreso de notas periodo 2")
        print()
        self.__period_2 ={
            'nota1':float(input("Ingrese la primera nota : ")),
            'nota2':float(input("Ingrese la segunda nota : ")),
            'nota3':float(input("Ingrese la tercera nota : ")),
            'definitiva':0
        }
        self.__period_2['definitiva'] = (self.__period_2['nota1']+self.__period_2['nota2']+self.__period_2['nota3'])/3,        
        
        print()
        print("***ingreso de notas periodo 3")
        print()
        self.__period_3 ={
            'nota1':float(input("Ingrese la primera nota : ")),
            'nota2':float(input("Ingrese la segunda nota : ")),
            'nota3':float(input("Ingrese la tercera nota : ")),
            'definitiva':0
        }
        self.__period_3['definitiva'] = (self.__period_3['nota1']+self.__period_3['nota2']+self.__period_3['nota3'])/3,
       
        print()
        print("***ingreso de notas periodo 4")
        print()
        self.__period_4 ={
            'nota1':float(input("Ingrese la primera nota : ")),
            'nota2':float(input("Ingrese la segunda nota : ")),
            'nota3':float(input("Ingrese la tercera nota : ")),
            'definitiva':0
        }
        self.__period_4['definitiva'] = (self.__period_4['nota1']+self.__period_4['nota2']+self.__period_4['nota3'])/3,

        return({'periodo 1':self.__period_1}, {'periodo 2':self.__period_2}, {'periodo 3':self.__period_3}, {'periodo 4':self.__period_4})


    def getStudent(self):
        os.system("cls")
        print("******Listado de Estudiantes*****")
        print()
        self.__cont =0
        for i in range(len(self.__list_student)):
            self.__cont = self.__cont + 1
            print(f"******Estudiante numero {self.__cont}*****")
            print()
            print(f"Nombre: {self.__list_student[i]['nombre']}")
            print(f"Grado: {self.__list_student[i]['grado']}")
            print(f"Curso: {self.__list_student[i]['curso']}")
            print(f"Asignatura: {self.__list_student[i]['asignatura']}")
            print()
            print("----- Notas del estudiante agrupadas mediante diccionarios -----")
            print()
            print(f"Periodos: {self.__list_student[i]['periodo']}")
            print()

                


    def menu(self, options):
        while(True):
            os.system("cls")
            for i in range(len(options)):
                print(options[i])
            print("")
            print("")
            option = input("Escoge una opcion => ")
            
            if option == "1":
                os.system("cls")
                self.addStudent()
                print("")
                print("")
                os.system("pause")
            
            elif option == "2":
                os.system("cls")
                self.getStudent()
                print()
                print()
                os.system("pause")


def main():
    options = ("    Parcial Adanud Meza","*****Menu de opciones*****"," ","1. Agregar estudiantes", "2. Mostrar estudiantes")
    stu = Student()
    stu.menu(options)

if __name__ == "__main__":
    main()