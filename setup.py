from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Muhammad-Rehan-Ali',
    author_email='rehan5073@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)