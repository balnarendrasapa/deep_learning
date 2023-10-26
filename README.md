# Deep Learning

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/balnarendrasapa/deep_learning)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/balnarendrasapa/deep_learning)
![GitHub](https://img.shields.io/github/license/balnarendrasapa/deep_learning)

This repository contains all the things that i learnt about deep learning. Currently there is one app available, that is object detection. Notes will be added. If you want to contribute to this repo, fork this repo, add your changes to the fork and make a pull request. Or you open this repo in codespace by clicking on above badge. this repo also contains dev-container which can be helpful to isolate dev environment.

## Development setup ⚙️

This repository contains a devcontainer.json file. You can either choose to open this in codespace or build a development environment locally. If you choose to develop locally, make sure to install the `Remote Development` extension in VSCode.

- If you want to open in codespaces, click on the above badge `Open in GitHub Codespaces` 🛠️
- If you want to open in VSCode locally, click on the above badge `Open in Dev Containers` 🛠️

## Running server 🏃‍♂️
### In Dev Environment 🛠️
- To run the server, run the command `make run`. This starts up the streamlit app. You can access the stremalit app through `localhost:8501` 🚀
- To stop the server, run `make stopserver` ⛔

### Using docker-compose in root 🐳

- To run using docker-compose, cd into the root directory and run `docker-compose up`. This may not be useful for development.
- There is an image available in this repository. If you just want to check this project out, download `other/docker-compose.yml` file and run `docker-compose up` 🐳
