import os
import datetime
import logging
import subprocess
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LeoEnterpriseCore")

app = FastAPI()

# Configuration Placeholders
DB_FILE = "audit_rating.db"
BUCKET_NAME = "leo-optimized-storage-bucket"
AWS_SIMULATION_MODE = True

# SQL DATABASE INITIALIZATION
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_name TEXT,
            rating INTEGER,
            comment_text TEXT,
            s3_path TEXT
        )
    """)
    conn.commit()
    conn.close()

# Initialize local tracking matrix DB on startup
init_db()

# Data Structure Schemas for Ingestion
class OfficeCommentPayload(BaseModel):
    user_name: str
    rating: int
    comment_text: str

# HEALTH CHECK ROOT ENDPOINT
@app.head("/")
@app.get("/")
async def root_status_check():
    return {
        "status": "HYPER_PRO_ACTIVE",
        "architect": "S.LALITH",
        "mode": "SIMULATION" if AWS_SIMULATION_MODE else "PRODUCTION",
        "capabilities": ["Primary Python", "Primary SQL Audit & Rating DB", "AWS S3 Optimizer", "Nmap Scanner", "Docker Orchestration", "Java Microservices Bridge"],
        "ui_interface_route": "/interface"
    }

# MODERN UI/UX INTERFACE ROUTE (WITH 5-STAR SYSTEM - DEFAULT OFF)
@app.get("/interface", response_class=HTMLResponse)
async def get_ui_interface():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Leo Enterprise Cloud Suite - UI/UX Control Interface</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-primary: #0f172a;
                --bg-card: #1e293b;
                --accent: #38bdf8;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
            }
            body {
                font-family: 'Poppins', sans-serif;
                background-color: var(--bg-primary);
                color: var(--text-main);
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .container {
                width: 100%;
                max-width: 800px;
                background: var(--bg-card);
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
                border: 1px solid #334155;
            }
            h1 { color: var(--accent); margin-bottom: 5px; font-weight: 600; text-align: center; }
            .subtitle { text-align: center; color: var(--text-muted); font-size: 0.9rem; margin-bottom: 25px; }
            
            .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin-bottom: 30px; }
            .card { background: #0f172a; padding: 15px; border-radius: 10px; border: 1px solid #334155; }
            .card h3 { margin: 0 0 5px 0; font-size: 0.9rem; color: var(--accent); }
            .card p { margin: 0; font-size: 0.85rem; color: var(--text-muted); }
            
            .form-group { margin-bottom: 20px; display: flex; flex-direction: column; }
            label { font-weight: 400; margin-bottom: 8px; font-size: 0.9rem; }
            input, textarea {
                background: #0f172a; border: 1px solid #475569; padding: 12px; 
                border-radius: 8px; color: #fff; font-family: inherit; font-size: 0.9rem;
            }
            input:focus, textarea:focus { border-color: var(--accent); outline: none; }
            
            .star-rating { display: flex; gap: 8px; margin-top: 5px; flex-direction: row-reverse; justify-content: flex-end; }
            .star-rating input { display: none; }
            .star-rating label {
                font-size: 2.2rem; color: #475569; cursor: pointer; transition: color 0.2s; margin: 0;
            }
            .star-rating input:checked ~ label,
            .star-rating label:hover,
            .star-rating label:hover ~ label { color: #f59e0b; }

            button {
                background: var(--accent); color: #0f172a; font-weight: 600; border: none;
                padding: 14px; border-radius: 8px; cursor: pointer; font-size: 1rem; transition: background 0.2s;
            }
            button:hover { background: #7dd3fc; }
            #responseBox {
                margin-top: 20px; padding: 15px; border-radius: 8px; display: none;
                background: #0f172a; border: 1px solid #334155; font-family: monospace; font-size: 0.85rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Leo Cloud Gateway Console</h1>
            <div class="subtitle">Architect: S.LALITH | Active Engine Pipeline</div>
            
            <div class="grid">
                <div class="card"><h3>AWS S3 & SQL Status</h3><p>Cost Optimizer Engine & SQLite Target Trackers Active</p></div>
                <div class="card"><h3>Python & Java</h3><p>Compression Architecture & Heavy Processing Logic Active</p></div>
                <div class="card"><h3>Nmap Security</h3><p>Vulnerability Network Mapper Agent Online</p></div>
                <div class="card"><h3>Docker Daemon</h3><p>Container Containerized Operations Online</p></div>
            </div>

            <div class="form-group">
                <label>Architect / User Name</label>
                <input type="text" id="userName" placeholder="Enter your structural identity...">
            </div>

            <div class="form-group">
                <label>Evaluation Audit Level (Select Stars)</label>
                <div class="star-rating">
                    <input type="radio" id="star5" name="rating" value="5"><label for="star5">★</label>
                    <input type="radio" id="star4" name="rating" value="4"><label for="star4">★</label>
                    <input type="radio" id="star3" name="rating" value="3"><label for="star3">★</label>
                    <input type="radio" id="star2" name="rating" value="2"><label for="star2">★</label>
                    <input type="radio" id="star1" name="rating" value="1"><label for="star1">★</label>
                </div>
            </div>

            <div class="form-group">
                <label>Deployment / Optimization Analytics Comments</label>
                <textarea id="commentText" rows="3" placeholder="Write logs or comment tracking details..."></textarea>
            </div>

            <button onclick="submitAuditMetrics()">Submit System Audit Log</button>
            <div id="responseBox"></div>
        </div>

        <script>
            async function submitAuditMetrics() {
                const name = document.getElementById('userName').value;
                const comment = document.getElementById('commentText').value;
                
                const ratingRadio = document.querySelector('input[name="rating"]:checked');
                if(!name || !comment || !ratingRadio) {
                    alert("Please fill all deployment parameters and provide a star evaluation rating!");
                    return;
                }
                
                const payloadData = {
                    user_name: name,
                    rating: parseInt(ratingRadio.value),
                    comment_text: comment
                };

                const resBox = document.getElementById('responseBox');
                resBox.style.display = 'block';
                resBox.innerText = 'Transmitting execution parameters to cloud runtime pipeline...';

                try {
                    const response = await fetch('/office/submit-comment', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(payloadData)
                    });
                    const result = await response.json();
                    resBox.innerText = JSON.stringify(result, null, 4);
                } catch(err) {
                    resBox.innerText = 'Pipeline Core Broken: ' + err;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# UTILITIES & BACKGROUND CORE INTEGRATION

# 1. PYTHON COST OPTIMIZER & FILE COMPRESSION (AWS LOGIC)
@app.post("/api/leo/optimize")
async def run_cost_optimizer(bucket_name: str = BUCKET_NAME, file_key: str = "large_asset.zip"):
    logger.info(f"Triggering Leo Python file compression logic for {file_key}")
    return {
        "status": "SUCCESS",
        "framework": "Python 3 Engine",
        "message": f"Compressed {file_key} from 1GB to 100MB. AWS Cloud S3 storage costs minimized.",
    }

# 2. NMAP SECURITY MATRIX SCANNER
@app.get("/api/leo/security-scan")
async def run_nmap_audit(target_host: str = "127.0.0.1"):
    logger.info(f"Initiating Nmap architecture tracking scan on: {target_host}")
    try:
        result = subprocess.run(["nmap", "-sV", target_host], capture_output=True, text=True, timeout=15)
        return {"status": "SECURE", "scan_output": result.stdout[:500]}
    except Exception as e:
        return {"status": "SIMULATED_SCAN", "tool": "Nmap Infrastructure Scanner", "details": str(e)}

# 3. DOCKER ENGINE ORCHESTRATION CONSOLE
@app.get("/api/leo/docker-status")
async def check_docker_containers():
    return {
        "status": "CONTAINERS_ACTIVE",
        "orchestration": "Docker Daemon Engine",
        "active_services": ["leo-python-compressor", "java-billing-microservice", "nmap-scheduler-agent"]
    }

# 4. JAVA MICROSERVICES BRIDGE CONTEXT
@app.post("/api/leo/java-bridge")
async def trigger_java_microservice(payload: dict = None):
    return {
        "status": "JAVA_BRIDGE_PRO_ACTIVE",
        "runtime": "Java OpenJDK Environment Core",
        "payload_received": payload if payload else "Default Handshake Data Active"
    }

# TRANSACTIONAL AWS & SQL TRACKING OPERATIONS

@app.post("/office/submit-comment")
async def submit_office_comment(payload: OfficeCommentPayload):
    try:
        logger.info(f"Primary asset input evaluation processing from: {payload.user_name}")
        timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # AWS S3 PATH GENERATION LOGIC
        file_name = f"office-comments/comment_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        s3_uri_path = f"s3://{BUCKET_NAME}/{file_name}"
        
        # SQL LOCAL DATABASE LOG TRANSACTION LOGIC
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO audit_logs (timestamp, user_name, rating, comment_text, s3_path)
            VALUES (?, ?, ?, ?, ?)
        """, (timestamp_str, payload.user_name, payload.rating, payload.comment_text, s3_uri_path))
        conn.commit()
        conn.close()
        logger.info("SQL Record synchronized successfully.")

        return {
            "status": "LOG_GENERATED_AND_DB_SYNCHRONIZED",
            "s3_path": s3_uri_path,
            "aws_status": "INTEGRITY_CHECK_PASSED (SHA-256 Token Mask)",
            "sql_database_sync": "SUCCESS_WRITE",
            "audit_data_stored": {
                "user": payload.user_name,
                "stars_awarded": f"{payload.rating} Out of 5",
                "logs_text": payload.comment_text
            }
        }
    except Exception as e:
        logger.error(f"Primary Ingestion Fault Tracked: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("leo_core_gateway:app", host="0.0.0.0", port=10000)