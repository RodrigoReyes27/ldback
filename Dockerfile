FROM alpine:3.19.1

# Avoid geographic area configuration
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk upgrade
RUN apk add python3
RUN apk add py3-pip
RUN apk update
RUN apk add nodejs
RUN apk add npm

# Create a directory for the application
RUN mkdir -p /home/app
WORKDIR /home/app

# Expose PORTS for firebase emulator
# ui
EXPOSE 4000
# hub
EXPOSE 4400
# logging
EXPOSE 4600
# functions
EXPOSE 5001
# firestore
EXPOSE 8080
# pubsub
EXPOSE 8085
# database
EXPOSE 9000
# auth
EXPOSE 9099
# Storage
EXPOSE 9199
# Hosting
EXPOSE 6000

# Install python dependencies && node dependencies && start firebase emulator
COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]