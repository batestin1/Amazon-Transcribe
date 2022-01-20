<h1 align="center">
<img src="https://img.shields.io/static/v1?label=AWS%20POR&message=MAYCON%20BATESTIN&color=7159c1&style=flat-square&logo=ghost"/>


<h3> <p align="center">AMAZON TRANSCRIBE  </p> </h3>
<h3> <p align="center"> ================= </p> </h3>

>> Arquitetura da solução:

![delta](image/img.png)


>> <h3> Description </h3>
-------------------------

<p> 
Amazon Transcribe uses a deep learning process called automatic speech recognition (ASR) to convert speech to text quickly and accurately. Amazon Transcribe can be used to transcribe customer service calls, to automate closed captioning and subtitling, and to generate metadata for media assets to create a fully searchable archive.
In this project we use a very simple architecture. We use Lambda to perform the operation, this lambda is triggered by any file to be inserted into S3. Once inserted, it will play and transcribe the audio file to another output bucket.</p>