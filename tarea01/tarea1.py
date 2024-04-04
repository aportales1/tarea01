from PIL import Image
import numpy as np

imagenes={}

class add_imagenes:
    def __init__(self, nombre, imagen_png):
        self.nombre = nombre
        self.imagen = imagen_png
        imagenes[self.nombre] = self.imagen  
    

class pixeles_de_imagen:
    def __init__(self, foto, resta, nombre):
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

        # Guardar la imagen modificada
        self.imagen_original.save('imagen_modificada.jpg')
        imagenes[self.nombre] = 'imagen_modificada.jpg'



class edicion_imagenes:
    def __init__(self, nombre, imagen_jpg):
        self.nombre = nombre
        self.imagen = imagen_jpg
    
    def filtro_negativo(self):
        # para cada pixel se resta el valor de cada componente RGB a 255. Por ejemplo, si un pixel es (200,100,50) el pixel negativo sera (55,155,205) (el alpha se mantiene igual).
        pixeles_de_imagen(self.imagen, 255, self.nombre)
    
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
        return ("fusion de dos imagenes")
    
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
          (3)  Salir 
        
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
        print("haz salido del programa")

    elif opcion_1 == "4":
        print(imagenes)
        mostrar_acciones_realizar()
    
    else:
        print("""
            Opción inválida""")
        mostrar_acciones_realizar()    

mostrar_acciones_realizar()

    
imagen = Image.open(imagenes['h'])
imagen.show()