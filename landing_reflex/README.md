# Landing Page con Reflex

## Descripción

Este proyecto consiste en la recreación de una landing page profesional utilizando **Reflex**, **Python 3.12**, **Poetry**, **Git** y **GitHub**.

El objetivo fue aplicar conocimientos de desarrollo frontend, estructura visual, componentes reutilizables y buenas prácticas de organización del código.

---

# Tecnologías utilizadas

- Python 3.12
- Reflex
- Poetry
- Git
- GitHub
- HTML/CSS mediante componentes de Reflex

---

# Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- Python 3.12
- Poetry
- Git

---

# Verificar instalación de Python

```bash
python --version
```

Resultado esperado:

```text
Python 3.12.x
```

---

# Verificar instalación de Poetry

```bash
poetry --version
```

---

# Pasos para clonar y ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/Julioblack09/landing-reflex.git
```

---

## 2. Entrar a la carpeta del proyecto

```bash
cd landing-reflex
```

---

## 3. Instalar dependencias con Poetry

```bash
poetry install
```

---

## 4. Ejecutar la aplicación

```bash
poetry run reflex run
```

---

## 5. Abrir el navegador

Abrir la siguiente URL:

```text
http://localhost:3000
```

---

# Pasos realizados para crear el proyecto

## 1. Creación de la carpeta del proyecto

```bash
mkdir landing-reflex
cd landing-reflex
```

---

## 2. Inicialización del repositorio Git

```bash
git init
```

---

## 3. Inicialización del proyecto con Poetry

```bash
poetry init -n
```

---

## 4. Configuración de Python compatible

En el archivo `pyproject.toml` se configuró:

```toml
requires-python = ">=3.12,<4.0"
```

---

## 5. Instalación de Reflex

```bash
poetry add reflex==0.9.2
```

---

## 6. Inicialización de Reflex

```bash
poetry run reflex init
```

---

## 7. Ejecución del servidor local

```bash
poetry run reflex run
```

---

# Desarrollo de la Landing Page

La estructura principal se desarrolló en el archivo:

```text
landing_reflex/landing_reflex.py
```

La landing page contiene las siguientes secciones:

- Barra de navegación
- Hero principal
- Sección de estadísticas
- Sección profesional
- Work Process
- Portfolio
- Diseño responsive
- Uso de imágenes externas

---

# Uso de imágenes

Las imágenes fueron almacenadas dentro de la carpeta:

```text
assets/
```

Archivos utilizados:

```text
assets/brooklyn_photo.jpg
assets/portfolio1.jpg
assets/portfolio2.jpg
assets/portfolio3.jpg
```

---

# Estructura del proyecto

```text
landing-reflex/
│
├── assets/
│   ├── brooklyn_photo.jpg
│   ├── portfolio1.jpg
│   ├── portfolio2.jpg
│   └── portfolio3.jpg
│
├── landing_reflex/
│   ├── __init__.py
│   └── landing_reflex.py
│
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
└── rxconfig.py
```

---

# Comandos Git utilizados

## Agregar archivos

```bash
git add .
```

---

## Crear commit

```bash
git commit -m "Landing page replica completed with Reflex"
```

---

## Configurar rama principal

```bash
git branch -M main
```

---

## Conectar con GitHub

```bash
git remote add origin https://github.com/Julioblack09/landing-reflex.git
```

---

## Subir proyecto a GitHub

```bash
git push -u origin main
```

---

# Ejecución completa del proyecto

```bash
git clone https://github.com/Julioblack09/landing-reflex.git

cd landing-reflex

poetry install

poetry run reflex run
```

---

# URL del proyecto

Repositorio oficial:

```text
https://github.com/Julioblack09/landing-reflex
```

---

# Autor

## Julio Cruz

Proyecto desarrollado utilizando Reflex y Python 3.12.