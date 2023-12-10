import threading
import time
from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])
class TranslateThread(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text
    
    def run(self):
        translation = translator.translate(self.text, dest='en')
        result = translation.text
        time.sleep(1)
        print(f"原始文本: {self.text}")
        print(f"翻译结果: {result}")
        print()

texts = ["你好", "谢谢", "再见"]
threads = []
for text in texts:
    thread = TranslateThread(text)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
