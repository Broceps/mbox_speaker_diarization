# load pipeline
import torch
import zmq
import base64

#ZMQ for receiving wav files to process
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://0.0.0.0:8080")

while True:
    print("waiting for incoming package from client...")
    recieved_file = socket.recv()
    print("package recieved from client")
    decode_string = base64.b64decode(recieved_file)
    wav_file = open("temp.wav", "wb")
    wav_file.write(decode_string)
    wav_file.close()

    pipeline = torch.hub.load('pyannote/pyannote-audio', 'dia')

    # apply diarization pipeline on your audio file
    diarization = pipeline(
        {'audio': 'temp.wav'})

    # dump result to disk using RTTM format
    with open('/home/mbox/speaker_diarization/test1.sad.rttm', 'w') as f:
        diarization.write_rttm(f)

        # iterate over speech turns
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(
            f'Speaker {speaker} speaks between t={turn.start:.1f}s and t={turn.end:.1f}s.')
        # Speaker "A" speaks between t=0.2s and t=1.4s.
        # Speaker "B" speaks between t=2.3s and t=4.8s.
        # Speaker "A" speaks between t=5.2s and t=8.3s.
        # Speaker "C" speaks between t=8.3s and t=9.4s.
        # ...
