import streamlit as st
from streamlit_pannellum import streamlit_pannellum

image_0001_url = "static/image_0001.jpg"
image_0002_url = "static/image_0002.jpg"

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
