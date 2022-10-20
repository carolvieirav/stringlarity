from flask import (
    Flask,
    render_template,
    request
)
import spacy

nlp = spacy.load('pt_core_news_sm')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle a POST request and the data sent here.
        x_nlp = nlp(request.form.get('x', ''))
        y_nlp = nlp(request.form.get('y', ''))
        
        resultado = x_nlp.similarity(y_nlp)
        
    # Return a rendered template and pass defined variables to the template.
    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)