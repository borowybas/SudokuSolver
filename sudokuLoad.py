
import cv2
import numpy as np
import pytesseract

def process_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    # Wczytaj obraz w skali szarości
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Zastosuj rozmycie Gaussa i progowanie adaptacyjne
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Znajdź kontury i wybierz największy (powinien to być cały kwadrat Sudoku)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Wyznacz prostokąt otaczający Sudoku
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)

    # Przekształcenie perspektywiczne, jeśli wykryto kwadrat Sudoku
    if len(approx) == 4:
        points = np.array([p[0] for p in approx], dtype="float32")
        size = 450  # Docelowy rozmiar obrazu Sudoku
        dst = np.array([[0, 0], [size - 1, 0], [size - 1, size - 1], [0, size - 1]], dtype="float32")
        matrix = cv2.getPerspectiveTransform(points, dst)
        warped = cv2.warpPerspective(image, matrix, (size, size))
    else:
        return None  # Nie wykryto Sudoku poprawnie

    # Podziel obraz na siatkę 9x9 i odczytaj liczby
    sudoku_board = [[0] * 9 for _ in range(9)]
    cell_size = size // 9

    for i in range(9):
        for j in range(9):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = (j + 1) * cell_size, (i + 1) * cell_size
            cell = warped[y1:y2, x1:x2]

            # Progowanie i usunięcie szumów
            cell = cv2.resize(cell, (28, 28))
            cell = cv2.GaussianBlur(cell, (3, 3), 0)
            _, cell = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Rozpoznawanie cyfr przy użyciu Tesseract OCR
            digit = pytesseract.image_to_string(cell, config="--psm 10 --oem 3 -c tessedit_char_whitelist=123456789")

            # Jeśli wykryto cyfrę, umieść ją w tablicy
            digit = digit.strip()
            if digit.isdigit():
                sudoku_board[i][j] = int(digit)

    return sudoku_board



















#=============================================================================================================================================================================================================
#=============================================================================================================================================================================================================
#=============================================================================================================================================================================================================

# import cv2
# import pytesseract
# import numpy as np
# from flask import Flask, render_template, request, redirect, url_for
# import os

# # app = Flask(__name__)
# # app.config['UPLOAD_FOLDER'] = 'uploads'

# # Funkcja do przetwarzania obrazu i odczytywania liczb
# def process_image(image_path):
#     pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#     # Wczytaj obraz
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     # Zastosuj binaryzację (przekształć obraz w czarno-biały)
#     _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

#     # Znajdź kontury (obramowania komórek)
#     contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Przygotuj pustą planszę sudoku
#     sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

#     # Przetwarzaj każdą komórkę
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)

#         # Sprawdź, czy kontur jest komórką sudoku
#         if w > 20 and h > 20:  # Filtruj małe kontury (szum)
#             cell = image[y:y+h, x:x+w]

#             # Użyj Tesseract do odczytania liczby
#             number = pytesseract.image_to_string(cell, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

#             # Oblicz indeksy wiersza i kolumny
#             row = y // (image.shape[0] // 9)
#             col = x // (image.shape[1] // 9)

#             # Jeśli liczba została odczytana, zapisz ją w planszy
#             if number.strip().isdigit():
#                 sudoku_board[row][col] = int(number.strip())

#     return sudoku_board