from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="hi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>YouTube Automation Agent</title>
        <style>
            body { font-family: system-ui, -apple-system, sans-serif; background: #0f172a; color: #fff; margin: 0; padding: 20px; display: flex; justify-content: center; }
            .card { background: #1e293b; padding: 24px; border-radius: 14px; max-width: 480px; width: 100%; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
            h2 { color: #38bdf8; margin: 10px 0; font-size: 22px; }
            p { color: #94a3b8; font-size: 14px; }
            input { width: 100%; padding: 12px; margin: 15px 0; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: #fff; font-size: 15px; box-sizing: border-box; }
            button { width: 100%; padding: 12px; background: #2563eb; color: #fff; border: none; border-radius: 8px; font-weight: bold; font-size: 16px; cursor: pointer; }
            .badge { background: #10b981; color: #fff; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">● Online & Ready</span>
            <h2>YouTube Automation Agent</h2>
            <p>यहाँ अपना वीडियो टॉपिक दर्ज करें:</p>
            <input type="text" placeholder="उदाहरण: 1971 युद्ध की अनकही कहानी..." />
            <button onclick="alert('एजेंट सक्रिय है! अगला फीचर जल्द ही कनेक्ट होगा।')">जेनरेट करें (Title, Script & SEO)</button>
        </div>
    </body>
    </html>
    """
    
