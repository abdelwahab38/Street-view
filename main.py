from streamlit_pannellum import streamlit_pannellum

streamlit_pannellum(
    config={
      "default": {
        "firstScene": "first",
      },
      "scenes": {
        "first": {
          "title": "My first example",
          "type": "equirectangular",
          "panorama": "https://pannellum.org/images/alma.jpg",
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
          "panorama": "/mount/src/street-view/static/alma.jpg",
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
