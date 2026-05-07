from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Cloud Web App</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to My Cloud Web Application ☁️</h1>
            <h2>Successfully Deployed on Render 🚀</h2>
            <p>This application is created using Flask and deployed using PaaS.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()