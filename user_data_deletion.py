
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user-data-deletion', methods=['POST'])
def delete_user_data():
    signed_request = request.form.get('signed_request')

    # TODO: Bạn có thể giải mã signed_request nếu cần xác minh user
    # Trong bản đơn giản này, ta trả về URL xác nhận xóa

    return jsonify({
        "url": "https://yourdomain.com/deletion-status?id=example_user_123"
    })

@app.route('/deletion-status')
def deletion_status():
    return "🗑️ Yêu cầu xóa dữ liệu người dùng của bạn đã được ghi nhận và đang được xử lý."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
