# Use the base image from Microsoft
FROM mcr.microsoft.com/devcontainers/universal:2-linux

# Install Python 3 and pip (already included in the base image, but let's make sure)
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install the Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Set the working directory in the container
WORKDIR /learning

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container
COPY . /learning

# Expose port 8501 for Streamlit
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "curconvert.py"]

#Should run on port 8501
