🔧 Selenium Web Testing + GitHub Actions  
Python | Selenium | Pytest | CI  

---

### 📋 **Description**  
Automatización de pruebas web con Selenium y pytest, integrada en GitHub Actions para ejecutar tests en cada `push` o `pull request`.  

**🎯 Main Objective**:  
Validar el comportamiento de una página web (ej: GitHub) bajo condiciones controladas, asegurando que los elementos clave funcionen como se espera.  

---

### 🛠️ **Tech Stack**  
| Tool                | Purpose                                  |  
|---------------------|------------------------------------------|  
| 🐍 Python 3.12      | Lenguaje base para las pruebas           |  
| 🖥️ Selenium WebDriver | Automatización del navegador (Chrome)   |  
| 🧪 Pytest           | Framework de testing y reportes HTML/XML |  
| 🔄 GitHub Actions   | CI/CD para ejecución automática          |  

---

### 📁 **Project Structure**  
```plaintext
project-root/  
│  
├── 📂 tests/  
│   └── first_test.py           # Test de Selenium (ej: verifica título de GitHub)  
│  
├── 📂 .github/workflows/  
│   └── pytest.yml              # Workflow de GitHub Actions  
│  
├── requirements.txt            # Dependencias (pytest, selenium, pytest-html)  
└── README.md                  # Este archivo

🧪 How to Run Tests
🖥️ Localmente (con Chrome instalado):
bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest tests/ --html=report.html --self-contained-html

🔁 Via GitHub Actions
Cada push o PR dispara el workflow que:

⚙️ Configura Python 3.12 y Chrome.

🐍 Instala dependencias (pytest, selenium).

🚀 Ejecuta los tests en modo headless.

📦 Sube reportes (HTML + XML) como artefactos.

🔄 GitHub Actions Workflow
yaml
name: Run Pytest  
on: [push]  
jobs:  
  test:  
    runs-on: ubuntu-latest  
    steps:  
      - uses: actions/checkout@v4  
      - uses: actions/setup-python@v4  
      - uses: browser-actions/setup-chrome@latest  
      - run: pip install -r requirements.txt  
      - run: pytest --html=report.html --junitxml=results.xml  
      - uses: actions/upload-artifact@v4  
        with:  
          name: test-reports  
          path: |  
            report.html  
            results.xml

⚠️ Important Notes
ChromeDriver: Se instala automáticamente via selenium-manager (no requiere ruta hardcodeada).

Modo Headless: Essential para CI (sin interfaz gráfica).

Reportes:

HTML: Visualiza resultados en report.html.

XML: Integrable con herramientas como Jenkins.

📜 License
Educational project - Part of DevOps/QA training.
