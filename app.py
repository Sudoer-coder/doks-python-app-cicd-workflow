from flask import Flask, jsonify, Response
import os
import json

app = Flask(__name__)

# Environment variables (injected by CI/CD)
APP_NAME = "Python Microservice CICD Demo"
DESCRIPTION = "A simple demo microservice to showcase CI/CD with GitHub Actions and DigitalOcean Kubernetes."
AUTHOR = "Zaw Ye"
VERSION = os.getenv("APP_VERSION", "v0.0.0")
COMMIT = os.getenv("GIT_COMMIT", "unknown")
ENV = os.getenv("APP_ENV", "local")

@app.route("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                font-family: Arial, Helvetica, sans-serif;
                color: #ffffff;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 700px;
                margin: 80px auto;
                background: rgba(0, 0, 0, 0.45);
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            }}
            h1 {{
                color: #00e5ff;
            }}
            .badge {{
                display: inline-block;
                padding: 6px 12px;
                background: #00e5ff;
                color: #00323a;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
            }}
            .info {{
                margin-top: 20px;
                line-height: 1.8;
            }}
            .label {{
                color: #9be7ff;
                font-weight: bold;
            }}
            footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #b0bec5;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">{ENV.upper()} ENVIRONMENT</span>
            <h1>{APP_NAME}</h1>
            <p>{DESCRIPTION}</p>

            <div class="info">
                <p><span class="label">Author:</span> {AUTHOR}</p>
                <p><span class="label">Version:</span> {VERSION}</p>
                <p><span class="label">Git Commit:</span> {COMMIT}</p>
                <p><span class="label">Runtime:</span> Python Flask</p>
                <p><span class="label">Platform:</span> DigitalOcean Kubernetes (DOKS)</p>
            </div>

            <footer>
                🚀 CI/CD powered by GitHub Actions | Kubernetes Native
            </footer>
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


@app.route("/api")
def api():
    """API-friendly JSON response for curl / automation"""
    return jsonify(
        app=APP_NAME,
        description=DESCRIPTION,
        author=AUTHOR,
        version=VERSION,
        commit=COMMIT,
        environment=ENV
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
