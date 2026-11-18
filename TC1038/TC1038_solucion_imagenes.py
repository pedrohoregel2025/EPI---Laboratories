from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def cargar_imagen(ruta):
    """Carga una imagen RGB y devuelve su matriz de píxeles."""
    imagen = Image.open(ruta).convert("RGB")
    matriz = np.array(imagen)
    return matriz


def mostrar_informacion(matriz):
    """Imprime dimensiones, tipo de datos y ejemplos de píxeles."""
    alto, ancho, canales = matriz.shape
    print("Dimensiones (alto, ancho, canales):", matriz.shape)
    print("Tipo de dato:", matriz.dtype)
    print("Total de valores:", matriz.size)
    print("Alto:", alto, "Ancho:", ancho, "Canales:", canales)
    print("Píxel [0, 0]:", matriz[0, 0])
    print("Píxel central:", matriz[alto // 2, ancho // 2])
    print("Fragmento 3 x 3 de la matriz RGB:")
    print(matriz[:3, :3, :])


def mostrar_imagen(matriz, titulo="Imagen"):
    """Muestra una matriz como imagen RGB o de un canal."""
    plt.figure(figsize=(10, 6))
    if matriz.ndim == 2:
        plt.imshow(matriz, cmap="gray", vmin=0, vmax=255)
    else:
        plt.imshow(matriz)
    plt.title(titulo)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def convertir_grises(matriz):
    """Calcula la intensidad de gris para cada píxel RGB."""
    rojo = matriz[:, :, 0].astype(float)
    verde = matriz[:, :, 1].astype(float)
    azul = matriz[:, :, 2].astype(float)
    grises = 0.299 * rojo + 0.587 * verde + 0.114 * azul
    return np.rint(grises).astype(np.uint8)


def convertir_blanco_negro(grises, umbral=128):
    """Convierte cada gris en 0 (negro) o 255 (blanco)."""
    if umbral < 0 or umbral > 255:
        raise ValueError("El umbral debe estar entre 0 y 255")
    return np.where(grises >= umbral, 255, 0).astype(np.uint8)


def separar_rgb(matriz):
    """Devuelve las tres matrices bidimensionales de color."""
    rojo = matriz[:, :, 0]
    verde = matriz[:, :, 1]
    azul = matriz[:, :, 2]
    return rojo, verde, azul


def crear_imagen_canal(canal, posicion):
    """Coloca un canal en una imagen RGB y los otros dos en cero."""
    alto, ancho = canal.shape
    resultado = np.zeros((alto, ancho, 3), dtype=np.uint8)
    resultado[:, :, posicion] = canal
    return resultado


def main():
    ruta = "big-data.jpg"
    matriz = cargar_imagen(ruta)
    mostrar_informacion(matriz)
    mostrar_imagen(matriz, "Imagen original")

    grises = convertir_grises(matriz)
    print("Matriz gris, primeras 3 filas y columnas:")
    print(grises[:3, :3])
    mostrar_imagen(grises, "Escala de grises")

    binaria = convertir_blanco_negro(grises, 128)
    print("Matriz binaria, primeras 3 filas y columnas:")
    print(binaria[:3, :3])
    mostrar_imagen(binaria, "Blanco y negro, umbral 128")

    rojo, verde, azul = separar_rgb(matriz)
    print("Canal rojo, muestra 3 x 3:\n", rojo[:3, :3])
    print("Canal verde, muestra 3 x 3:\n", verde[:3, :3])
    print("Canal azul, muestra 3 x 3:\n", azul[:3, :3])

    mostrar_imagen(crear_imagen_canal(rojo, 0), "Canal rojo")
    mostrar_imagen(crear_imagen_canal(verde, 1), "Canal verde")
    mostrar_imagen(crear_imagen_canal(azul, 2), "Canal azul")

    Image.fromarray(grises).save("escala_grises.png")
    Image.fromarray(binaria).save("blanco_negro.png")
    Image.fromarray(crear_imagen_canal(rojo, 0)).save("canal_rojo.png")
    Image.fromarray(crear_imagen_canal(verde, 1)).save("canal_verde.png")
    Image.fromarray(crear_imagen_canal(azul, 2)).save("canal_azul.png")
    print("Imágenes procesadas guardadas correctamente.")


if __name__ == "__main__":
    main()
