import os

os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"

from Todo import app

import seed


if __name__ == '__main__':

    app.run()