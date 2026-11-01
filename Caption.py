from Config import HUGGINGFACE_API_KEY as hf_key
import requests, base64, os, re, time
from colorama import init, Fore, Style

init(autoreset=True)

ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {hf_key}", "Content-Type": "application/json"}

VISION_MODELS = [
    "moonshotai/Kimi-K2.6:novita",
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct:sombanova",
    "meta-llama/Llama-3.2-11B-Vision-Instruct:sombanova",
]

TEXT_MODELS = [
    "Qwen/Qwen2.5-7B-Instruct:together",
    "Qwen/Qwen2.5-14B-Instruct:together",
    "Qwen/Qwen2.5-32B-Instruct:together",
    "mistralai/Mistral-7B-Instruct-v0.3:together",
    "mistralai/Mistral-8x7B-Instruct-v0.1:together",
    "meta-llama/Llama-3-8B-Instruct",
    "MiniMaxAI/MiniMax-M1-80k"
]

def _data_url(path: str) -> str:
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

def query_hf_api(payload: dict) -> dict:
    try:
        r = requests.post(ROUTER_URL, headers=HEADERS, json=payload, timeout=120)
    except requests.RequestException as e:
        return None, f"Request failed: {e}"
    if r.status_code != 200:

        try:
            j = r.json()
            msg = j.get("error", {}).get("message", {}) or {}
        except Exception:
            msg = (r.text or "").strip() or r.reason or "Request failed"
        return None, f"Status {r.status_code}: {msg}"
    try:
        return r.json(), None
    except Exception:
        return None, "Non-JSON response received from Hugging Face API"

def _extract_text(data) -> str:
    msg = (data or {}).get("choices", [{}])[0].get("message", {}) or {}
    return (msg.get("content") or "").strip()
#work in proggress finish second half later.
