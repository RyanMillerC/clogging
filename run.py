import clogging
from app.App import App

log = clogging.start_from_yaml("conf/settings.yaml")
log.info("This is an info message")

c = App("Hello World!")
