from flask import Blueprint, request, jsonify, render_template, send_file
from app.detector.yolo_detector import detect_giraffes
from .reporter import generate_pdf_report

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

@main_bp.route("/report")
def report():
    """Генерирует и отдаёт PDF-файл пользователю."""
    pdf_path = generate_pdf_report()
    return send_file(pdf_path, as_attachment=True)