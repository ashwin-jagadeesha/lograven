from setuptools import setup, find_packages

setup(
    name='lograven',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tiktoken',
        'transformers',
        'nltk',
        'scikit-learn',
        'rich',
    ],
    author='Your Name',
    description='Modular log analyzer with pluggable chunkers and LLM-optional summarization',
    license='MIT',
    keywords='logs LLM chunking summarization tokenizer NLP',
)
