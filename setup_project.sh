#!/bin/bash
echo "Iniciando preparación del entorno..."
sudo apt-get update
echo "Instalando dependencias: Git, Python3, Docker..."
sudo apt-get install -y git python3 docker.io
echo "Creando estructura de directorios..."
mkdir -p app helper .github/workflows
echo "Entorno configurado con éxito."
