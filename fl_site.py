from flask import Flask, render_template

# __name__ = file name
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='О парсере')
    

@app.route('/about')  # обработчик для url: '/about'
def about():
    return '<h3>О нас:</h3><p>здесь будет сайт с подборками новостей</p>'


if __name__ == "__main__":
    app.run(debug=True)


