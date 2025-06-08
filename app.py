from flask import Flask, render_template, request, send_file
import qrcode
import os
from datetime import datetime

app = Flask(__name__)
OUTPUT_DIR = 'static/qrcodes'
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_path = None
    if request.method == 'POST':
        data = request.form['data']
        if data:
            filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
            filepath = os.path.join(OUTPUT_DIR, filename)
            img = qrcode.make(data)
            img.save(filepath)
            qr_path = filepath
    return render_template('index.html', qr_path=qr_path)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(OUTPUT_DIR, filename), as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
