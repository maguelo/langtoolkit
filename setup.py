from setuptools import setup, find_packages

setup(
    name="langtoolkit",  # Nombre del paquete/distribución
    version="0.1",  # Versión del paquete
    packages=['langtoolkit', 'langtoolkit.lang'], #find_packages(),  # Encuentra paquetes automáticamente
    package_dir={'': 'src'},
    install_requires=[
        "unidecode",
        "spacy==3.6",
        "en_core_web_lg==3.6",
        "es_core_news_lg==3.6",
    ],
    # extras_require={
    #     "dev": [
    #         "unittest",
    #     ]
    # },
    # entry_points={
    #     "console_scripts": [
    #         "mi-comando = mi_paquete.modulo:funcion_principal",  # Ejemplo de comando CLI
    #     ],
    # },
    author="Miguel Maldonado",
    # author_email="tu.email@example.com",
    description="Tools for working with natural language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maguelo/langtoolkit",  # URL del repositorio o página del proyecto
    python_requires=">=3.9",  # Requerimiento de versión de Python
)