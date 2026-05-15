from flask import Flask

app = Flask(__name__)

def process_data():
    print("Processing Data Engineering Task... Success!")
    return True

@app.route('/')
def hello_world():
    # تصفح
    return '<h1>Hello CI/CD from Rahaf 🚀</h1>'

if __name__ == "__main__":

    process_data()
    

    app.run(host='0.0.0.0', port=5000)
