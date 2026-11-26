print("Hello")
print("ohayo")
print("konnitiha")
print("目つき悪")
print("ほえー")

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "I'm a Flask app!"

KAIKEI_DATA = [
    {"date": "2026-10-05", "kind": "収入", "item": "会費", "amount": 3000},
    {"date": "2026-10-06", "kind": "収入", "item": "会費", "amount": 3000},
    {"date": "2026-10-20", "kind": "支出", "item": "備品代", "amount": 1200},
    {"date": "2026-11-10", "kind": "支出", "item": "イベント費", "amount": 5000},
]

@app.route("/kaikei")
def kaikei():
    balance = 0
    rows = ""
    for d in KAIKEI_DATA:
        balance += d["amount"] if d["kind"] == "収入" else -d["amount"]
        rows += f"<tr><td>{d['date']}</td><td>{d['kind']}</td><td>{d['item']}</td><td>{d['amount']:,}円</td><td>{balance:,}円</td></tr>"
    return f"""
    <h1>自治会会計 入出金一覧</h1>
    <table border="1" cellpadding="6">
      <tr><th>日付</th><th>収入・支出</th><th>項目</th><th>金額</th><th>残高</th></tr>
      {rows}
    </table>
    <p>現在の残高：<b>{balance:,}円</b></p>
    """
    
