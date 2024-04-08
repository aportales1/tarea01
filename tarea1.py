from PIL import Image
import numpy as np

imagenes={}
contador_imagenes = 0

class add_imagenes:
    def __init__(self, nombre, imagen_png):
        self.nombre = nombre
        self.imagen = imagen_png
        imagenes[self.nombre] = self.imagen  
    

class negativo:
    def __init__(self, foto, resta, nombre):
        global contador_imagenes
        self.imagen_original = Image.open(foto)
        self.resta = resta
        self.nombre = nombre

        ancho, alto = self.imagen_original.size
        datos_pixeles = self.imagen_original.load()

        for y in range(alto):
            for x in range(ancho):
                r, g, b = datos_pixeles[x, y]
                datos_pixeles[x, y] = (resta - r, resta - g, resta - b)
                #return(datos_pixeles)

        contador_imagenes += 1
        nombre_modificado = f"imagen_modificada_{contador_imagenes}.jpg"

        self.imagen_original.save(nombre_modificado)
        imagenes[self.nombre] = nombre_modificado


class fusion:
    def __init__(self, nombre1, imagen_png1, nombre2, imagen_png2):
        global contador_imagenes
        self.nombre1 = nombre1
        self.imagen1 = Image.open(imagen_png1)
        self.nombre2 = nombre2
        self.imagen2 = Image.open(imagen_png2)

        imagen1_array = np.array(self.imagen1.convert("RGBA"))
        imagen2_array = np.array(self.imagen2.convert("RGBA"))

        fusion = (imagen1_array + imagen2_array) // 2
        self.imagen_fusionada = Image.fromarray(fusion.astype('uint8'), 'RGBA')

        contador_imagenes += 1
        nombre_imagen_fusionada = f"imagen_fusionada_{contador_imagenes}.jpg"
        self.imagen_fusionada.save(nombre_imagen_fusionada)

        return self.nombre_imagen_fusionada



class edicion_imagenes:
    def __init__(self, nombre, imagen_jpg):
        self.nombre = nombre
        self.imagen = imagen_jpg
    
    def filtro_negativo(self):
        # para cada pixel se resta el valor de cada componente RGB a 255. Por ejemplo, si un pixel es (200,100,50) el pixel negativo sera (55,155,205) (el alpha se mantiene igual).
        negativo(self.imagen, 255, self.nombre)
    
    def filtro_pixeliado(self):
        tamano_pixel = input('''indique un tamano para los cuadros, debe estar entre 2 y 50 pixeles
                             >''')
        return ("imagen pixeliada")


class composicion_imagenes:
    def __init__(self, nombre1, imagen_png1, nombre2, imagen_png2):
        self.nombre1 = nombre1
        self.imagen1 = imagen_png1
        self.nombre2 = nombre2
        self.imagen2 = imagen_png2
    
    def composicion_fusionar(self):
        #fusiona dos imagenes, promediando los componentes de sus pixeles.
        foto = fusion(self.nombre1, self.imagen1, self.nombre2, self.imagen2)
        nombre_fusionado = foto
        imagenes[f"{self.nombre1}_{self.nombre2}"] = nombre_fusionado
    
    def composicion_unir(self):
        tamano_pixel = input('''indique de que manera quiere unir mas imagenes:
                             (1) right (segunda imagen se pone a la derecha de la primera)
                             (2) bottom (se unen desde la esquina inferior izquierda de la primera con la esquina superior izquierda de la segunda)
                             >''')
        return ("imagen unida")




def mostrar_acciones_realizar():
    opcion_1 = input("""
            ¿Qué deseas hacer? 
          
          (1)  Cargar Imagen 
          (2)  Editar Imagen Existente
          (3)  Fusionar imagenes
          (4)  mostrar diccionario   
          (5)  ver imagen   
          (10) Salir 
        
           > """)
    
    if opcion_1 == "1":
        nombre_imagen = input("Por favor, introduce el nombre de la imagen que deseas cargar: ")
        nueva_imagen = input('cargue la imagen aqui:  > ')
        print(f"Has seleccionado cargar la imagen por nombre: {nombre_imagen}.")
        add_imagenes(nombre_imagen, nueva_imagen)
        mostrar_acciones_realizar()
    
    elif opcion_1 == "2":
        nombre_imagen = input("¿Qué imagen deseas editar? ")
        print(f"Has seleccionado editar la imagen por nombre: {nombre_imagen}.")

        editar_imagen = edicion_imagenes(nombre_imagen,imagenes[nombre_imagen])

        accion = input(''''
                       (1) aplicar filtro negativo 
                       (2) aplicar filtro pixeliado
                       > ''')
        
        if accion == '1':
            editar_imagen.filtro_negativo()


        mostrar_acciones_realizar()

    elif opcion_1 == "3":
        print("¿Qué imagen deseas editar? ")
        imagen_1 = input('> ')
        imagen_2 = input('> ')
        composicion_imagenes(imagen_1, imagenes[imagen_1], imagen_2, imagenes[imagen_2])

        mostrar_acciones_realizar()
    
    elif opcion_1 == "4":
        print(imagenes)
        mostrar_acciones_realizar()

    elif opcion_1 == "5":
        cual = input('que imagen quieres ver: ')
        imagen = Image.open(imagenes[cual])
        imagen.show()

        mostrar_acciones_realizar()

    elif opcion_1 == "10":
        print("haz salido del programa") 
    
    else:
        print("""
            Opción inválida""")
        mostrar_acciones_realizar()    

mostrar_acciones_realizar()