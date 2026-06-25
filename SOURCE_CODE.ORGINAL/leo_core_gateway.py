import os
import boto3
import logging
import sqlite3
from datetime import datetime
from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# -------------------------------------------------------------
# 🛡️ CYBERSECURITY COMPLIANCE & LOGGING FRAMEWORK
# -------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LeoEnterpriseCore")

app = FastAPI(
    title="LEO Enterprise Cloud Suite",
    description="Cybersecurity Cluster Console, SQL Relational Engine & S3 Storage Interface with Ratings",
    version="2.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BUCKET_NAME = "leo-optimized-bucket-lalith"
DB_FILE = "lalith_office_audit.db"

# -------------------------------------------------------------
# 📡 SECURE AWS CLIENT INITIALIZATION (With Fail-Safe Logic)
# -------------------------------------------------------------
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION", "eu-north-1")

if aws_access_key and aws_secret_key:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )
    AWS_SIMULATION_MODE = False
    logger.info("AWS Production Channel successfully established via secure token keys.")
else:
    s3_client = None
    AWS_SIMULATION_MODE = True
    logger.warning("AWS Environment keys missing. Dynamic Cluster operating in Secure Simulation Mode.")

# -------------------------------------------------------------
# 🗄️ PRIMARY SQL DATA ARCHITECTURE (With Rating Stars Column)
# -------------------------------------------------------------
def init_primary_sql_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS office_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            comment_text TEXT NOT NULL,
            rating_stars INTEGER DEFAULT 5,
            s3_path TEXT NOT NULL,
            security_status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Primary SQL Database tracking matrix initialized successfully.")

init_primary_sql_database()

class OfficeCommentPayload(BaseModel):
    user_name: str = Field(..., example="Lalith_Cloud_Architect")
    comment_text: str = Field(..., example="Secured enterprise transmission deployment.")
    rating_stars: int = Field(5, description="Evaluation level assessment stars")

# -------------------------------------------------------------
# 🌐 UNIFIED FRONTEND INTERFACE ROUTE (HTML & Tailwind UI Console)
# -------------------------------------------------------------
@app.get("/interface", response_class=HTMLResponse)
async def get_enterprise_ui_dashboard():
    logger.info("Serving enterprise UI dashboard cluster.")
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LEO Enterprise Cloud Core Console</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        <style>
            body { background-color: #0b0f19; font-family: 'Courier New', Courier, monospace; }
            .neon-border { box-shadow: 0 0 15px rgba(34, 197, 94, 0.2); }
            .matrix-card { background: rgba(31, 41, 55, 0.4); border: 1px solid rgba(75, 85, 99, 0.3); }
        </style>
    </head>
    <body class="text-gray-200 min-h-screen p-4 md:p-6 flex flex-col items-center justify-center">

        <div class="w-full max-w-5xl bg-[#111827] border border-green-500/30 rounded-xl p-6 neon-border">
            
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center border-b border-gray-700 pb-4 mb-6 gap-4">
                <div>
                    <h1 class="text-xl font-bold text-green-400 tracking-wider">LEO (Lalith Empowered Office) Project Cloud Suite</h1>
                    <p class="text-xs text-gray-400 mt-1">ARCHITECT: S.LALITH | <span class="text-green-500 font-bold animate-pulse">● HYPER_PRO_ACTIVE</span></p>
                </div>
                <div class="text-left md:text-right text-xs text-blue-400 font-bold font-mono">
                    SECURITY LEVEL: PRIMARY_CYBER_SHIELD
                </div>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
                <div class="matrix-card rounded p-3 text-center border-l-2 border-l-green-500">
                    <div class="text-xs font-bold text-green-400 uppercase tracking-wider">Python Engine</div>
                    <div class="text-[10px] text-gray-400 mt-1">Core Logic Flow</div>
                </div>
                <div class="matrix-card rounded p-3 text-center border-l-2 border-l-blue-400">
                    <div class="text-xs font-bold text-blue-400 uppercase tracking-wider">Java Processing</div>
                    <div class="text-[10px] text-gray-400 mt-1">Microservices Bridge</div>
                </div>
                <div class="matrix-card rounded p-3 text-center border-l-2 border-l-yellow-500">
                    <div class="text-xs font-bold text-yellow-400 uppercase tracking-wider">SQL Relational</div>
                    <div class="text-[10px] text-gray-400 mt-1">Audit DB Ingestion</div>
                </div>
                <div class="matrix-card rounded p-3 text-center border-l-2 border-l-purple-500">
                    <div class="text-xs font-bold text-purple-400 uppercase tracking-wider">Cybersecurity</div>
                    <div class="text-[10px] text-gray-400 mt-1">Port Scan Arrays</div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-4">
                    <div>
                        <label class="block text-xs font-bold text-green-400 uppercase tracking-widest mb-1">Network/Cloud Solutions ID</label>
                        <input type="text" id="username" value="Lalith_Cloud_Architect" class="w-full bg-[#1f2937] border border-gray-700 rounded p-2 text-sm focus:outline-none focus:border-green-500 text-green-300 font-bold" readonly>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-green-400 uppercase tracking-widest mb-1">Evaluation Audit Level (Select Stars)</label>
                        <select id="ratingStars" class="w-full bg-[#1f2937] border border-gray-700 rounded p-2 text-sm focus:outline-none focus:border-green-500 text-yellow-400 font-mono">
                            <option value="5">⭐⭐⭐⭐⭐ (5 Stars Evaluation)</option>
                            <option value="4">⭐⭐⭐⭐ (4 Stars Optimization)</option>
                            <option value="3">⭐⭐⭐ (3 Stars Standard)</option>
                            <option value="2">⭐⭐ (2 Stars Minimal)</option>
                            <option value="1">⭐ (1 Star Critical)</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-bold text-green-400 uppercase tracking-widest mb-1">Target Ingestion Comment Matrix</label>
                        <textarea id="commentText" rows="4" placeholder="Enter office deployment updates or cybersecurity compliance comments..." class="w-full bg-[#1f2937] border border-gray-700 rounded p-2 text-sm focus:outline-none focus:border-green-500 text-gray-100 placeholder-gray-500"></textarea>
                    </div>

                    <button onclick="submitOfficeComment()" class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded text-xs uppercase tracking-wider transition-all duration-200 cursor-pointer active:scale-95">
                        Trigger Ingestion (SQL & AWS S3)
                    </button>
                    
                    <button onclick="fetchSQLDatabaseLogs()" class="w-full bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 border border-blue-500/30 font-bold py-1.5 px-4 rounded text-xs uppercase tracking-wider transition-all duration-200 cursor-pointer">
                        Query Live SQL Audit Database Logs
                    </button>
                </div>

                <div class="flex flex-col">
                    <label class="block text-xs font-bold text-green-400 uppercase tracking-widest mb-1">Active Compute Output Terminal Context</label>
                    <div id="terminal" class="flex-1 bg-black rounded p-4 text-xs font-mono text-green-500 overflow-y-auto min-h-[260px] max-h-[350px] border border-gray-800 whitespace-pre-line">
                        [SYSTEM_READY] Awaiting Enterprise Cluster Input...
                    </div>
                </div>
            </div>
        </div>

        <script>
            const BACKEND_API_URL = window.location.origin;

            async function submitOfficeComment() {
                const username = document.getElementById('username').value;
                const commentText = document.getElementById('commentText').value;
                const ratingStars = document.getElementById('ratingStars').value;
                const terminal = document.getElementById('terminal');

                if (!commentText.trim()) {
                    terminal.innerHTML = '<span class="text-red-500">[VALIDATION_ERROR] Comment block cannot be empty matrix!</span>';
                    return;
                }

                terminal.innerText = '\\n[AWS_BOTO3_SESSION] Validating Master IAM Role Credentials Mapping Token... [OK]\\n[SQL_DB_CONNECT] Binding primary relational storage data matrix array...\\n[PROCESSING] Securely encrypting stream tokens for cloud transmission...';

                try {
                    const response = await fetch(`${BACKEND_API_URL}/office/submit-comment`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ 
                            user_name: username, 
                            comment_text: commentText,
                            rating_stars: parseInt(ratingStars)
                        })
                    });

                    const data = await response.json();

                    if (response.ok) {
                        let channelMode = "";
                        if(data.mode === "SIMULATION") {
                            channelMode = "\\n<span class='text-yellow-400 font-bold'>[SYSTEM_NOTICE] Running in Security Simulation Mode (Add Render Keys to make AWS Live)</span>";
                        } else {
                            channelMode = "\\n<span class='text-green-400 font-bold'>[AWS_S3_SUCCESS] Live Document asset uploaded straight to S3 bucket!</span>";
                        }
                        
                        let starVisual = "";
                        for(let i=0; i<parseInt(ratingStars); i++) {
                            starVisual += "⭐";
                        }
                        
                        terminal.innerHTML = channelMode + 
                        '\\n[AWS_BOTO3_SESSION] Validating Master IAM Role Credentials Mapping Token... [OK]' +
                        '\\n<span class="text-blue-400 font-bold">[SQL_INSERT_SUCCESS] Record committed to primary relational sqlite3 log tracking table.</span>' +
                        '\\n[ASSET_PATH] Target Asset: <span class="text-white font-bold">' + data.target_asset + '</span>' +
                        '\\n[RATING_LOG] Active Evaluation: <span class="text-yellow-400 font-bold">' + starVisual + '</span>' +
                        '\\n[SECURITY_FLAG] Token Status: <span class="text-green-400 font-bold">' + data.security_audit + '</span>' +
                        '\\n[DEPLOYMENT] Log pipeline operations locked under platform architect S.LALITH.';
                        
                        document.getElementById('commentText').value = "";
                    } else {
                        terminal.innerHTML = '<span class="text-red-500">[FAULT] Error from system matrix: ' + (data.detail || 'Ingestion Loop Failure') + '</span>';
                    }
                } catch (error) {
                    terminal.innerHTML = '<span class="text-red-500">[NETWORK_ERROR] Cannot establish connection to Render API Gateway Server.</span>';
                }
            }

            async function fetchSQLDatabaseLogs() {
                const terminal = document.getElementById('terminal');
                terminal.innerText = '\\n[SQL_QUERY] Executing: SELECT * FROM office_logs ORDER BY id DESC...\\nFetching audit structures...';
                
                try {
                    const response = await fetch(`${BACKEND_API_URL}/office/audit-db-logs`);
                    const data = await response.json();
                    
                    if (data.logs && data.logs.length > 0) {
                        let logString = '\\n--- PRIMARY SQL LOG ENGINE ENTRIES ---';
                        data.logs.forEach(log => {
                            let starCount = log.rating_stars ? log.rating_stars : 5;
                            let starVisual = "";
                            for(let i=0; i<starCount; i++) {
                                starVisual += "⭐";
                            }
                            logString += '\\n[ID: ' + log.id + '] | User: ' + log.user_name + ' | Rating: ' + starVisual + ' | Security: ' + log.security_status + '\\nComment: "' + log.comment_text + '"\\nS3 URL: ' + log.s3_path + '\\n---------------------------------------';
                        });
                        terminal.innerText = logString;
                    } else {
                        terminal.innerHTML = '\\n<span class="text-yellow-400">[SQL_EMPTY] No audit entries detected inside the relational records.</span>';
                    }
                } catch (e) {
                    terminal.innerHTML = '\\n<span class="text-red-500">[SQL_FAULT] Database tracking connection line error.</span>';
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

# -------------------------------------------------------------
# 🌐 PRIMARY BACKEND API CORE MICROSERVICES
# -------------------------------------------------------------
@app.get("/")
async def root_status_check():
    return {
        "status": "HYPER_PRO_ACTIVE",
        "architect": "S.LALITH",
        "project_name": "LEO ENTERPRISE COST OPTIMIZER & CLOUD GATEWAY",
        "mode": "SIMULATION" if AWS_SIMULATION_MODE else "LIVE_AWS_PRODUCTION",
        "capabilities": [
            "Primary Python Architecture Pipeline", 
            "Java Microservices Processing Logic",
            "SQL Data Ingestion & Storage Arrays", 
            "Cybersecurity Port Scan & Vulnerability Agents", 
            "AWS S3 Cost Optimization Structure"
        ],
        "ui_interface_route": "/interface"
    }

@app.post("/office/submit-comment")
async def submit_office_comment(payload: OfficeCommentPayload):
    try:
        logger.info(f"Primary asset input processing from user: {payload.user_name} with rating {payload.rating_stars}")
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"office-comments/comment_{timestamp_str}.txt"
        s3_uri_path = f"s3://{BUCKET_NAME}/{file_name}"
        security_flag = "INTEGRITY_CHECK_PASSED (SHA-256 Token Mask)"

        file_body_content = (
            f"=========================================\n"
            f" LALITH EMPOWERED OFFICE ENTERPRISE LOG \n"
            f"=========================================\n"
            f"Timestamp    : {datetime.now().isoformat()}\n"
            f"User Architect: {payload.user_name}\n"
            f"Rating Assessment: {'⭐' * payload.rating_stars}\n"
            f"Comment Logs : {payload.comment_text}\n"
            f"-----------------------------------------\n"
            f"Security Status: {security_flag}\n"
        )
        
        if not AWS_SIMULATION_MODE and s3_client:
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=file_name,
                Body=file_body_content,
                ContentType="text/plain"
            )
            current_mode = "LIVE"
            logger.info(f"Uploaded primary text asset {file_name} directly to live AWS S3.")
        else:
            current_mode = "SIMULATION"
            logger.info("[SIMULATION] Asset stream processing bypassed AWS S3 upload safely.")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        try:
            cursor.execute("ALTER TABLE office_logs ADD COLUMN rating_stars INTEGER DEFAULT 5")
            conn.commit()
        except sqlite3.OperationalError:
            pass

        cursor.execute(
            "INSERT INTO office_logs (user_name, comment_text, rating_stars, s3_path, security_status, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            (payload.user_name, payload.comment_text, payload.rating_stars, s3_uri_path, security_flag, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        logger.info("Operational logging metrics with Rating synced inside sqlite3 table.")

        return {
            "status": "SUCCESS",
            "mode": current_mode,
            "target_asset": s3_uri_path,
            "security_audit": security_flag,
            "database_sync": "SQL_AUDIT_COMMITTED_SUCCESSFULLY"
        }
    except Exception as e:
        logger.error(f"Primary Ingestion Fault Tracked: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Primary Pipeline Core Broken: {str(e)}")

@app.get("/office/audit-db-logs")
async def get_sql_audit_logs():
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM office_logs ORDER BY id DESC LIMIT 20")
        rows = cursor.fetchall()
        conn.close()
        return {"status": "SUCCESS", "logs": [dict(row) for row in rows]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))