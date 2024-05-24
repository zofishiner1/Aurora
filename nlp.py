from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
from system_interactions import SystemInteractions
import config_loader
si = SystemInteractions()

class NLP:
    def __init__(self, intents):
        self.responses = config_loader.load_intents()

    def get_response(self, input_text):
        max_similarity = 30
        response = "Извините, я не поняла вас."
        for key in self.responses:
            similarity = fuzz.ratio(input_text.lower(), key)
            if similarity > max_similarity:
                max_similarity = similarity
                response = random.choice(self.responses[key])
                if key == 'выключи':
                    si.shutdown_computer()
                    pass
                elif key == 'перезагрузи':
                    si.restart_computer()
                    pass
        return response