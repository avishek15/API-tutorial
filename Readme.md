# To build a Dockerfile, open the folder with your DOckerfile in terminal and run the following

```
docker build -t similarity:0.1 .
```

# To run run the built image, run the following command

```
docker run -v ./albert:/albert -p 80:8000 similarity:0.1
```