all: update-servicecatalog spatial-dl-ami

update-servicecatalog: ec2-cloudformation
	python3 python/place-template-in-service-catalog.py

ec2-cloudformation: docker-ami
	rm -f *-template.json
	python3 python/get-latest-ami.py > latest_ami.txt
	python3 python/create-template.py
	python3 python/validate-template.py
	python3 python/push-template-to-s3.py

docker-ami: packer/docker-ami.json
	packer build packer/docker-ami.json
