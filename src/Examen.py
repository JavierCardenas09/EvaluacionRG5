import csv
from flask import Flask, jsonify

# iniciar instancia de flask
app = Flask(__name__, static_url_path="")

@app.route('/json', methods=['GET'])
def json():
    ruta_archivo = 'Data/employees.csv'
    lista = [];
    with open(ruta_archivo, 'r') as csv_archivo:
        reader1 = csv.DictReader(csv_ar)
        for linea1 in reader1:
            lista.append(linea1)
        return jsonify(lista)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")
