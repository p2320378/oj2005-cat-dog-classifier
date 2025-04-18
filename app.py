from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import random
import os

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': '没有文件'})
            
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'})
            
        if not allowed_file(file.filename):
            return jsonify({'error': '不支持的文件格式'})

        # 读取图像（仅作为验证）
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        
        # 演示版本：随机生成预测结果
        cat_prob = random.random()
        dog_prob = 1 - cat_prob
        
        return jsonify({
            'result': '猫' if cat_prob > dog_prob else '狗',
            'cat_probability': cat_prob,
            'dog_probability': dog_prob
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/report_error', methods=['POST'])
def report_error():
    return jsonify({'message': '感谢您的反馈！'})

if __name__ == '__main__':
    app.run(debug=True) 