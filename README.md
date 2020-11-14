# mbox_speaker_diarization

### 1. Description
This project contains scripts for a speaker diarization server intended to run in a Linux environment. 

The server and clientcommunicate with ZMQ ([pyzmq](https://github.com/zeromq/pyzmq)) protocol. Diarization is made with the 
[pyannote](https://pyannote.github.io) framework. 

This project is one of the sub-parts to Multimodal Learning Analytics Box (MBOX) which is a research project at Malmo University.


### 2. Installation
First make sure python3 is installed. 

Then install LLVM
```
sudo apt install llvm-9

LLVM_CONFIG=llvm-config-9 pip install llvmlite
```

Install Librosa
```
pip install librosa
```

Install pytorch
```
pip install torch
```

Install pyannote by downloading github repo and using pip:
```
git clone https://github.com/pyannote/pyannote-audio.git
cd pyannote-audio
git checkout develop
pip install .
```

Finally install required sound library for linux
```
sudo apt-get install libsndfile1
```

