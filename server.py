from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def startCheckerBoard():
    return render_template('index.html', first_color='black', second_color='red', rows=8, columns=8)

@app.route('/<rows>')
def setCheckerRows(rows:int):
    rows = int(rows)
    return render_template('index.html', first_color='black', second_color='red', rows=rows, columns=8)

@app.route('/<rows>/<columns>')
def setWholeBoard(rows:int, columns:int):
    rows = int(rows)
    columns = int(columns)
    return render_template('index.html', first_color='black', second_color='red', rows=rows, columns=columns)

@app.route('/<rows>/<columns>/<first_color>')
def setFirstBoardColor(rows:int, columns:int, first_color:str):
    rows = int(rows)
    columns = int(columns)
    return render_template('index.html', first_color=first_color, second_color='red', rows=rows, columns=columns)

@app.route('/<rows>/<columns>/<first_color>/<second_color>')
def setBothBoardColors(rows:int, columns:int, first_color:str, second_color:str):
    rows = int(rows)
    columns = int(columns)
    return render_template('index.html', first_color=first_color, second_color=second_color, rows=rows, columns=columns)

if __name__ == '__main__':
    app.run(debug= True)