from flask import Flask, render_template, request
from openaiSudoku import loadSudokuDataFromFile
from sudoku import solveSudoku
# from sudokuLoad import process_image
# from weather import get_current_weather
from waitress import serve
# import json
import os
from werkzeug.utils import secure_filename
# from PIL import Image

# import werkzeug.serving
# import logging

# logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        if 'sudoku_image' in request.files:
            # File uploaded
            file = request.files['sudoku_image']

            if file.filename == '':
                return render_template('index.html', error='Nie wybrano pliku')
            
            filename = secure_filename(file.filename)

            
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # file_image = Image.open(file)
            # file_image.show()
            # if file.filename == '':
            #     return render_template('index.html', error='Nie wybrano pliku')
            # Save file on server
            # file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            # file.save(file_path)

            # sudoku_data=process_image(file_path)
            # print(sudoku_data)

            sudoku_data=loadSudokuDataFromFile(file)

            matrix = eval(sudoku_data)
            
            print(matrix)
            # SOlove
            if solveSudoku(matrix):
                return render_template('index.html', sudoku=matrix, solved=True, image_url=img)
            else:
                return render_template('index.html', error="This sudoku cannot be solved", sudoku=matrix, image_url=img)

        else:
            
            # Text data formular

            sudoku_data = []

            for i in range(9):
                row = []
                for j in range(9):
                    cell_value = request.form.get(f'cell-{i}-{j}') #get cell value from form data
                    row.append(int(cell_value) if cell_value else 0) #if empty - make 0
                sudoku_data.append(row)

            
            if solveSudoku(sudoku_data):
                return render_template('index.html', sudoku=sudoku_data, solved=True)
            else:
                return render_template('index.html', error="This sudoku cannot be solved", sudoku=sudoku_data)
                

    except Exception as e:
        # Zaloguj błąd (możesz użyć logging zamiast print)
        print(f"Wystąpił błąd: {e}")
        return render_template('index.html', error="Wystąpił błąd podczas rozwiązywania sudoku.")

    



if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    serve(app, host="0.0.0.0", port=8000)
    
# @app.route('/weather')
# def get_weather():
#     city = request.args.get('city')

#     if not bool(city.strip()):
#         # You could render "City Not Found" instead like we do below
#         city = "Kansas City"

#         # City is not found by API
#     # if not weather_data['cod'] == 200:
#     #     return render_template('city-not-found.html')

#     weather_data = get_current_weather(city)

#     return render_template(
#         "weather.html",
#         title=weather_data["name"],
#         status=weather_data["weather"][0]["description"].capitalize(),
#         temp=f"{weather_data['main']['temp']:.1f}",
#         feels_like=f"{weather_data['main']['feels_like']:.1f}"
#     )

