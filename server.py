from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
# import werkzeug.serving
# import logging

# logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    sudoku_data = []

    for i in range(9):
        row = []
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}') #get cell value from form data
            row.append(int(cell_value) if cell_value else 0) #if empty - make 0
        sudoku_data.append(row)

    # Wypisanie danych Sudoku w konsoli
    # print('fjsdjajd')
    # logging.debug("Dane Sudoku z formularza:")
    # for row in sudoku_data:
    #     logging.debug(row)  # Wypisujemy każdą linię (wiersz) Sudoku

    return render_template('index.html', sudoku=sudoku_data)


if __name__ == "__main__":
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

