all: packer/docker-ami.json
	packer build packer/docker-ami.json

