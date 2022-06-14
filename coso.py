# NOTAS: por defecto muestra 200 carácteres por linea
# debes quitarle algo de zoom al CMD (con control + scroll) y
# ajustar el tamaño de la ventana para que se vea bien uwu
# la mayoría del código es una adaptación del código de Tom-Savoie's, créditos:
# https://www.instructables.com/member/Tom-Savoie/

from PIL import Image, ImageOps
import cv2
import os
import os.path as path
import time

PAUSE = 0.009  # ajusta este para cambiar la velocidad de impresión.
FORMP4 = ".mp4"  # el tipo de video a transformar

#variables de control
finalRange = 0
ok = False


#Función para extraer fotogramas del video y guardarlos en la carpeta Images.
def video_to_images(path):
  os.mkdir('Images')
  video = cv2.VideoCapture(path)
  fps = video.get(cv2.CAP_PROP_FPS)
  success, image = video.read()
  counter = 1
  while success:
      cv2.imwrite("Images/Image{0}.jpg".format(str(counter)), image)
      success, image = video.read()
      counter += 1
  global finalRange
  finalRange = counter-1
  print(str(finalRange)+" fotogramas totales (esto puede tardar un rato)")
  return fps, (counter-1)


#Función para  trabajar la imagen con Image de PILL
def get_image(image_path):
    initial_image = Image.open(image_path)
    width, height = initial_image.size
    initial_image = initial_image.resize((round(width*1.05), height))
    return initial_image


#Pixelear imagen PILL, el final_width es la cantidad de caracteres por linea que tendrá al final.
def pixelate_image(image, final_width=200):
  width, height = image.size
  final_height = int((height*final_width)/width)
  image = image.resize((final_width, final_height))
  return image


#Recibe la imagen pixelada y la convierte a escala de grises
def grayscale_image(image):
  image_bw = ImageOps.grayscale(image)
  return image_bw


#Recibe imagen pixelada en escala de grises y replaza cada pixel con un carácter según qué tan oscuro sea.
def ascii_conversion(bw_image, ascii_string=[" ", ".", ":", "-", "=", "+", "*", "#", "%", "@", "&"]):
  pixels = bw_image.getdata()
  ascii_image_list = []
  for pixel in pixels:
     ascii_converted = int((pixel*len(ascii_string))/256)
     ascii_image_list.append(ascii_string[ascii_converted])
  return ascii_image_list


#Guadra la conversión a ascii en un archivo de texto.
def print_ascii(ascii_list, image, image_pos):
  if (image_pos % 100 == 0):  # para que se vea algo de movimiento en la consola porque este paso puede tardar
      print("..", end="")
  file = open('./fotogramAscii/shot{0}.txt'.format(str(image_pos)), "w")
  file.write("")
  width, height = image.size
  counter = 0
  for j in ascii_list:
     counter += 1
     if (counter % width) != 0:
        file.write("{0}".format(j))
     else:
        file.write("\n")
  file.write("")
  file.close()


#Ejecuta en orden las funciones anteriores usando una ruta de video.
def main(video_path):
  ascii_string = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@", "&"]
  fps, number_images = video_to_images(video_path)
  os.mkdir('fotogramAscii')

  for i in range(1, number_images+1):
      image = get_image('Images/Image{0}.jpg'.format(str(i)))
      right_size_image = pixelate_image(image)
      bw_image = grayscale_image(right_size_image)
      converted_list = ascii_conversion(bw_image, ascii_string)
      print_ascii(converted_list, right_size_image, i)


#Imprime en consola el resultado del ascii.
def printAll():
    global finalRange
    shot = []
    print("iniciando impresión:")
    for i in range(1, (finalRange+1)):
        with open("./fotogramAscii/shot{0}.txt".format(i), "r", encoding="utf8") as file:
            shot.append(file.read())
            file.close()

    for i in range(1, (finalRange+1)):
        print(shot[i])
        time.sleep(PAUSE)


#Menú improvisado para la consola.
def menu():
    os.system("cls")
    ok = path.exists("./fotogramAscii/shotl.txt")
    menu = 0
    while(menu != 3):
        if(menu == 0):
          print("Introduce un numero para elegir la opción: ")
          if(ok):
            menu = int(input("2.imprimir resultado, 3. cerrar\n"))
          else:
            menu = int(input("1. iniciar conversión, 3. cerrar\n"))

        elif(menu == 1):
          print("nota: Recuerda colocar el video en la misma carpeta que este programa.")
          nameOfFile = str(input(
              "Introduce el nombre del video, cuidando las mayusculas y minusculas. (numero 3 para cancelar)\n"))

          os.system("cls")
          if(nameOfFile == "3"):
            print("")
            menu = 0
          elif path.exists("./"+nameOfFile+FORMP4):
            if(ok):
              print("Parece que ya se intentó convertir un video antes.")
              print("intenta borrar o renombrar las carpetas Images y fotogramAscii para que no se amontonen los archivos")
            else:
              print("iniciando conversión para "+nameOfFile+FORMP4)
              main("./"+nameOfFile+FORMP4)
              ok = True
              menu = 0
              print("Conversión terminada")

          else:
            print("\nNo se pudo detectar el archivo '"+nameOfFile +
                  FORMP4+"' verifique que esté bien escrito. \n")
            menu = 1

        elif(menu == 2):
            print("Recuerda quitarle algo de zoom al CMD (con control + scroll) y ")
            print("ajustar el tamaño de la ventana para que se vea bien uwu")
            time.sleep(5)
            os.system("cls")
            printAll()
            menu = 0

        else:
            print("\n"+menu + "no es una opción válida \n")

menu()  # exito banda
