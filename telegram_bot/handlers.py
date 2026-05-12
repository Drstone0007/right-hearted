from telegram import Update
from telegram.ext import ContextTypes
import requests

API = "http://localhost:5000"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐐 Right-Hearted bot.\n/manus <task>\n/tars <code>\n/nubia <query>")

async def manus_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = ' '.join(context.args)
    if not task: await update.message.reply_text("Usage: /manus <task>"); return
    resp = requests.post(f"{API}/manus/api/start", json={"task": task}).json()
    if resp.get('success'):
        await update.message.reply_text(f"Session started: {resp['session_id']}")
    else:
        await update.message.reply_text("Failed.")

async def tars_cmd(update, context):
    problem = ' '.join(context.args)
    if not problem: await update.message.reply_text("Usage: /tars <code problem>"); return
    # TARS has no async endpoint yet; we'll create a simple sync call
    resp = requests.post(f"{API}/nubia/ask", json={"question": problem}).json()
    await update.message.reply_text(resp.get('answer',''))

async def nubia_cmd(update, context):
    query = ' '.join(context.args)
    if not query: await update.message.reply_text("Usage: /nubia <query>"); return
    resp = requests.post(f"{API}/nubia/ask", json={"question": query}).json()
    await update.message.reply_text(resp.get('answer',''))
