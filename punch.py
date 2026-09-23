from flask import Flask, render_template
import ssl

app = Flask(__name__)

@app.route("/")
def start():
    print("villone sta a fa brutta roba\n")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443,ssl_context=("cert.pem","key.pem"))