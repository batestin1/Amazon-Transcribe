#!/usr/local/bin/python3
#coding: utf-8
# LAMBDA FUNCTION

##################################################################################################################################################################
# Created on 21 de Julho de 2021
#
#     Projeto base: AMAZON TRANSCRIBE
#     Repositorio: S3
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
# imports


import boto3
import uuid
import json

def lambda_handler(event, context):

    record = event['Records'][0] # arquivo enviado pelo trigger após o upload no S3
    
    s3bucket = record['s3']['bucket']['name'] # bucket de entrada que dispara o trigger
    s3object = record['s3']['object']['key'] # arquivo para ser processado
    
    s3Path = "s3://" + s3bucket + "/" + s3object # caminho para localizar o arquivo dentro do bucket de entrada
    jobName = s3object + '-' + str(uuid.uuid4()) # cria novo nome único para o job

    client = boto3.client('transcribe') # instancia um cliente python do Transcribe

    # parâmetros para iniciar um job de transcrição
    response = client.start_transcription_job(
        TranscriptionJobName=jobName,
        LanguageCode='pt-BR', # código do idioma
        MediaFormat='mp3', # formato do arquivo
        Media={
            'MediaFileUri': s3Path 
        },
        OutputBucketName = "<bucket-out>" # bucket de saída para receber o arquivo JSON com a transacrição
    )


    return {
        'TranscriptionJobName': response['TranscriptionJob']['TranscriptionJobName'] # resposta do job executado
    }
