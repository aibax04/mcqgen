from  setuptools import find_packages,setup

setup (
    name='mcqgenerator' ,
    version='0.0.1' ,
    author='aibax04' ,
    author_email='aibax04@gmail.com',
    install_requires=["openai","langchain","streamlit","pyhton-dotenv","pyPDF2"],
    packages=find_packages()
    
)