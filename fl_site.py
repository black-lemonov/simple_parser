from flask import Flask

# __name__ = file name
app = Flask(__name__) 

if __name__ == "__main__":
    app.run(debug=True)


