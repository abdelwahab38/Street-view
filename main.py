import streamlit as st
from streamlit_pannellum import streamlit_pannellum
import os
import subprocess

# Démarrer le serveur HTTP pour les fichiers statiques
server_script = os.path.join(os.path.dirname(__file__), 'serving_images.py')
subprocess.Popen(["python", server_script])

# URLs des images servies
image_0001_url = "http://localhost:8000/image_0001.jpg"
image_0002_url = "http://localhost:8000/image_0002.jpg"

# Assurez-vous que les URLs des images sont correctes
if not image_0001_url or not image_0002_url:
    st.error("Les URLs des images ne sont pas correctes.")
else:
    # Configuration de Pannellum
    streamlit_pannellum(
        config={
            "default": {
                "firstScene": "first",
            },
            "scenes": {
                "first": {
                    "title": "My first example",
                    "type": "equirectangular",
                    "panorama": image_0001_url,
                    "autoLoad": True,
                    "author": "Me",
                    "hotSpots": [
                        {
                            "pitch": 15,
                            "yaw": 0,
                            "type": "info",
                            "text": "This is an info."
                        },
                        {
                            "pitch": 0,
                            "yaw": -10,
                            "type": "scene",
                            "text": "Second scene",
                            "sceneId": "second"
                        }
                    ],
                },
                "second": {
                    "title": "My second example",
                    "type": "equirectangular",
                    "panorama": image_0002_url,
                    "autoLoad": True,
                    "author": "always Me",
                    "hotSpots": [
                        {
                            "pitch": 15,
                            "yaw": 0,
                            "type": "info",
                            "text": "This is an info."
                        },
                        {
                            "pitch": 0,
                            "yaw": -10,
                            "type": "scene",
                            "text": "First scene",
                            "sceneId": "first"
                        }
                    ],
                }
            }
        }
    )
