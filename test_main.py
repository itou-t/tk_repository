from flask import Flask
app = Flask(__name__)

@app.route('/test_get_follow',methods=['GET','POST'])
def get_follow():
    return render_template("/",)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)