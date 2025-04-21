from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = '''
    <h2>Somma due numeri</h2>
    <form method="POST">
        Inserisci un numero: <input type="number" name="a"><br>
        Inserisci un altro numero: <input type="number" name="b"><br>
        <input type="submit" value="Calcola somma">
    </form>
    {% if risultato is not none %}
        <p>La somma di {{ a }} e {{ b }} è: {{ risultato }}</p>
    {% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def somma():
    risultato = None
    a = b = ""
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        risultato = a + b
    return render_template_string(HTML, risultato=risultato, a=a, b=b)

if __name__ == "__main__":
    app.run()