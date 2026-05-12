from flask import Blueprint, render_template, jsonify, request
from agents.nubia_orchestrator import nubia

nubia_bp = Blueprint('nubia', __name__)

@nubia_bp.route('/')
def nubia_home():
    return render_template('nubia.html')

@nubia_bp.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    if not question:
        return jsonify(success=False, answer="No question provided."), 400
    answer = nubia.handle(question)
    return jsonify(success=True, answer=answer)
