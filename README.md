# Práctica Final DevOps - CI/CD Automatizado

Este proyecto implementa un flujo completo de Integración Continua y Despliegue Continuo (CI/CD) para una aplicación web desarrollada en Python con Flask.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.11 + Flask
* **Testing:** Pytest
* **Contenedores:** Docker
* **Registro:** Docker Hub
* **Orquestación CI/CD:** GitHub Actions
* **Despliegue Cloud:** Render

## 🔄 Flujo del Pipeline CI/CD

Cada vez que se hace un `git push` a la rama `main`:
1. **GitHub Actions** descarta errores probando el código con **Pytest**.
2. Si las pruebas pasan, construye la imagen de Docker.
3. Publica la imagen automáticamente en **Docker Hub**.
4. Notifica a **Render** mediante Deploy Hook para actualizar el servicio en producción.

---

### Repositorio

https://github.com/MaxwellAybar/PracticaFinalDevops-Maxwell-Aybar

### Aplicación en producción

https://practica-devops-maxwell.onrender.com
