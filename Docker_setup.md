# Container setup for Deep learning masterclass

### What is Docker?

Docker is a  software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux and Windows Server apps.

Today we will use Docker container  as an environment to run our Deep learning  image classification tutorial and ‘Kaggle in class’ competition.

We have done the work of installing required tools and libraries to run the problems discussed in class. Following are the installation steps

### Docker installation 
* From the link below, install the Docker application that suits your OS
	* [Docker for Mac](https://docs.docker.com/docker-for-mac/install/#install-and-run-docker-for-mac)
	* [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
	* note** please read installation notes, since running Docker for windows requires additional steps like Hyper-V installation to run Docker containers
* Make sure that Docker has been installed and running in your system
	* (for mac) : type ‘docker --version’ in your terminal
	* (windows) : Enter 'docker --version' in cmd.exe or powershell
* Adjust computing resources allocated to Docker.
	* Since Deep learning is processor intensive task, it is advisable to utilize maximum capacity available in host machine
	* (mac) : Menu bar -> Docker -> Preferences -> advanced

Docker menubar           |  Docker preference
:-------------------------:|:-------------------------:
![Check in readme images](/readme_images/menubar-docker.png?raw=true "docker menubar") |![Check in readme images](/readme_images/docker-preference.png?raw=true "Docker preference")
* [Resource allocation for Windows](https://docs.docker.com/docker-for-windows/#shared-drives) 


### Docker keras-tf image download
* A Docker image is a file system and parameters to use at runtime, download 'Keras-tf-jupyter' Docker image from dockerhub by executing the following command.

```
docker pull zanelim/keras-tf-jupyter:0.1
```
* The image comes pre-installed with the following tools
	* Python anaconda package 
	* Keras Deep learning framework
	* Tensor Flow backend

### Instantiate container from image
* Container are efficient, lightweight, self-contained systems that guarantees software will always run the same, regardless of where it’s deployed.
* Replace "[local-directory]" with the path where you have downloaded source code and data for Cats_and_Dogs classification tutorial (the path where you have cloned this github respository locally) and run the following command

```
docker run --rm -p 8888:8888 --name keras-tf-jupyter -e PASSWORD=workshop -v /[local-directory]:/src/NUS_ISS_DeepLearningWorkshop -v zanelim/keras-tf-jupyter:0.1
```
* note if you are already using port 8888 to run a local jupyter notebook simply replace the host port to 8889 (or another port number) by running:
```
docker run --rm -p 8889:8888 --name keras-tf-jupyter -e PASSWORD=workshop -v /[local-directory]:/src/NUS_ISS_DeepLearningWorkshop -v zanelim/keras-tf-jupyter:0.1
```
* Running the instruction will 
	* Instantiate a container
	* Map the volume of local directory within the container 
	* Print a URL to iPython notebook
	* Pass the jupyter notebook password (`workshop` in this case) as an environment variable
* Go to [http://localhost:8888](http://localhost:8888) or [http://localhost:8889](http://localhost:8889) and you will see a jupyter notebook interface, enter `workshop` as the password.
* Once the local volume is mapped with the docker container, the files available in local volume will be visible within Docker container and hence the Jupyter notebook.