
import os

class Agent:
    def __init__(self):
        pass

    def setup_tools(self):
        self.setup_tools = [
            {
                "type": "function",
                "name": "list_files_in_dir",
                "description": "Lista los archivos que existen en un directorio dado.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "directory": {
                            "type": "string",
                            "description": "Directorio en el que se van a buscar los archivos."
                        }
                    },
                    "required": ["directory"]
                }
            }
        ]