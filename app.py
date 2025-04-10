from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Vineeth"  # Replace with your real full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error running top: {e}"

    return f"""
    <h3>Name: {full_name}</h3>
    <h3>User: {username}</h3>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>{top_output}</pre>
    """

# Optional: define root route if needed
@app.route("/")
def index():
    return "Go to <a href='/htop'>/htop</a> to see system info."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
