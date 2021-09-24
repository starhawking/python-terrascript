FROM gitpod/workspace-full:latest

USER root

# Fetch Terraform binary
RUN cd /tmp && \
    curl https://releases.hashicorp.com/terraform/1.0.7/terraform_1.0.7_linux_amd64.zip > terraform.zip && \
    unzip terraform.zip && \
    install -m 0755 terraform /usr/local/bin/terraform && \
    rm -f terraform
    
RUN python3 -m ensurepip --upgrade && \
    pip3 install --upgrade 'coverage==4.4.1' \
                           'nose==1.3.7' \
                           'setuptools>=18.5,<22' \
                           'deepdiff==4.0.7' \
                           'flake8==3.7.9' \
                           'black==20.8b1' \
                           'sphinx'

USER gitpod
