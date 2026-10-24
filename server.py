from flask import Flask, request
import fai  # your Groq wrapper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("text", "")
        ai_response = fai.run(user_text)
    else:
        user_text = ""
        ai_response = ""

    return f"""
    <html>
    <body>
        <h2>Python + Groq Web Chat</h2>

        <form method="POST">
            <input name="text" placeholder="Type something..." style="width:300px;">
            <button type="submit">Send</button>
        </form>

        <h3>Your Input:</h3>
        <div>{user_text}</div>

        <h3>Groq Response:</h3>
        <div>{ai_response}</div>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)