all: ec2-cloudformation spatial-dl-ami

ec2-cloudformation: docker-ami
	# get the most recent AMI for the docker EC2 instance
	python3 python/get-latest-ami.py > latest_ami.txt

	# add that AMI to the template
	python3 python/create-template.py

	# validate template
	aws cloudformation validate-template --template-body file://$(date +%Y-%m-%d)-ec2-template.json

	# upload that template to S3
	aws s3 cp $(date +%Y-%m-%d)-ec2-template.json s3://earthlab-cloudformation/$(date +%Y-%m-%d)-ec2-template.json

docker-ami: packer/docker-ami.json
	packer build packer/docker-ami.json


spatial-dl-ami:
	packer build packer/geospatial-deep-learning-ami.json
