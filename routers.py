from flask import Blueprint, request, jsonify, render_template
from app.detector.yolo_detector import detect_giraffes

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/detect', methods=['POST'])
def detect():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'Файл не загружен'}), 400

    result = detect_giraffes(file)
    return jsonify(result)