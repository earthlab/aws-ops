all: packer/docker-ami.json
	packer build packer/docker-ami.json
	packer build packer/geospatial-deep-learning-ami.json
