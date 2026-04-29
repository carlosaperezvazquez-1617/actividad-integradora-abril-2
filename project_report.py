import os

files = {
    "Dockerfile app": "app/Dockerfile",
    "Dockerfile helper": "helper/Dockerfile",
    "docker-compose.yml": "docker-compose.yml",
    "README.md": "README.md",
    "Plantilla CloudFormation": "infraestructura-base.yaml"
}

print("--- Reporte del Entorno ---")
all_found = True
for name, path in files.items():
    exists = os.path.exists(path)
    print(f"{name}: {'Encontrado' if exists else 'No encontrado'}")
    if not exists: all_found = False

status = "Listo para validación" if all_found else "Incompleto"
print(f"Estado general: {status}")