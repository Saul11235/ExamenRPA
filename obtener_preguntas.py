from random import sample

numero_de_preguntas=3 #numero total de preguntas a tomar

def Todas_las_preguntas():
    lista=[
            ["Cuando es 2 y 2?","4"],
            ["de que color es la bandera del Perú","roja y blanca"],
            ["hay una palabra clave","churichurinfunflays"],
            ["si un maya se desmaya es maya","no se"],
            ["solo se","que nada se"],

            ]
    return lista

def preguntas():
    # devuelve una lista con las preguntas sacadas del temario
    # deben ser preguntas aleatorias
    todas_las_pregs=Todas_las_preguntas()
    return sample(todas_las_pregs,numero_de_preguntas)[:]


if __name__=="__main__" :
    print(preguntas())
    input()

