from random import sample
import os

#----------------------------

numero_de_preguntas=20 #numero total de preguntas a tomar
Archivo_preguntas="PreguntasRpa.md"

#----------------------------

directorio_actual = os.path.abspath(os.path.dirname(__file__))
ruta_archivo = os.path.join(directorio_actual, Archivo_preguntas)
contenido_archivo=""

def corrige_input(entrada):
    entrada=str(entrada)[:]
    entrada=entrada.strip()[:]
    entrada=entrada.replace("\t","")[:]
    entrada=entrada.replace("\n","")[:]
    entrada=" ".join(entrada.split())[:]
    return(entrada[:])

def valida_comentario(texto):
    if texto.startswith("#"): return True
    else: return False

def corrige_formato_pregunta(texto):
    return corrige_input(texto[1:][:]) 

with open(ruta_archivo, mode="r",encoding="utf-8") as archivo: #abre archivo en string
    contenido_archivo = archivo.read()

lineas=contenido_archivo.split("\n")[:]
lineas_sin_espacios=[]

for linea in lineas:
    espacios=" "*len(linea)
    lcorregida=corrige_input(linea)
    if espacios!=linea:
        lineas_sin_espacios.append(lcorregida)

Todas_las_preguntas=[] # corrigiendo todas las preguntas
ayuda=[] #variable que agrupa una pregunta
var_pregunta=""
var_respuesta=""
leyendo_pregunta=False

def registra_pregunta():
    global Todas_las_preguntas,var_pregunta,var_respuesta
    texto_total=var_pregunta+var_respuesta
    if texto_total!="":
        Todas_las_preguntas.append([var_pregunta,var_respuesta][:])
    var_pregunta=""
    var_respuesta=""

#----------------------------------
for x in lineas_sin_espacios:
    if valida_comentario(x):
        #--------
        if not(leyendo_pregunta):
            leyendo_pregunta=True
            registra_pregunta()
        #--------
        texto_pregunta=corrige_formato_pregunta(x)
        if var_pregunta=="": var_pregunta=texto_pregunta[:]
        else: var_pregunta=var_pregunta+"\n"+texto_pregunta
    else:
        leyendo_pregunta=False
        segundo_ciclo=True
        texto_corregido=corrige_input(x)
        if var_respuesta=="":var_respuesta=texto_corregido[:]
        else: var_respuesta=var_respuesta+"\n"+texto_corregido
registra_pregunta() 
#----------------------------------

def preguntas():
    # devuelve una lista con las preguntas sacadas del temario
    # deben ser preguntas aleatorias
    return sample(Todas_las_preguntas,numero_de_preguntas)[:]

if __name__=="__main__" :
    print(contenido_archivo)
    print(preguntas())
    input()
