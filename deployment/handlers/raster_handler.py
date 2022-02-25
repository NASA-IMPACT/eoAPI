"""AWS Lambda handler."""

import logging
import os

from mangum import Mangum

from eoapi.raster.app import app

os.environ["AWS_SECRET_ACCESS_KEY"] = os.environ["SECRET_ACCESS_KEY"]
os.environ["AWS_ACCESS_KEY_ID"] = os.environ["ACCESS_KEY_ID"]
os.environ["AWS_SESSION_TOKEN"] = os.environ["SESSION_TOKEN"]

logging.getLogger("mangum.lifespan").setLevel(logging.ERROR)
logging.getLogger("mangum.http").setLevel(logging.ERROR)

handler = Mangum(app, lifespan="auto", log_level="error")
