# The binary to build (just the basename).
MODULE := TemplateGenerator

# Where to push the docker image.
REGISTRY ?= dmarshaltu

IMAGE := $(REGISTRY)/template-generator

VERSION := 1.0.0

# This version-strategy uses git tags to set the version string
TAG := $(shell git describe --tags --always --dirty)

BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python3 ./TemplateGenerator/app.py

build:
	@echo "\n${BLUE}Building Development image with labels:\n"
	@echo "name: $(MODULE)"
	@echo "version: $(TAG)${NC}\n"
	@sed                                 \
	    -e 's|{NAME}|$(MODULE)|g'        \
	    -e 's|{VERSION}|$(TAG)|g'        \
	    Dockerfile | docker build -t $(IMAGE):demo -f- .

shell: build
	@echo "\n${BLUE}Launching a shell in the containerized build environment...${NC}\n"
		@docker run                                                 \
			-ti                                                     \
			--rm                                                    \
			--entrypoint /bin/bash                                  \
			-u $$(id -u):$$(id -g)                                  \
			$(IMAGE):$(TAG)										    \
			$(CMD)

push: build
	@echo "\n${BLUE}Pushing image to GitHub Docker Registry...${NC}\n"
	@docker push $(IMAGE):$(VERSION)

version:
	@echo $(TAG)

.PHONY: clean image-clean build-prod push test

docker-clean:
	@docker system prune -f --filter "label=name=$(MODULE)"