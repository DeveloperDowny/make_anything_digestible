# About this Project
- Make any given concept digestible by breaking it down into smaller parts and picking 5 random part daily and explaining each part in detail, giving advance knowledge along with exmaples using ChatGPT API and mailing the output to the user.
- Use brevo for sending emails.


# The prompt for code generation

- Make any given concept digestible by breaking it down into smaller parts and picking 5 random part daily and explaining each part in detail, giving advance knowledge along with exmaples using ChatGPT API and mailing the output to the user.
- Use brevo for sending emails.

Use OpenAPI for backend

Use best practices for writing the code.
Use latest version of python and libraries.
Use OOP concepts.
Use logging for debugging.
Use comments for explaining the code.
Use docstrings for documenting the functions.
Use type hints for the function arguments and return values.
Use a virtual environment for the project.
Use a requirements.txt file to list the dependencies.
Use a README.md file to explain how to run the code.
Use a .gitignore file to exclude the virtual environment and the dependencies. 
Use software engineering best practices like DRY, KISS, etc.
Use coupling and cohesion principles.


# The Data

Data source: https://www.knowledgehut.com/blog/devops/basic-docker-commands

Scraped it using Firecrawl: https://www.firecrawl.dev/playground?url=https%3A%2F%2Fwww.knowledgehut.com%2Fblog%2Fdevops%2Fbasic-docker-commands&mode=scrape&limit=5&excludes=&includes=&returnOnlyUrls=&ignoreSitemap=&maxDepth=&onlyMainContent=false&includeHtml=false&removeTags=&onlyIncludeTags=&waitFor=

## Result of scraping

[All Courses](/courses)

Bootcamps

Enterprise

Resources

![Knowledgehut Logo](https://www.knowledgehut.com/_next/image?url=%2Fkh-desktop-new-logo.svg&w=3840&q=75)

[All Blogs](/blog)

[Agile](/blog/category/agile)
[Project Management](/blog/category/project-management)
[Data Science](/blog/category/data-science)

More

Subscribe

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iODYiIGhlaWdodD0iMzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Knowledgehut Logo](https://www.knowledgehut.com/_next/image?url=%2Fkh-desktop-new-logo.svg&w=256&q=75)

Courses

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![banner-in1](https://www.knowledgehut.com/_next/image?url=https%3A%2F%2Fd2o2utebsixu4k.cloudfront.net%2Fassets%2Fimages%2Fbanner-in1.png&w=384&q=75)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTcxIiBoZWlnaHQ9IjE1NCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![Blog_Banner_Asset](https://www.knowledgehut.com/_next/image?url=https%3A%2F%2Fd2o2utebsixu4k.cloudfront.net%2Fassets%2Fimages%2FBlog_Banner_Asset.svg&w=384&q=75)

1.  [Home](https://www.knowledgehut.com/)
    
2.  [Blog](https://www.knowledgehut.com/blog)
    
3.  [DevOps](https://www.knowledgehut.com/blog/category/devops)
    
4.  Top 55+ Basic Docker Commands You Must Learn in 2024

[Home](https://www.knowledgehut.com/)
[Blog](https://www.knowledgehut.com/blog)
[DevOps](https://www.knowledgehut.com/blog/category/devops)
Top 55+ Basic Docker Commands You Must Learn in 2024

Share

[](http://www.facebook.com/sharer/sharer.php?u=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](http://twitter.com/share?via=Knowledgehut&url=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](https://www.linkedin.com/cws/share?url=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](https://web.whatsapp.com/send?text=https://www.knowledgehut.com/blog/devops/basic-docker-commands)

Top 55+ Basic Docker Commands You Must Learn in 2024
====================================================

Blog Author

[Lakshmi Sushmitha V](/blog/author/lakshmi-sushmitha-v)

Published

24th Jul, 2024

Views

40,375

Read TimeRead it in

7 Mins

In this article

1.  What is Docker?
2.  Top 15 Basic Docker Commands
3.  57 Essential Docker Commands List
4.  Docker Use Cases
5.  Docker Architecture
6.  Conclusion
7.  Frequently Asked Questions (FAQs)

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTEiIGhlaWdodD0iMTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Play icon](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![Video Thumbnail Image](https://www.knowledgehut.com/_next/image?url=%2Fvideo-thumbnail-image.svg&w=3840&q=75)

In this article

1.  What is Docker?
2.  Top 15 Basic Docker Commands
3.  57 Essential Docker Commands List
4.  Docker Use Cases
5.  Docker Architecture
6.  Conclusion
7.  Frequently Asked Questions (FAQs)

View All

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjU2IiBoZWlnaHQ9IjI0NyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![Top 55+ Basic Docker Commands You Must Learn in 2024](https://www.knowledgehut.com/_next/image?url=https%3A%2F%2Fd2o2utebsixu4k.cloudfront.net%2Fmedia%2Fimages%2Fd522248b-0283-4c92-8a57-1a301cc6c0d4.png&w=1920&q=75)

DevOps is a natural evolution of software development. DevOps is not just a tool, a framework, or just automation. It is a combination of all these. DevOps aimed to align the Dev and Ops team with shared goals. A developer builds an application and sends it to the tester. But, the environments of development and testing systems are different; thus, the code does not work. There are two solutions to this: Docker and Virtual Machines.

Dockers have been used widely in many DevOps toolchains. Dockers platform provides numerous features that make it popular among developers. Some features include application isolation, portability, security management, Ease of software delivery, scalability, etc. Let's discuss the docker commands in more detail, along with examples! You can refer to the [best Docker courses](https://www.knowledgehut.com/devops/docker-training)
 for training related to docker and docker commands. 

What is Docker?
---------------

![Docker architecture](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

  

Docker is a platform that enables the creation, deployment, and running of applications with the help of containers. A container is a unit of software that packages the code and all its dependencies together so that the application becomes runnable irrespective of the environment. 

The container isolates the application and its dependencies into a self-contained unit that can run anywhere. Container removes the need for physical hardware, allowing for more efficient use of computing resources. Containers provide operating-system-level virtualization. Additionally, using Docker commands, developers can easily manage these containers, enhancing their productivity and workflow efficiency.

Let's understand a few of the above commands along with their usage in detail. The following are the most used docker basic commands for beginners and experienced docker professionals. 

Here is the list of 50+ basic docker commands:

Top 15 Basic Docker Commands
----------------------------

### 1\. docker –version

This command is used to get the current version of the docker 

**Syntax:**

docker - -version \[OPTIONS\] 

Copy Code

By default, this will render all version information in an easy-to-read layout. 

### 2\. docker pull

Pull an image or a repository from a registry 

**Syntax:**

docker pull \[OPTIONS\] NAME\[: TAG|@DIGEST\] 

Copy Code

To download an image or set of images (i.e. A Repository) , Once can use docker pull command 

**Example:**

$ docker pull dockerimage 

Copy Code

### 3\. docker run

This command is used to create a container from an image 

**Syntax:**

docker run \[OPTIONS\] IMAGE \[COMMAND\] \[ARG...\]

Copy Code

The docker run command creates a writeable container layer over the specified image and then starts it using the specified command.

The docker run command can be used with many variations, One can refer to the following documentation [docker run.](https://docs.docker.com/engine/reference/commandline/run/)
 

### 4\. docker ps

This command is used to list all the containers 

**Syntax:**

docker ps \[OPTIONS\]

Copy Code

The above command can be used with other options like - all or –a 

docker ps -all: Lists all containers 

**Example:**

$ docker ps 

Copy Code

$ docker ps -a 

Copy Code

### 5\. docker exec

This command is used to run a command in a running container 

**Syntax**

docker exec \[OPTIONS\] CONTAINER COMMAND \[ARG...\] 

Copy Code

Docker exec command runs a new command in a running container.

Refer to the following article for more detail regarding the usage of the docker exec command [docker exec](https://docs.docker.com/engine/reference/commandline/exec/)
. 

### 6\. docker stop

This command is used to stop one or more running containers. 

**Syntax:** 

docker stop \[OPTIONS\] CONTAINER \[CONTAINER...\] 

Copy Code

The main process inside the container will receive SIGTERM, and after a grace period, SIGKILL. The first signal can be changed with the STOPSIGNAL instruction in the container’s Dockerfile, or the --stop-signal option to docker run. 

**Example:**

$ docker stop my\_container 

Copy Code

### 7\. docker restart

This command is used to restart one or more containers. 

**Syntax:** docker restart \[OPTIONS\] CONTAINER \[CONTAINER...\] 

**Example:**

$ docker restart my\_container 

Copy Code

### 8\. docker kill

This command is used to kill one or more containers. 

**Syntax:** docker kill \[OPTIONS\] CONTAINER \[CONTAINER...\] 

**Example:**

$ docker kill my\_container 

Copy Code

### 9\. docker commit

This command is used to create a new image from the container image. 

**Syntax:** docker commit \[OPTIONS\] CONTAINER \[REPOSITORY\[:TAG\]\] 

Docker commit command allows users to take an existing running container and save its current state as an image 

There are certain steps to be followed before running the command

*   First , Pull the image from docker hub 
*   Deploy the container using the image id from first step 
*   Modify the container (Any changes ,if needed) 
*   Commit the changes 

**Example:**

$ docker commit c3f279d17e0a dev/testimage:version3. 

Copy Code

### 10\. docker push

This docker command is used to push an image or repository to a registry. 

**Syntax:** docker push \[OPTIONS\] NAME\[: TAG\] 

Use docker image push to share your images to the Docker Hub registry or to a self-hosted one. 

**Example:**

$ docker image push registry-host:5000/myadmin/rhel-httpd:lates 

Copy Code

Apart from the above commands, we have other commands for which the detailing can be found in the following link [Docker reference](https://docs.docker.com/reference/)
. 

### 11\. docker rm 

This command is used to remove one or more docker containers. We can use options such as -f i.e. force removal of running container which internally uses SIGKILL. Or -v  which removes any anonymous volumes associated with the container. 

**Syntax:** docker rm \[OPTIONS\] CONTAINER \[CONTAINER...\] 

**Example:** 

docker rm container1 

Copy Code

Removing multiple containers: 

docker rm container1 container2 container3 

Copy Code

Removing with -v and -f options: 

docker rm -v container1 

Copy Code

docker rm -f  running\_container  

Copy Code

### 12\. docker rmi

This command is used to remove one or more docker images from the system. We can use some common options such as - f for force removal of an image or --no-prune for not deleting untagged parent images. 

**Syntax:** 

docker rmi \[OPTIONS\] IMAGE  

Copy Code

*   Remove a single image: 
    

docker rmi my\_image:tag 

Copy Code

*   Remove multiple images: 
    

docker rmi image1:tag image2:tag image3:tag 

Copy Code

*   Force remove an image: 
    

docker rmi -f my\_image:tag 

Copy Code

*   Removing image without deleting untagged images: 
    

docker rmi --no-prune my\_image:tag 

Copy Code

### 13\. docker push 

This command is used to upload the docker image to a Docker registry such as  Docker Hub or a private registry. 

**Syntax:** docker push \[OPTIONS\] NAME\[:TAG\] 

**Example:**  

Command: docker push myusername/myrepository:latest 

Copy Code

###  14. docker login 

This command is used to log in to the Docker registry such as Docker Hub, a private registry, or any other third-party registry. We can use some common options such as -u for the username of the registry, -p for the password of the registry. 

**Syntax:** docker login \[OPTIONS\] \[SERVER\] 

**Examples:**  

*   Login to Docker Hub: docker login 
    

Command: docker login 

Copy Code

*   Login with username and password: 
    

Command: docker login -u myusername -p mypassword 

Copy Code

Note: In case we need to log in to other Docker registries: 

Command: docker login myregistry.com 

Copy Code

### 15\. docker start

This command is used to start one or more containers. We can use common options such as -a to attach stderr /stdout and forward signal. Also -i  option can be used as an interactive mode where the container STDIN can be attached. 

**Syntax:** docker start \[OPTIONS\] CONTAINER \[CONTAINER...\] 

**Example:**

1.  Starting Single Container:  
    

Command: docker start  container1

Copy Code

One can become DevOps certified by referring to [DevOps Certification courses](https://www.knowledgehut.com/devops)
. 

57 Essential Docker Commands List
---------------------------------

Here are the top 57 essential/ basic docker commands with descriptions to learn and use.

| **Command** | **Usage** |
| --- | --- |
| [docker attach](https://docs.docker.com/engine/reference/commandline/attach/) | Attach local standard input, output, and error streams to a running container |
| [docker build](https://docs.docker.com/engine/reference/commandline/build/) | Build an image from a Dockerfile |
| [docker builder](https://docs.docker.com/engine/reference/commandline/builder/) | Manage builds |
| [docker checkpoint](https://docs.docker.com/engine/reference/commandline/checkpoint/) | Manage checkpoints |
| [docker commit](https://docs.docker.com/engine/reference/commandline/commit/) | Create a new image from a container’s changes |
| [docker config](https://docs.docker.com/engine/reference/commandline/config/) | Manage Docker configs |
| [docker container](https://docs.docker.com/engine/reference/commandline/container/) | Manage containers |
| [docker context](https://docs.docker.com/engine/reference/commandline/context/) | Manage contexts |
| [docker cp](https://docs.docker.com/engine/reference/commandline/cp/) | Copy files/folders between a container and the local filesystem |
| [docker create](https://docs.docker.com/engine/reference/commandline/create/) | Create a new container |
| [docker diff](https://docs.docker.com/engine/reference/commandline/diff/) | Inspect changes to files or directories on a container’s filesystem |
| [docker events](https://docs.docker.com/engine/reference/commandline/events/) | Get real time events from the server |
| [docker exec](https://docs.docker.com/engine/reference/commandline/exec/) | Run a command in a running container |
| [docker export](https://docs.docker.com/engine/reference/commandline/export/) | Export a container’s filesystem as a tar archive |
| [docker history](https://docs.docker.com/engine/reference/commandline/history/) | Show the history of an image |
| [docker image](https://docs.docker.com/engine/reference/commandline/image/) | Manage images |
| [docker images](https://docs.docker.com/engine/reference/commandline/images/) | List images |
| [docker import](https://docs.docker.com/engine/reference/commandline/import/) | Import the contents from a tarball to create a filesystem image |
| [docker info](https://docs.docker.com/engine/reference/commandline/info/) | Display system-wide information |
| [docker inspect](https://docs.docker.com/engine/reference/commandline/inspect/) | Return low-level information on Docker objects |
| [docker kill](https://docs.docker.com/engine/reference/commandline/kill/) | Kill one or more running containers |
| [docker load](https://docs.docker.com/engine/reference/commandline/load/) | Load an image from a tar archive or STDIN |
| [docker login](https://docs.docker.com/engine/reference/commandline/login/) | Log in to a Docker registry |
| [docker logout](https://docs.docker.com/engine/reference/commandline/logout/) | Log out from a Docker registry |
| [docker logs](https://docs.docker.com/engine/reference/commandline/logs/) | Fetch the logs of a container |
| [docker manifest](https://docs.docker.com/engine/reference/commandline/manifest/) | Manage Docker image manifests and manifest lists |
| [docker network](https://docs.docker.com/engine/reference/commandline/network/) | Manage networks |
| [docker node](https://docs.docker.com/engine/reference/commandline/node/) | Manage Swarm nodes |
| [docker pause](https://docs.docker.com/engine/reference/commandline/pause/) | Pause all processes within one or more containers |
| [docker plugin](https://docs.docker.com/engine/reference/commandline/plugin/) | Manage plugins |
| [docker port](https://docs.docker.com/engine/reference/commandline/port/) | List port mappings or a specific mapping for the container |
| [docker ps](https://docs.docker.com/engine/reference/commandline/ps/) | List containers |
| [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) | Pull an image or a repository from a registry |
| [docker push](https://docs.docker.com/engine/reference/commandline/push/) | Push an image or a repository to a registry |
| [docker rename](https://docs.docker.com/engine/reference/commandline/rename/) | Rename a container |
| [docker restart](https://docs.docker.com/engine/reference/commandline/restart/) | Restart one or more containers |
| [docker rm](https://docs.docker.com/engine/reference/commandline/rm/) | Remove one or more containers |
| [docker rmi](https://docs.docker.com/engine/reference/commandline/rmi/) | Remove one or more images |
| [docker run](https://docs.docker.com/engine/reference/commandline/run/) | Run a command in a new container |
| [docker save](https://docs.docker.com/engine/reference/commandline/save/) | Save one or more images to a tar archive (streamed to STDOUT by default) |
| [docker search](https://docs.docker.com/engine/reference/commandline/search/) | Search the Docker Hub for images |
| [docker secret](https://docs.docker.com/engine/reference/commandline/secret/) | Manage Docker secrets |
| [docker service](https://docs.docker.com/engine/reference/commandline/service/) | Manage services |
| [docker stack](https://docs.docker.com/engine/reference/commandline/stack/) | Manage Docker stacks |
| [docker start](https://docs.docker.com/engine/reference/commandline/start/) | Start one or more stopped containers |
| [docker stats](https://docs.docker.com/engine/reference/commandline/stats/) | Display a live stream of container(s) resource usage statistics |
| [docker stop](https://docs.docker.com/engine/reference/commandline/stop/) | Stop one or more running containers |
| [docker swarm](https://docs.docker.com/engine/reference/commandline/swarm/) | Manage Swarm |
| [docker system](https://docs.docker.com/engine/reference/commandline/system/) | Manage Docker |
| [docker tag](https://docs.docker.com/engine/reference/commandline/tag/) | Create a tag TARGET\_IMAGE that refers to SOURCE\_IMAGE |
| [docker top](https://docs.docker.com/engine/reference/commandline/top/) | Display the running processes of a container |
| [docker trust](https://docs.docker.com/engine/reference/commandline/trust/) | Manage trust on Docker images |
| [docker unpause](https://docs.docker.com/engine/reference/commandline/unpause/) | Unpause all processes within one or more containers |
| [docker update](https://docs.docker.com/engine/reference/commandline/update/) | Update configuration of one or more containers |
| [docker version](https://docs.docker.com/engine/reference/commandline/version/) | Show the Docker version information |
| [docker volume](https://docs.docker.com/engine/reference/commandline/volume/) | Manage volumes |
| [docker wait](https://docs.docker.com/engine/reference/commandline/wait/) | Block until one or more containers stop, then print their exit codes |

Docker Use Cases
----------------

Let's understand a few of the docker use cases: 

**Use case 1:** Developers write their code locally and can share it using docker containers. 

**Use case 2:** Fixing the bugs and deploying them into the respective environments is as simple as pushing the image to the respective environment. 

**Use case 3:** Using docker one can push their application to the test environment and execute automated and manual tests 

**Use case 4:** One can make their deployment responsive and scalable by using docker since docker can handle dynamic workloads feasibility. 

### **Let us take an example of an application,** 

When a company wants to develop a web application, it needs an environment where they have a Tomcat server installed. Once the tester set up a tomcat environment and test the application, it is deployed into a production environment. Once again the tomcat has to be setup in a production environment to host the java web application There are some issues with this approach: 

*   Loss of time and effort. 
*   Developer and tester might use a different tomcat versions. 

Now, let's see how the Docker container can be used to prevent this loss.

In order to overcome the issues, docker will be used by a developer to create a docker image using a base image which is already existing in Docker hub. Docker hub has some base images available for free. Now this image can be used by the developer, tester, and the system admin to deploy a Tomcat environment using Docker Commands. In this way, Docker container solves the problem.

Docker Architecture
-------------------

Docker architecture generally consists of a Docker Engine which is a client-server application with three major components: 

1.  Generally, docker follows a client-server architecture 
2.  The client communicates with the daemon, which generally takes up the task of building,running, and shipping the docker containers. 
3.  The client and daemon communicate using REST API calls. These calls act as an interface between the client and daemon 
4.  A command-line interface, Docker CLI runs docker commands. Some basic docker commands with examples are listed in the next section. 
5.  Registry stores the docker images 

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Conclusion
----------

DevOps (development + operations) is an evolution born between developers and system administrators. One of the main tasks of [DevOps](https://www.toolshero.com/information-technology/devops-methodology/)
 is the automation and centralization of software development and deployment. One of the most popular tools that helps solve this task is Docker. To get a better understanding of Docker commands and more, enroll in [Docker Kubernetes training](https://www.knowledgehut.com/devops/docker-with-kubernetes-training)
. 

Three main features of Docker products are the most distinguishing: 

*   Quick deployment in a variety of environments 
*   Greatly facilitated testing 
*   Possibility of using Docker as a development environment.

Learning the top Docker commands is essential for any DevOps professional looking to streamline container management and deployment processes. As you continue to explore and learn more about Docker, keeping these commands at your fingertips will prove invaluable in your journey toward DevOps operational excellence.

Frequently Asked Questions (FAQs)
---------------------------------

1. What do you mean by Docker command line?

Docker CLI (command line interface) is a command-line tool that is used to interact with the docker daemon. To get the list of commands either run docker with no parameters or execute the docker help command.   

2. How many commands are there in Docker?

Docker has 13 Management commands and 41 general commands. One can run the docker command using the docker CLI tool. To list available commands, either run docker with no parameters or execute docker help.   

3. What is an image in Docker?

An image is a read-only template with instructions for creating a Docker container. The container is a runnable instance, while image is a read only template of it. Using the command docker pull one can get the images from the docker registry.   

4. How can I run a docker command?

One can run a docker command using the Docker CLI tool. Docker command line interface tool is preferably used to run docker commands Docker CLI tool can be installed along with docker.  

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![Profile](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

#### Lakshmi Sushmitha V

Author

[](https://www.linkedin.com/in/lakshmi-susmitha-251b29b0/)

I am an ambitious software professional with 5 years of experience in the industry working with various tech  gaints. I am an inquisitive person who always interested to explore the things and takeup challenges.Apart from profession , I love travelling,reading books,blogging and editing.

Share This Article

[](http://www.facebook.com/sharer/sharer.php?u=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](http://twitter.com/share?via=Knowledgehut&url=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](https://www.linkedin.com/cws/share?url=https://www.knowledgehut.com/blog/devops/basic-docker-commands)
[](https://web.whatsapp.com/send?text=https://www.knowledgehut.com/blog/devops/basic-docker-commands)

Top 55+ Basic Docker Commands You Must Learn in 2024

Top 55+ Basic Docker Commands You Must Learn in 2024

First name\*

Error

Last name\*

Error

Email\*

Something went wrong

+1

Phone\*

Something went wrong

Your Message (Optional)

I want to receive updates directly on WhatsApp.

Top 55+ Basic Docker Commands You Must Learn in 2024

Join Our Community

Get Benefits of

Free Learning resources

😍

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Join whatsapp icon](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)Join Telegram](https://t.me/KH_Consultation)

#### Upcoming DevOps Batches & Dates

| Name | Date | Fee | Know more |
| --- | --- | --- | --- |

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkiIGhlaWdodD0iMTkiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Course advisor icon](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Course Advisor

Connect with us

*   [](https://www.linkedin.com/company/upgradknowledgehut/)
    
*   [](https://www.facebook.com/KnowledgeHut.Global)
    
*   [](https://www.instagram.com/knowledgehut.global/)
    
*   [](https://www.youtube.com/user/TheKnowledgehut)
    
*   [](https://twitter.com/KnowledgeHut)
    
*   [](https://www.knowledgehut.com/blog/feed)
    

Get Our Weekly Newsletter

We Accept

USA: [+1-469-442-0620](tel:+1-469-442-0620)
, [+1-832-684-0080](tel:+1-832-684-0080)

India: Toll Free [1800-121-9232](tel:1800-121-9232)

UK: [+44-2036085923](tel:+44-2036085923)

Singapore: [+65-317-46174](tel:+65-317-46174)

Malaysia: [+601548770914](tel:+601548770914)

Canada: [+1-613-707-0763](tel:+1-613-707-0763)

New Zealand: [+64-36694791](tel:+64-36694791)

Ireland: [+353-12708328](tel:+353-12708328)

Australia: [+61-290995641](tel:+61-290995641)

UAE: Toll Free [8000180860](tel:8000180860)

Company

*   [About Us](/about-us "About Us")
    
*   [Careers](/career "Careers")
    
*   [Customer Speak](/customer-speak "Customer Speak")
    
*   [Accreditation](/accreditation "Accreditation")
    
*   [Media](/media "Media")
    
*   [Contact Us](/contact-us "Contact Us")
    
*   [Grievance Redressal](/complaint-forum "Grievance Redressal")
    

Offerings

*   [Live virtual (online)](/courses "Live virtual (online)")
    
*   [Classroom](/courses "Classroom")
    
*   [Agile Services](/agile-services "Agile Services")
    
*   [Corporate Training](/corporate-training "Corporate Training")
    

Resources

*   [Course Info](/info "Course Info")
    
*   [Tutorials](/tutorials "Tutorials")
    
*   [Blog](/blog "Blog")
    
*   [Interview Questions](/interview-questions "Interview Questions")
    
*   [Practice Tests](/practice-tests "Practice Tests")
    
*   [Master Classes](/master-classes "Master Classes")
    

Partner with us

*   [Become an Instructor](/become-an-instructor "Become an Instructor")
    
*   [Hire from Us](/hire-from-us-engineers "Hire from Us")
    
*   [Affiliates](/affiliate-program "Affiliates")
    

Support

*   [FAQs](/faqs "FAQs")
    
*   [Terms & Conditions](/terms-conditions "Terms & Conditions")
    
*   [Privacy Policy & Disclaimer](/privacy-policy "Privacy Policy & Disclaimer")
    
*   [Cancellation & Refund Policy](/refund-policy "Cancellation & Refund Policy")
    
*   [Site map](/html-sitemap "Site map")
    

Company

*   [About Us](/about-us "About Us")
    
*   [Careers](/career "Careers")
    
*   [Customer Speak](/customer-speak "Customer Speak")
    
*   [Accreditation](/accreditation "Accreditation")
    
*   [Media](/media "Media")
    
*   [Contact Us](/contact-us "Contact Us")
    
*   [Grievance Redressal](/complaint-forum "Grievance Redressal")
    

Offerings

*   [Live virtual (online)](/courses "Live virtual (online)")
    
*   [Classroom](/courses "Classroom")
    
*   [Agile Services](/agile-services "Agile Services")
    
*   [Corporate Training](/corporate-training "Corporate Training")
    

Resources

*   [Course Info](/info "Course Info")
    
*   [Tutorials](/tutorials "Tutorials")
    
*   [Blog](/blog "Blog")
    
*   [Interview Questions](/interview-questions "Interview Questions")
    
*   [Practice Tests](/practice-tests "Practice Tests")
    
*   [Master Classes](/master-classes "Master Classes")
    

Partner with us

*   [Become an Instructor](/become-an-instructor "Become an Instructor")
    
*   [Hire from Us](/hire-from-us-engineers "Hire from Us")
    
*   [Affiliates](/affiliate-program "Affiliates")
    

Support

*   [FAQs](/faqs "FAQs")
    
*   [Terms & Conditions](/terms-conditions "Terms & Conditions")
    
*   [Privacy Policy & Disclaimer](/privacy-policy "Privacy Policy & Disclaimer")
    
*   [Cancellation & Refund Policy](/refund-policy "Cancellation & Refund Policy")
    
*   [Site map](/html-sitemap "Site map")
    

Top Categories

*   [Agile Management Courses](/agile-management "Agile Management Courses")
    
*   [Project Management Courses](/project-management-certifications "Project Management Courses")
    
*   [IT Service Management Courses](/itsm-certifications "IT Service Management Courses")
    
*   [Programming Courses](/programming-certification "Programming Courses")
    
*   [Web Development Courses](/web-development-courses "Web Development Courses")
    
*   [Mobile App Development Courses](/mobile-app-development-courses "Mobile App Development Courses")
    
*   [Six Sigma Courses](/six-sigma-certifications "Six Sigma Courses")
    
*   [Cloud Computing Courses](/cloud-computing-courses "Cloud Computing Courses")
    
*   [Devops Courses](/devops-courses "Devops Courses")
    
*   [Business Management Courses](/business-management-courses "Business Management Courses")
    
*   [Data Science Courses](/data-science-courses "Data Science Courses")
    
*   [BI and Visualization Courses](/business-intelligence-and-visualization "BI and Visualization Courses")
    
*   [Quality Management Courses](/quality-management-courses "Quality Management Courses")
    
*   [Kanban Courses](/kanban-certifications "Kanban Courses")
    

Top Courses

*   [CSM Certification](/agile-management/csm-certification-training "CSM Certification")
    
*   [CSPO Certification](/agile-management/cspo-certification-training "CSPO Certification")
    
*   [Leading SAFe 6.0 Certification](/agile-management/leading-safe-certification-training "Leading SAFe 6.0 Certification")
    
*   [PSM Certification](/agile-management/psm-certification-training "PSM Certification")
    
*   [PMP Certification](/project-management/pmp-certification-training "PMP Certification")
    
*   [ITIL Foundation Certification](/it-service-management/itil-foundation-certification-training "ITIL Foundation Certification")
    
*   [PRINCE2 Certification](/project-management/prince2-foundation-and-practitioner-certification-training "PRINCE2 Certification")
    
*   [Devops Foundation Certification](/devops/devops-foundation-certification-training "Devops Foundation Certification")
    
*   [Data Science with Python Certification](/data-science/data-science-with-python-certification-training "Data Science with Python Certification")
    
*   [Full-Stack Development Bootcamp](/web-development/fullstack-development-bootcamp-training "Full-Stack Development Bootcamp")
    
*   [Front-End Development Bootcamp](/web-development/front-end-development-bootcamp-training "Front-End Development Bootcamp")
    
*   [Python Certification Training](/programming/python-programming-certification-training "Python Certification Training")
    

Top Categories

*   [Agile Management Courses](/agile-management "Agile Management Courses")
    
*   [Project Management Courses](/project-management-certifications "Project Management Courses")
    
*   [IT Service Management Courses](/itsm-certifications "IT Service Management Courses")
    
*   [Programming Courses](/programming-certification "Programming Courses")
    
*   [Web Development Courses](/web-development-courses "Web Development Courses")
    
*   [Mobile App Development Courses](/mobile-app-development-courses "Mobile App Development Courses")
    
*   [Six Sigma Courses](/six-sigma-certifications "Six Sigma Courses")
    

*   [Cloud Computing Courses](/cloud-computing-courses "Cloud Computing Courses")
    
*   [Devops Courses](/devops-courses "Devops Courses")
    
*   [Business Management Courses](/business-management-courses "Business Management Courses")
    
*   [Data Science Courses](/data-science-courses "Data Science Courses")
    
*   [BI and Visualization Courses](/business-intelligence-and-visualization "BI and Visualization Courses")
    
*   [Quality Management Courses](/quality-management-courses "Quality Management Courses")
    
*   [Kanban Courses](/kanban-certifications "Kanban Courses")
    

Top Courses

*   [CSM Certification](/agile-management/csm-certification-training "CSM Certification")
    
*   [CSPO Certification](/agile-management/cspo-certification-training "CSPO Certification")
    
*   [Leading SAFe 6.0 Certification](/agile-management/leading-safe-certification-training "Leading SAFe 6.0 Certification")
    
*   [PSM Certification](/agile-management/psm-certification-training "PSM Certification")
    
*   [PMP Certification](/project-management/pmp-certification-training "PMP Certification")
    
*   [ITIL Foundation Certification](/it-service-management/itil-foundation-certification-training "ITIL Foundation Certification")
    

*   [PRINCE2 Certification](/project-management/prince2-foundation-and-practitioner-certification-training "PRINCE2 Certification")
    
*   [Devops Foundation Certification](/devops/devops-foundation-certification-training "Devops Foundation Certification")
    
*   [Data Science with Python Certification](/data-science/data-science-with-python-certification-training "Data Science with Python Certification")
    
*   [Full-Stack Development Bootcamp](/web-development/fullstack-development-bootcamp-training "Full-Stack Development Bootcamp")
    
*   [Front-End Development Bootcamp](/web-development/front-end-development-bootcamp-training "Front-End Development Bootcamp")
    
*   [Python Certification Training](/programming/python-programming-certification-training "Python Certification Training")
    

Disclaimer: The content on the website and/or Platform is for informational and educational purposes only. The user of this website and/or Platform (User) should not construe any such information as legal, investment, tax, financial or any other advice. Nothing contained herein constitutes any representation, solicitation, recommendation, promotion or advertisement on behalf of KnowledgeHut and / or its Affiliates (including but not limited to its subsidiaries, associates, employees, directors, key managerial personnel, consultants, trainers, advisors). The User is solely responsible for evaluating the merits and risks associated with use of the information included as part of the content. The User agrees and covenants not to hold KnowledgeHut and its Affiliates responsible for any and all losses or damages arising from such decision made by them basis the information provided in the course and / or available on the website and/or platform. KnowledgeHut reserves the right to cancel or reschedule events in case of insufficient registrations, or if presenters cannot attend due to unforeseen circumstances. You are therefore advised to consult a KnowledgeHut agent prior to making any travel arrangements for a workshop. For more details, please refer to the [Cancellation & Refund Policy](/refund-policy "Cancellation & Refund Policy")
.

CSM®, CSPO®, CSD®, CSP®, A-CSPO®, A-CSM® are registered trademarks of Scrum Alliance®. KnowledgeHut Solutions Pvt. Ltd. is a Registered Education Ally (REA) of Scrum Alliance®. PMP is a registered mark of the Project Management Institute, Inc. CAPM is a registered mark of the Project Management Institute, InRead More

© 2011-2024, KnowledgeHut Solutions Private Limited. All Rights Reserved

*   [Privacy policy](/privacy-policy)
    
*   [Terms of service](/terms-conditions)
    

Hello! Ready to elevate your career? Explore 500+ future-ready courses with KnowledgeHut upGrad 🚀x

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTYiIGhlaWdodD0iNTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Chat bot icon](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

1

Fast forward your career with 500+ future-ready courses ⏩💻👩‍🎓📚x

![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Whatsapp/Chat icon](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

1

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Phone icon for mobile](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](tel:+918448445027)
[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Chat icon for mobile](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)](https://api.whatsapp.com/send/?phone=917618793167&text=I%20am%20ready%20to%20accelerate%20my%20career%20growth%20by%20upskilling%20P-35tvjfzp&type=phone_number&app_absent=0)
![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTAiIGhlaWdodD0iNTAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmVyc2lvbj0iMS4xIi8+)![Chat icon for mobile](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![](https://www.knowledgehut.com/www.linkconnector.com/tu.php?pid=165589&nv=user-location%3D%7B%22country%22%3A%7B%22id%22%3A102%2C%22code%22%3A%22US%22%2C%22name%22%3A%22United%20States%22%2C%22slug%22%3A%22unitedstates%22%2C%22isd%22%3A%22%2B1%22%7D%2C%22region%22%3A%7B%22id%22%3A%225%22%2C%22name%22%3A%22Americas%22%2C%22slug%22%3A%22americas%22%7D%2C%22currency%22%3A%7B%22id%22%3A74%2C%22name%22%3A%22USD%22%7D%2C%22city%22%3A%7B%22id%22%3A240%2C%22name%22%3A%22Chicago%2C%20IL%22%2C%22slug%22%3A%22chicago%22%2C%22timezone_abbr%22%3A%22CST%22%2C%22timezone_name%22%3A%22America%2FChicago%22%7D%7D%2C%20rl_user_id%3DRudderEncrypt%253AU2FsdGVkX18PP9RpY0ARbgWrvf%252FV5861S%252BM2zwOO6Ak%253D%2C%20rl_trait%3DRudderEncrypt%253AU2FsdGVkX1%252BYZchv4fBFYQ3sz6AURRQ2Uju6%252FeWk5LQ%253D%2C%20rl_group_id%3DRudderEncrypt%253AU2FsdGVkX1%252B5dPhlN56cz4djiyK6k81OuiTualmHN8g%253D%2C%20rl_group_trait%3DRudderEncrypt%253AU2FsdGVkX1%252FJEbuN3nsc0kVfGMVdi8xOSU3cIE1KvBQ%253D%2C%20rl_anonymous_id%3DRudderEncrypt%253AU2FsdGVkX1%252FhCIOuvh1oO5JGzOPXc5Lyhsa97H8QEmUdP%252F9lwfCsTEMiIwl84eNfEJcGncqcCa%252F79wr7bgOwJA%253D%253D%2C%20rl_page_init_referrer%3DRudderEncrypt%253AU2FsdGVkX19fV%252FlXyvp0BILItzUIyvYthD%252B%252FumU%252Bsi4%253D%2C%20rl_page_init_referring_domain%3DRudderEncrypt%253AU2FsdGVkX1%252FO%252B9OYrKTrc1nAOYy7g4xPdSHxuZ%252FrL7Y%253D%2C%20_uc_referrer%3Ddirect%2C%20_uc_last_referrer%3Ddirect%2C%20_uc_initial_landing_page%3Dhttps%253A%2F%2Fwww.knowledgehut.com%2Fblog%2Fdevops%2Fbasic-docker-commands%2C%20_uc_current_session%3Dtrue%2C%20_uc_visits%3D1%2C%20_gcl_au%3D1.1.529195932.1723789980%2C%20rl_session%3DRudderEncrypt%253AU2FsdGVkX18g1CER1%252FuRTF0qO7q4DXco8Uj6FrYiFdQmDSLpXDrVu8NEjuL5xYhj8fjd7rMzcV1ha1wPw%252B%252BzdRkH%252B9ijawiuCvetoG%252FtPenEWy5z2Dvh3DapDTQZP4ObaPFEAkw3JzN9KK0K4YHHKQ%253D%253D%2C%20_gid%3DGA1.2.1094597308.1723789980%2C%20_gat_gtag_UA_65830755_1%3D1%2C%20_ga_SK97XFVRE8%3DGS1.1.1723789979.1.0.1723789979.0.0.0%2C%20_ga%3DGA1.1.595064849.1723789980%2C%20_ga_5LZ1E5WWE3%3DGS1.1.1723789980.1.0.1723789980.60.0.0)![](https://www.knowledgehut.com/www.linkconnector.com/js/uts_uid.php?cgid=902026&uts_protocol=)

![](https://bat.bing.com/action/0?ti=20264832&tm=gtm002&Ver=2&mid=8b7c080f-ef45-4f9d-b10b-df75cbe71afb&sid=61f8d8505b9911ef95d2fd20780b32b1&vid=61fa1f405b9911ef8ebb6d4d492c9de1&vids=1&msclkid=N&uach=pv%3D10.0&pi=918639831&lg=en-US&sw=1280&sh=720&sc=16&tl=Top%2055%2B%20Basic%20Docker%20Commands%20You%20Must%20Learn%20in%202024&p=https%3A%2F%2Fwww.knowledgehut.com%2Fblog%2Fdevops%2Fbasic-docker-commands&r=&lt=1179&evt=pageLoad&sv=1&cdb=AQAQ&rn=247187)

---

# The Prompt

adduser adduser dsoneil | This command will automatically add a new user to the system
| The Bash script can be found in /usr/sbin if it needs to be changes
alias alias help=man | The alias command allows you to substitute a new name for a command
alias long=ls -al | An alias can also contain command line options
| Unless the alias definition is included in your .login file it is only temporary
apropos apropos keyword | Display command names based on keyword search
at at 1:23 lp /home/index.html | The at command runs a list of commands at a specified time (e.g. print @ 1:23)
at 1:50 echo “lp Job Done” | This uses the echo command to send a message at 1:50 saying a print job is done
at -l | Lists all scheduled jobs; an alias for the atq command
at -d 5555 | This will cancel job number 5555; an alias for the atrm command
batch Example: | Temporarily blank
cat cat /etc/filename | Prints specified file to the screen
cat file.a > file.b | Moves file.a to file.b
cat file.a > file.b | Appends the content of file.a to the end file.b
cd cd /home/dsoneil | Changes directories to the specified one
cd ~username | This will move you to the users specified home directory
chfn chfn dsoneil | This will allow you to change finger information on that user
| As an example it will allow you to change dsoneil to Darcy S. O’Neil
chmod chmod 666 filename | This command will give a file Read - Write permission for everyone
chmod 777 filename | This command gives Read - Write - Execute permission to everyone
chmod a=rwx file | This gives Read - Write - Execute permission to all users
For a complete listing of the available chmod permission commands please refer to Page 4 - Table 1
chown chown dso /home/html | This command will change the owner of the specified directory to dso
chown dso /home/file.a | This command will change the owner of the specified file to dso
clear clear | This will clear your screen
cmp cmp -s file.a file.b | Compares 2 files of any type. The -s option will return nothing in the files arethe same
cp cp file.a file.b | This will create a duplicate of file.a under a new file name, file.b
cpio ls /home | cpio -o > /root | This will copy the files of /home to the directory /root
cpio -it < /root > bk.indx | This will extract all of the files to /root and creates an index file called bk.indx
cpkgtool | Graphical front end to installpkg, removepkg, makepkg that uses ncurses.
cron |Comming Soon!
du du -k /home/html | Provides a summary of the disk space usage, in kb, within the specified path
du -k /home/html/file.a | Provides a summary of disk spaced used by a particular file
df df -h | Displays the total size, used and available space on all mounted file systems
fdformat fdformat /dev/fd0 | low level format of a floppy device in drive fd0
fdformat /dev/fd0H1440 | This will fromat a “Double Sided High Density”disk
file file file.a | This command will try to determine what type of file file.a is. (exec, text, etc.)
file -z file.a.tar | Looks inside a compressed file to determine it’s type.
file -L file.a | Follows symbolic links to be followed to determine file type
find find /path -name passwd | Locates the specified string (passwd), starting in the specified directory (/path)
| All filenames or directories containing the string will be printed to the screen
finger finger | This will list all users currently logged into the UNIX system
free free -t -o | Provides a snapshot of the system memory usage
fsck fsck /hda | file system check and repair
git | This is a file system viewer
grep cat /etc/passwd | grep dso | This searches for and limits the command output to the pattern specified
| In this case all instances of dso from the /etc/passwd file are printed
grep -i “Sample” /home/dsoneil | The -i option makes the search indifferent to case (e.g. sample or SAMPLE)
groupadd groupadd sudos | Create a new group called sudos on the system
groups groups | Shows which groups you are in
gzip gzip file.a | This will zip file.a and give it the extension file.a.gz
gzip -d file.a.gz | This will unzip the file file.a.gz
tar -zxvf file.a.tar.qz | The z flag allow you to decompress the tar file on the fly
hostname | Get or set hostname. Typically, the host name is stored in the file /etc/HOSTNAME.
Canadian Linux Users Group
Command Synopsis Description
www.linux.ca
Linux Command Summary
Release
Version 0.92
27.06.01
Ifconfig ifconfig eth0 | This will display the status of the currently defined interface (.e.g Ethernet Card 0)
ifconfig eth0 up | This flag causes the iterface to be activated (To deactivate an interface use down)
ifconfig eth1 192.168.0.2 up | Makes eth1 active with IP address 192.168.0.2
insmod | used (by root) to install modular device drivers
installpkg installpkg -r packagename.tgz | This will install a Slackware package with the name you specify (-r option)
removepkg removepkg -copy packagename | This will remove the named package but make a copy in the /tmp directory
rpm2targz rpm2targz filename.rpm | This will convert an RPM file to a Slackware .tgz package
upgradepkg upgradepkg packagename.tgz | This will upgrade a Slackware package and remove any old or no used files
jobs jobs | This will list all jobs presently running on your system
kernelcfg | GUI to add/remove kernel modules (as root in X terminal).
kill kill 2587 | Kills the process specified by the Process ID Number (2587)
kill -9 2587 | The -9 flag forces the process to die
last last -300 | Prints to the screen the username, location, log-in and log-off times of the last
last -5 username | -x logins to the system. The username will select the last x time that person has
| used the system. The last command is not traceable.
lastlog lastlog | Displays a list of the login attempts / times of all users on the system (security check)
less less /html/index.html | Less displays information a screen at a time, you can also page back and forth
ln ln -s /usr/dso ./home/html | Creates a “soft” link from the first directory or file to the second. A user changing
| into ./home/html will actually be directed to the /usr/dso directory.
locate locate wordperfect | The locate command will locate the file specified aand output a directory path (see “updatedb”)
lpr lpr /home/html/index.html | This command will print the file index.html to the printer
lprm lprm 12 | This command will cancel pint job 12 in the printer queue
lpq lpq | This will show the contents of the print queue
ls ls -al | Lists all information on all files (-a) in the current directory in single line
| format (-l). Includes permissions, owners, modification time, file size and name
ls -F | Marks (directories with a trailing / ) - ( executables with an *) (symbolic links w/ @)
lsmod | used (by root) to show kernel modules currently loaded
make make mrproper | Cleans up junk accidentally left behind by the development team
make xconfig | This will ask you a series of questions about your system and drive requirements
make dep | This will uses dependencies
make clean | The clean command will clean up any unnecessary files left lying around
make bzImage | This will begin the process of compiling your new kernel
make lnx | This specified that the source will be compiled under a Linux system
make install | After the make command this will install the compiled binaries to their directories
| To create a log of installed programs do: make install > /root/install_logs/program-1.0
man man vi | Prints the manual page on the specific topic (vi) to the screen. To scroll down
| the page use the Space Bar, to scroll up use the letter b, to exit press the q key.
mkdir mkdir pascal | This will create new directory (pascal) in the present directory
mkfs mkfs -t msdos -c -v /dos-drive | Formats a partition and builds a new filesystem on it
mkfs -t xfs -c -v /home | -t specifies filesystem type, -v produces verbose output, -c checks for bad blocks
more more /home/html/index.htm | Paginates the specified file so it can be read line by line (using Enter key) or
| screen by screen using the Space Bar. Use b key to move back and q to quit.
mount mount -t msdos /dev/hda5 /dos | Mounts the msdos partition on the Hard Drive (hda5) to the directory /dos
mount -t iso9660/dev/sr0 /cd | Mounts the CD-ROM under the directory /cd
mount -t msdos /dev/fd0 /mnt | Mounts the floppy drive with an msdos file system to /mnt
mount -a /etc/fstab | Attempts to mount all file systems located in the /etc/fstab file
mv mv ./home/file ./dso/file | Moves the specified file to another directory
nice nice -5 sort one.a > two.b | This command adjusts the priority of a process before it starts
| The higher the number the lower the priority. All process start at 10
nohup | This command allows a process to continue after you log out
passwd passwd | Launches the password program so the user can change their password
ps ps | Lists all current running processes, their corresponding pids, and their status
ps -ef | grep dsoneil | This will find all of the processes for user dsoneil
pstree pstree -p | Provides a list of running processes in a tree structure
pwd pwd | Prints the current working directory
quota quota | Lists the user’s quotas for both ada (/home/ada/a#/username) and amelia
| (/var/spool/mail/username), indicating the number of blocks used and the users quota.
Command Synopsis Description
Linux Command Summary
Release
Version 0.92
27.06.01
Canadian Linux Users Groupwww.linux.ca
renice renice -5 12345 | Adjusts the priority of the running process 12345 (The 5 lowers the priority)
rm rm file.a | Removes the specified file in your current directory
rm -i file.a | Removes specified file but prompts for confirmation before deleting
rm -r /home/dso | Removes the specified directory and all files in that directory
rmdir rmdir pascal | Removes the empty directory specified, if not empty you will receive an error
rmdir -r pascal | Removes the directory and all files in that directory
route route -n | Displays the Linux Kernel IP routing table
route add -net 192.168.0.0 eth0 | This will tell other systems what network to route your system on
route add default gw 192.168.0.5 eth0 | This will tell the your system where the Internet gateway is located
| This information can be added to you /etc/rc.d/rc.local system files (Slackware)
rpm rpm -i file.2.0-i386.rpm | This will unpack an RPM file. This is the most basic method of installation
rpm -U file.2.0-i386.rpm | This will install an upgrade to a previous RPM package.
rpm -i –force file.rpm | The –force option will force the package to re-install
rpm -e file.2.0-i386.rpm | This will remove and RPM package. (You do not need to use the complete name)
rpm -i –nodeps file.rpm | This command uses the “no dependencies” flag.
rpm -qa | This will give a screen print out of all packages installed (q is query)
rpm -qa | grep gtk | This will print out all of the rpm packages will gtk in the file name
rpm -qi file.2.0-i386.rpm | This will provide information on the package you are about to install
rpm –rebuild file.2.0.rpm | This will rebuild a package if it has been corrupted by another installation process
su su username | This will allow you to access the Superuser privileges. Type exit to revert back to normal
shutdown shutdown -t 10.00 | This will notify all logged in users that the system will shut down at 10:00 AM
shutdown -r -t 20.00 | This will reboot the system at 8:00 PM
shutdown -t +10 good day | This will shutdown the system in 10 minutes with the message “good day” sen
shutdown -f | The -f flag will cause Linux to do a fast reboot
tar tar -cf /user/dso /home | This command copies the directory /home to the directory /user/dso
tar cvf /backup.tar /dso | This will create a tar archive of everything in the directory /dso
tar -xvf file.a.tar | This command will extract the tar archive
tar -tvf file.a.tar | more | This will allow you to check whether the tar archive starts with a directory
tar -zxvf file.a.tgz | This command will unzip and extract the file in one step as opposed to using gzip
top M for memory usage information | This program shows a lot of stuff that goes on with your system. In the
P for CPU information | program, you can type: q to quit
touch touch file.a | Creates an empty file in the current directory with the name file.
uname uname -a | This will print to the screen the Linux Kernel in use on your system
updatedb updatedb | This will update the “locate” database
userdel userdel -r dsoneil | This will delete the user dsoneil from the system, the -r option will delete the users /home directory
w w | Lists all users currently logged into the UNIX system. Provides information such
| as username, login time, idle time, and current action
which which -a filename | This will search through all directories in your current path and find all files named filename
who who | Lists currently logged on users username, port, and when they logged in
whoami whoami | Tells the user who they are acting as; usually their own username

output this is json format the format is given in <format></format>

<format>
{
"data": [
{"id": "command name"}
]}
</format>

do for full. Complete output

# The Output

{
  "data": [
    {"id": "docker attach"},
    {"id": "docker build"},
    {"id": "docker builder"},
    {"id": "docker checkpoint"},
    {"id": "docker commit"},
    {"id": "docker config"},
    {"id": "docker container"},
    {"id": "docker context"},
    {"id": "docker cp"},
    {"id": "docker create"},
    {"id": "docker diff"},
    {"id": "docker events"},
    {"id": "docker exec"},
    {"id": "docker export"},
    {"id": "docker history"},
    {"id": "docker image"},
    {"id": "docker images"},
    {"id": "docker import"},
    {"id": "docker info"},
    {"id": "docker inspect"},
    {"id": "docker kill"},
    {"id": "docker load"},
    {"id": "docker login"},
    {"id": "docker logout"},
    {"id": "docker logs"},
    {"id": "docker manifest"},
    {"id": "docker network"},
    {"id": "docker node"},
    {"id": "docker pause"},
    {"id": "docker plugin"},
    {"id": "docker port"},
    {"id": "docker ps"},
    {"id": "docker pull"},
    {"id": "docker push"},
    {"id": "docker rename"},
    {"id": "docker restart"},
    {"id": "docker rm"},
    {"id": "docker rmi"},
    {"id": "docker run"},
    {"id": "docker save"},
    {"id": "docker search"},
    {"id": "docker secret"},
    {"id": "docker service"},
    {"id": "docker stack"},
    {"id": "docker start"},
    {"id": "docker stats"},
    {"id": "docker stop"},
    {"id": "docker swarm"},
    {"id": "docker system"},
    {"id": "docker tag"},
    {"id": "docker top"},
    {"id": "docker trust"},
    {"id": "docker unpause"},
    {"id": "docker update"},
    {"id": "docker version"},
    {"id": "docker volume"},
    {"id": "docker wait"}
  ]
}

# Next Steps
- Plugged this into my random_dsa_sheet_opener project
- Thanks to me that I made this project easily extensible by using the Factory Method pattern
- [ ] I now need to integrate it with ChatGPT to get the details with explanation and examples
- [ ] Then send the result over email
- [ ] I plan to do this using OpenAPI and FastAPI