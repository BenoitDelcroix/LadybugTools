# Dockerfile for VS Code Dev Container
#FROM nrel/openstudio:3.10.0
#FROM nrel/energyplus:25.1.0
FROM ladybugtools/honeybee-energy:1.117.9

USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Set python3 as default python (works even if python3 is not in /usr/bin)
RUN ln -sf "$(command -v python3)" /usr/bin/python

# Install common Python tools
RUN pip3 install --upgrade pip

# Install git
RUN apt-get update && \
	apt-get install -y git && \
	rm -rf /var/lib/apt/lists/*

# Install UV package manager
# RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN pip3 install uv

#USER ladybugbot

# Set working directory
WORKDIR /workspace
