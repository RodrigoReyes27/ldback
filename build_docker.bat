docker rmi -f frida_backend
docker build -t frida_backend .
docker run --name=frida_backend --rm ^
        -p 4000:4000 ^
        -p 4400:4400 ^
        -p 4500:4500 ^
        -p 5001:5001 ^
        -p 8081:8081 ^
        -p 9005:9005 ^
        --volume "%cd%":/home/app -it frida_backend