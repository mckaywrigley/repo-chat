#!/bin/sh

# Execute the load.py and embed.py scripts
python load.py
python embed.py

# Run the gotty command with the main application
exec gotty --port 3000 --permit-write --title-format "Repo Chat Terminal" python main.py
