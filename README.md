🚀 Pruebas Automatizadas con Selenium + GitHub Actions
Tecnologías: 🐍 Python 3.12 | 🖥️ Selenium WebDriver | 🧪 Pytest | 🔄 GitHub Actions

📋 Descripción
Solución de pruebas web automatizadas usando Selenium WebDriver con Python, integrada con GitHub Actions para ejecución continua en cada push o pull request.

Objetivos:
✅ Validar comportamiento de páginas web
📊 Generar reportes HTML/XML automáticos
🔁 Ejecutar pruebas en CI/CD

🛠 Configuración Rápida
Clonar repositorio:

bash
git clone https://github.com/tu-usuario/repo.git && cd repo
Instalar dependencias:

bash
pip install -r requirements.txt
Ejecutar pruebas localmente:

bash
pytest tests/ --html=report.html --self-contained-html
⚙️ GitHub Actions Workflow
El pipeline automático incluye:

yaml
name: Run Pytest
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: "3.12"
      - uses: browser-actions/setup-chrome@latest
      - run: pip install -r requirements.txt
      - run: pytest --html=report.html --junitxml=results.xml
      - uses: actions/upload-artifact@v4
        with:
          name: test-reports
          path: |
            report.html
            results.xml
📂 Estructura del Proyecto
text
.
├── tests/
│   └── test_github.py          # Prueba ejemplo (verifica título de GitHub)
├── .github/
│   └── workflows/
│       └── pytest.yml          # Configuración de CI
└── requirements.txt            # Dependencias (pytest, selenium, pytest-html)
📌 Mejores Prácticas
Usa fixtures de pytest para gestionar el navegador

Implementa el Patrón Page Object Model

Genera reportes con pytest-html

Ejecuta en modo headless para CI

📜 Licencia
Proyecto educativo - Parte de formación en QA Automation.

✉️ Contacto: tu-email@ejemplo.com
🔗 Repositorio: github.com/tu-usuario/repo

https://selenium.dev/images/selenium_logo_square_green.png
