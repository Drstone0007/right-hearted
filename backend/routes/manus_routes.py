from flask import Blueprint, request, jsonify, render_template
from agents.manus import Manus

manus_bp = Blueprint('manus', __name__)
manus_instance = Manus()

@manus_bp.route('/gui')
def gui():
    return render_template('manus_gui.html')

@manus_bp.route('/api/start', methods=['POST'])
def start():
    task = request.json.get('task')
    if not task:
        return jsonify(success=False), 400
    sid = manus_instance.execute_async(task)
    return jsonify(success=True, session_id=sid)

@manus_bp.route('/api/session/<sid>')
def session_status(sid):
    session = manus_instance.get_session(sid)
    if not session:
        return jsonify(success=False), 404
    return jsonify(success=True, session=session)
