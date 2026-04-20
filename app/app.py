import os
import sqlite3
from datetime import datetime
from flask import Flask, jsonify, request, render_template_string

DB_PATH = os.getenv("DB_PATH", "/data/app.db")

app = Flask(__name__)

# ---------- CSS & HTML Template ----------
COMMON_STYLE = """
<style>
    body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .container { background: #1e293b; padding: 2rem; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); width: 90%; max-width: 600px; text-align: center; border: 1px solid #334155; }
    h1 { color: #38bdf8; margin-bottom: 0.5rem; }
    .status-ok { background: #10b981; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: bold; }
    .btn { display: inline-block; background: #38bdf8; color: #0f172a; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; margin-top: 20px; transition: 0.3s; }
    .btn:hover { background: #0ea5e9; transform: scale(1.05); }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 0.9rem; }
    th { border-bottom: 2px solid #334155; padding: 10px; color: #94a3b8; }
    td { padding: 10px; border-bottom: 1px solid #334155; }
    .ts { color: #64748b; font-size: 0.8rem; }
    .msg-badge { background: #334155; padding: 3px 8px; border-radius: 4px; }
</style>
"""

BASE_LAYOUT = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dashboard PRA - EPSI</title>
    {COMMON_STYLE}
</head>
<body>
    <div class="container">
        {{{{ content | safe }}}}
        <br>
        <div style="margin-top:30px; font-size:0.7rem; color:#475569;">
            Jean-Gérard HOUNKANRIN - Atelier PRA/PCA - EPSI 2026
        </div>
    </div>
</body>
</html>
"""

# ---------- DB helpers ----------
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ---------- Routes ----------

@app.get("/")
def hello():
    init_db()
    content = """
        <span class="status-ok">ONLINE</span>
        <h1>Atelier PRA/PCA</h1>
        <p>Bonjour tout le monde ! L'application est prête pour les tests.</p>
        <a href="/consultation" class="btn">Voir les messages</a>
    """
    return render_template_string(BASE_LAYOUT, content=content)

@app.get("/health")
def health():
    init_db()
    content = """
        <h1 style="color:#10b981;">Health Check</h1>
        <p>Le système est parfaitement opérationnel.</p>
        <span class="status-ok">Status: OK</span>
        <br><a href="/" class="btn">Retour</a>
    """
    return render_template_string(BASE_LAYOUT, content=content)

@app.get("/add")
def add():
    init_db()
    msg = request.args.get("message", "hello")
    ts = datetime.utcnow().isoformat() + "Z"
    conn = get_conn()
    conn.execute("INSERT INTO events (ts, message) VALUES (?, ?)", (ts, msg))
    conn.commit()
    conn.close()
    
    content = f"""
        <h1 style="color:#10b981;">Message Ajouté</h1>
        <p class="msg-badge">"{msg}"</p>
        <p class="ts">Enregistré à : {ts}</p>
        <a href="/consultation" class="btn">Consulter la base</a>
    """
    return render_template_string(BASE_LAYOUT, content=content)

@app.get("/consultation")
def consultation():
    init_db()
    conn = get_conn()
    cur = conn.execute("SELECT id, ts, message FROM events ORDER BY id DESC LIMIT 50")
    rows = cur.fetchall()
    conn.close()

    table_rows = ""
    for r in rows:
        table_rows += f"<tr><td>{r[0]}</td><td class='ts'>{r[1]}</td><td><span class='msg-badge'>{r[2]}</span></td></tr>"

    content = f"""
        <h1>Base de Données</h1>
        <p>Historique des messages restaurés (PRA)</p>
        <table>
            <thead><tr><th>ID</th><th>Timestamp</th><th>Message</th></tr></thead>
            <tbody>{table_rows}</tbody>
        </table>
        <a href="/" class="btn">Accueil</a>
    """
    return render_template_string(BASE_LAYOUT, content=content)

@app.get("/count")
def count():
    init_db()
    conn = get_conn()
    cur = conn.execute("SELECT COUNT(*) FROM events")
    n = cur.fetchone()[0]
    conn.close()

    content = f"""
        <h1>Statistiques</h1>
        <div style="font-size: 3rem; font-weight: bold; color: #38bdf8; margin: 20px 0;">{n}</div>
        <p>Messages actuellement en base.</p>
        <a href="/consultation" class="btn">Vérifier les données</a>
    """
    return render_template_string(BASE_LAYOUT, content=content)

# ---------- Main ----------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)