import threading, queue
import speech_recognition as sr

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()
r = sr.Recognizer()
mic = sr.Microphone()
filename = "sample_audio.wav"

# Send thirty task requests to the worker.
for item in range(2):
    # open the file
    print("Reading audio file...")
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
        q.put(item)

for item in range(2):
    # open the file
    print("Start speaking.")
    with mic as source:
        audio = r.listen(source)
    print('End.')
    print('Text is ...')
    print(r.recognize_google(audio))
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')





