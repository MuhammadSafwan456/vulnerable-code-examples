import os

def insecure_function(secret):
    print("Received secret: " + secret)
    print("Received secret: " + secret)

user_input = "sensitivesecret"
insecure_function(user_input)

# (CWE-359)
# This sample Python file contains a function that prints a secret to the console without any security measures.
# It can be used to test SAST tools' ability to identify sensitive information exposure.