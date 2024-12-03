import sys
import os

# Ensure the project root is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Bot.main import app

if __name__ == "__main__":
    app.run()
