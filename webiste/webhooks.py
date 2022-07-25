from flask import request, Blueprint, jsonify

webhooks = Blueprint('webhooks', __name__)


@webhooks.route('/test_webhook', methods=['POST', 'GET'])
def test_webhook():
    return jsonify({"status": "success"}), 200