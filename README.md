# MP4_to_AsciiCode

Convierte cada fotograma de video en arte ascii. 
Y permite impriir en consola de windows (con maña)

### Notas sobre esta versión:

  + Sólo funciona con videos en formato mp4.
  + El video a convertir y el archivo 'coso.py' deben estar en la misma carpeta.
  + Por defecto muestra 200 carácteres por linea, así que para ver bien el resultado en la consola de windows debes quitarle algo de zoom (control + scroll) y ajustar el tamaño de la ventana para que se vea bien uwu
  + Convierte un solo video por vez en la misma carpeta (habrá que borrar, mover o renombrar las dos carpetas que se crean al convertir un video a ascii)


### Necesita las siguientes cosillas:

  + Tener python instalado - https://www.python.org/downloads/
  + PIL (Image e ImageOps) - lo puedes instalar con "pip install Pillow" o "pip3 install Pillow"
  + cv2 (el poderosísimo OpenCV) - lo puedes instalar con "pip install opencv-python".


### Como usar:
- Convertir archivo:
  + Abra el CMD (win+r y escribe cmd)
  + Ejecuta "python coso.py"
  + Se abrirá un menú, elige la opción para convertir introduciendo el numero 1.
  + Te pedirá el nombre del video, escribelo sin el .mp4 y comenzará a generar los archivos.
  + Esto genera dos carpetas, una llamada 'Image' que tiene los fotogramas del video. y otra llamada 'fotogramAscii' que contiene el equivalente en arte ascii de cada fotograma (guardados como shot.txt).
- Verlo en la consola:
  + Antes de imprimir ajusta la ventana y quitale zoom (control + scroll), lo suficiente como para que puedas ver los 200 caracteres en una linea.
  + Quizá las letras sean demasiado pequeñas para ver pero si la conversión salió bien entonces basta con que pongas el numero 2 y des enter. 
  + Procederá a imprimirse en bruto en la consola y dará la ilusión de movimiento. (si esto no se ve tan fluido puedes ajustar la velocidad de impresión en la liena 13 del coso.py)
 

---
### Estado del proyecto

Yo creo que así se va a quedar un buen rato xd

### aasdfasdf

La mayoría del código es una adaptación del código de Tom-Savoie's, créditos:
https://www.instructables.com/member/Tom-Savoie/

Un saludo al grupo de FB Waifus Informáticas. 
