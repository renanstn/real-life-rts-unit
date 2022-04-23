import cv2
import numpy


def stack_images(scale, img_array):
    """
    Recebe uma lista de imagens, e as posiciona lado a lado, para facilitar a
    visualização das variadas etapas de tratamento de uma imagem ou vídeo.
    """
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y], (0, 0), None, scale, scale
                    )
                else:
                    img_array[x][y] = cv2.resize(
                        img_array[x][y],
                        (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                        None,
                        scale,
                        scale,
                    )
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(
                        img_array[x][y], cv2.COLOR_GRAY2BGR
                    )
        image_blank = numpy.zeros((height, width, 3), numpy.uint8)
        hor = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = numpy.hstack(img_array[x])
        ver = numpy.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(
                    img_array[x], (0, 0), None, scale, scale
                )
            else:
                img_array[x] = cv2.resize(
                    img_array[x],
                    (img_array[0].shape[1], img_array[0].shape[0]),
                    None,
                    scale,
                    scale,
                )
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = numpy.hstack(img_array)
        ver = hor
    return ver
