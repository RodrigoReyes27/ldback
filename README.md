# LDBack

npm install -g firebase
npm install -g firebase-tools

Python 3.11 is needed

# start development instance

firebase emulators:start --only functions

# run unittests from root directory

python -m unittest ./functions/app/test test_create_account.py
