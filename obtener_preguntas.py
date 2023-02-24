from random import sample
import os

#----------------------------

numero_de_preguntas=3 #numero total de preguntas a tomar
Archivo_preguntas="PreguntasRpa.txt"

#----------------------------

directorio_actual = os.path.abspath(os.path.dirname(__file__))
ruta_archivo = os.path.join(directorio_actual, Archivo_preguntas)
contenido_archivo=""

def corrige_input(entrada):
    entrada=str(entrada)[:]
    entrada=entrada.replace(" ","")[:]
    entrada=entrada.replace("\t","")[:]
    entrada=entrada.replace("\n","")[:]
    return(entrada[:])

with open(ruta_archivo, mode="r",encoding="utf-8") as archivo: #abre archivo en string
    contenido_archivo = archivo.read()

lineas=contenido_archivo.split("\n")[:]

print(lineas)
input()


def Todas_las_preguntas():
   lista=[1,2,3,4,45]
   return lista

def preguntas():
    # devuelve una lista con las preguntas sacadas del temario
    # deben ser preguntas aleatorias
    todas_las_pregs=Todas_las_preguntas()
    return sample(todas_las_pregs,numero_de_preguntas)[:]


if __name__=="__main__" :
    print(contenido_archivo)
    print(preguntas())
    input()

