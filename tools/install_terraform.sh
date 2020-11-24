#!/bin/sh

# Install Terraform

if [ ! -e install_terraform.sh ]; then
    echo "This script must be executed form within the tools/ folder"
    exit 1
fi

RELEASE="0.13.2"

[ -e terraform && rm -f terraform ]
wget https://releases.hashicorp.com/terraform/${RELEASE}/terraform_${RELEASE}_linux_amd64.zip
unzip terraform_${RELEASE}_linux_amd64.zip
rm -f terraform_${RELEASE}_linux_amd64.zip