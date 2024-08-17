# Run the following commands to build and run the docker container

```bash

docker build -t myimage .

docker run -d --name mycontainer -p 8080:8080 myimage
    
```