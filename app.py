from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")
    params = req.get("queryResult", {}).get("parameters", {})

    if intent == "ตรวจสอบสถานะคดี":
        case_id = params.get("case_id", "ไม่ระบุ")
        reply = f"คดีหมายเลข {case_id} อยู่ระหว่างดำเนินการครับ"
    else:
        reply = "Webhook ของคุณทำงานได้ปกติแล้วครับ!"

    return jsonify({"fulfillmentText": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
