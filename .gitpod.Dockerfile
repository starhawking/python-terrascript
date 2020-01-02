FROM gitpod/workspace-full:latest

USER root

# Fetch Terraform binary
RUN cd /tmp && \
    curl https://releases.hashicorp.com/terraform/0.12.18/terraform_0.12.18_linux_amd64.zip > terraform.zip && \
    unzip terraform.zip && \
    install -m 0755 terraform /usr/local/bin/terraform && \
    rm -f terraform

USER gitpod
