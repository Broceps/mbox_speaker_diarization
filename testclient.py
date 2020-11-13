import zmq
import base64

# Opens the recorded sound, 'output.wav' and encodes it
f = open("/home/mbox/speaker_diarization/audiofiles/test1.wav", 'rb')
bytes = bytearray(f.read())
byte_wav = base64.b64encode(bytes)
f.close()

context = zmq.Context()

# Socket to talk to server
socket = context.socket(zmq.PUSH)
socket.connect("tcp://0.0.0.0:8080")

print("Sending request...")
socket.send(byte_wav)

