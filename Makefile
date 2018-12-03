all: docker-ami spatial-dl-ami

docker-ami: packer/docker-ami.json
	packer build packer/docker-ami.json

spatial-dl-ami:
	packer/geospatial-deep-learning-ami.json
