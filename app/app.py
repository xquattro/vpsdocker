from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VPS Deployment Demo</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #333; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center; max-width: 500px; }
            h1 { color: #2c3e50; margin-bottom: 10px; }
            .status { display: inline-block; padding: 6px 12px; background-color: #2ecc71; color: white; border-radius: 20px; font-size: 14px; font-weight: bold; margin-bottom: 20px; }
            p { line-height: 1.6; color: #7f8c8d; }
            .tech-stack { margin-top: 30px; display: flex; justify-content: space-around; font-weight: 600; font-size: 14px; color: #34495e; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Web Application Deployed Successfully</h1>
            <div class="status">SECURE HTTPS CONNECTION ACTIVE</div>
            <p>This application is running inside a isolated Docker container, reverse-proxied via Nginx, and secured with an automated Let's Encrypt SSL certificate.</p>
            <div class="tech-stack">
                <span>🐳 Docker</span>
                <span>⚙️ Nginx</span>
                <span>🔒 SSL (Certbot)</span>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
