import qrcode
import base64
from io import BytesIO
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_qr(message):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    # Convert image to base64
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_path = None
    if request.method == 'POST':
        message = request.form['message']
        qr_code_path = generate_qr(message)
    return render_template('index.html', qr_code_path=qr_code_path)

if __name__ == "__main__":
    app.run(debug=True)
