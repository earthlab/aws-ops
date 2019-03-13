all: ec2-cloudformation spatial-dl-ami

ec2-cloudformation: docker-ami
	python3 python/get-latest-ami.py > latest_ami.txt
	python3 python/create-template.py
	python3 python/validate-template.py
	python3 python/push-template-to-s3.py

docker-ami: packer/docker-ami.json
	packer build packer/docker-ami.json

spatial-dl-ami:
	packer build packer/geospatial-deep-learning-ami.json
