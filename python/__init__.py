
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="production") # use "production" on a remote server
