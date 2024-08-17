# Run the following commands to build and run the docker container

```bash

docker build -t myimage .

docker run -d --name mycontainer -p 8080:8080 myimage
    
```

# Deploying on Cloud Run

gcloud auth login
docker build -t gcr.io/mproj-404317/mad-back .
gcloud auth configure-docker
docker push gcr.io/mproj-404317/mad-back
gcloud run deploy mad-back --image gcr.io/mproj-404317/mad-back:latest --platform managed --region us-central1 --allow-unauthenticated --service-account 389410602539-compute@developer.gserviceaccount.com
 


