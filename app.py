from flask import Flask, render_template
app = Flask(__name__)

@app.route("/signup")
def main():
    return render_template('signUp.html')



if __name__ == "__main__":
    app.run()
