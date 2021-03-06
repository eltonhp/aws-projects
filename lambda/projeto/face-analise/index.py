import boto3;

s3 = boto3.resource('s3');
client = boto3.client('rekognition');


def create_colecao():
	response = client.create_collection(
		CollectionId='faces'
	)

def lista_imagens():

	imagens=[]
	bucket = s3.Bucket('fa-image');
	for image in bucket.objects.all():
		imagens.append(image.key);
	return imagens;

def indexa_colecao(imagens):
	for i in imagens:
		response = client.index_faces(
			CollectionId='faces',
			DetectionAttributes=[
			],
			ExternalImageId=i[:-4],
			Image={
				'S3Object': {
					'Bucket': 'fa-image',
					'Name': i,
				}
			},

		)


imagens = lista_imagens()
indexa_colecao(imagens)
#create_colecao()
