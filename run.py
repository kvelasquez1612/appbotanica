import sys
import os
import uvicorn

# Obtenemos la ruta absoluta de la carpeta actual y aseguramos que la subcarpeta interna esté en el path
current_dir = os.path.dirname(os.path.abspath(__file__))
sub_project_dir = os.path.join(current_dir, "appbotanica-main")

if os.path.exists(sub_project_dir):
    sys.path.append(sub_project_dir)
else:
    sys.path.append(current_dir)

from app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)