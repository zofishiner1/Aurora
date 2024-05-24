import json
import os

def load_spec_config():
    config_path = 'data/configs/model.rec'
    with open(config_path, 'r', encoding='utf-8') as file:
        modeL = 'data/models/speech_rec/' + file.readline().strip()
    return modeL

def load_intents():
    intents_path = 'data/configs/intents.json'
    with open(intents_path, 'r', encoding='utf-8') as file:
        responses = json.load(file)
    return responses