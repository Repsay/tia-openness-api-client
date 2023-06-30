from setuptools import setup, find_packages

setup(
    name='tia-openness-api-client',
    version='0.1.0',
    author='Jasper Delahaije',
    author_email='jdelahaije@gmail.com',
    description='A Python library used to create a client for accessing the TIA Openness API',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Repsay/tia-openness-api-client',
    packages=find_packages(),
    install_requires=['pythonnet'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.11',
)
