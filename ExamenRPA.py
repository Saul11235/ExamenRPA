# -*- coding: ascii -*-

# modulo que simula un examen teorico de licencia de RPA

from platform import system as nombre_sistema
from obtener_preguntas import preguntas as get_preguntas
from os import system
from shutil import get_terminal_size
import textwrap

ancho=abs(get_terminal_size().columns-8)

def borrar_pantalla():
    if nombre_sistema()=="Windows": system("cls")
    else: system("clear")

def print_caja(texto):
    texto_ajustado=textwrap.wrap(texto,width=ancho-4)
    print("   +"+(ancho-2)*"-"+"+")
    for linea in texto_ajustado:
        nro_espacios=ancho-len(linea)-4
        print("   | "+linea+nro_espacios*" "+" |")
    print("   +"+(ancho-2)*"-"+"+")

def corrige_input(entrada):
    entrada=str(entrada)[:]
    entrada=entrada.replace(" ","")[:]
    entrada=entrada.replace("\t","")[:]
    return(entrada[:])

examenes_aprobados=0
examenes_desaprobados=0
porcentaje_aprobatorio=0.75 # porcentaje para dar un examen aprobado

preguntas=[];respuestas_usuario=[];fallos=0;aciertos=0 

def crear_nuevo_examen():
    global preguntas,respuestas_usuario, fallos, aciertos 
    preguntas=get_preguntas()
    respuestas_usuario=[]
    fallos=0 ; aciertos=0

def pantalla_pregunta(item):
    borrar_pantalla()
    pregunta=preguntas[item]
    print("\n pregunta "+str(item+1)+" de "+str(len(preguntas))+" :\n")
    print_caja(pregunta[0])
    respuesta=str(input("\n Tu respuesta: "))
    respuestas_usuario.append(respuesta[:])

def calificar_examen():
    #la calificacion es manual :(
    borrar_pantalla()
    print("\n CALIFICACION MANUAL:\n")
    print(" dejar en blanco si es correcto, con contenido si es incorrecto\n")
    input()
    for x in range(len(preguntas)): pantalla_calificacion(x) 

def pantalla_calificacion(item):
    global fallos, aciertos 
    pregunta=preguntas[item]
    borrar_pantalla()
    print("\n\nCALIFICANDO  pregunta "+str(item+1)+" de "+str(len(preguntas))+" :\n")
    print("  PREGUNTA: "+str(pregunta[0]))
    print("")
    print_caja("RESPUESTA: "+str(pregunta[1]))
    print("  TU RESPUESTA: "+str(respuestas_usuario[item]))
    print("")
    calificar=str(input(" Calificar:> "))
    if corrige_input(calificar)=="": aciertos +=1
    else: fallos +=1


def calificacion_final_examen():
    #la calificacion es manual :(
    global examenes_aprobados, examenes_desaprobados
    borrar_pantalla()
    print("\n RESULTADOS CALIFICACION \n")
    print("      aciertos: "+str(aciertos))
    print("      fallos  : "+str(fallos))
    print("")
    porcentaje_obtenido=aciertos/len(preguntas)
    print("      Tu calificacion es: "+str(round(100*porcentaje_obtenido,2))+" %")
    print("      Nota aprobatoria  : "+str(round(100*porcentaje_aprobatorio,2))+" %")
    print("")
    if porcentaje_obtenido>=porcentaje_aprobatorio:
        print_caja(" APROBADO")
        examenes_aprobados+=1
    else:
        print_caja(" DESAPROBADO")
        examenes_desaprobados+=1
    print("")
    print("      examenes aprobados   : "+str(examenes_aprobados))
    print("      examenes desaprobados: "+str(examenes_desaprobados))
    print("")
    repetir=input("_Repetir?(dejar en blanco)> ")
    if corrige_input(repetir)=="":
        comenzar_examen()
    else:
        borrar_pantalla()
        exit()

def comenzar_examen():
    crear_nuevo_examen()
    for x in range(len(preguntas)): pantalla_pregunta(x)
    calificar_examen()
    calificacion_final_examen()


if __name__=="__main__":
    try:
        comenzar_examen()
    except:
        borrar_pantalla()
        print("programa finalizado")

        
