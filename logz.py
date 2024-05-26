import datetime
import json

session_id = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

def create_session_file():
    session_data = {
        "session_id": session_id,
        "start_time": str(datetime.datetime.now()),
        "end_time": "",
        "user_utterances": [],
        "assistant_responses": [],
        "response_times": [],
        "memory_usage": []
    }
    with open(f'data/logs/session_{session_id}.json', 'w+', encoding='utf-8') as file:
        json.dump(session_data, file, indent=4, ensure_ascii=False)

def update_session_file(data, end_time=None):
    with open(f"data/logs/session_{session_id}.json", 'r', encoding='utf-8') as file:
        session_data = json.load(file)
    session_data["user_utterances"].append(data["user_utterance"])
    session_data["assistant_responses"].append(data["assistant_response"])
    session_data["response_times"].append(f"{data['response_time']} секунд")
    session_data["memory_usage"].append(f"{data['memory_usage']} МБ")
    session_data["end_time"] = end_time
    with open(f"data/logs/session_{session_id}.json", 'w', encoding='utf-8') as file:
        json.dump(session_data, file, indent=4, ensure_ascii=False)