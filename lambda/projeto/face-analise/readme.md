# Comando AWS CLI

 Fazer upload para serviço s3 de armazenamento
`aws s3 sync . s3://fa-image`


Subir uma imagem especifica para o serviço s3 de armazenamento
`aws s3 cp _analise.jpg s3://fa-image`

busca a lista de coleções pela api de reconhecimento facial da aws - rekognition

`aws rekognition list-collections`


ver o  conteúdo de uma collection ID na aws rekognition

`aws rekognition list-faces --collection-id <nome da collection>`
exemplo: aws rekognition list-faces --collection-id faces | findstr ExternalImageId


Inserido um arquivo como função lambda aws

`aws lambda update-function-code --function-name faceAnalise --zip-file fileb://faceanalise.zip`


Criar versionamento no aws lambda
`aws lambda publish-version --function-name <nome da funçao lambda>`  Exemplo: aws lambda publish-version --function-name faceAnalise

Criar um alias no aws lambda
`aws lambda create-alias --function-name faceAnalise  --function-version 1 --name PROD`
