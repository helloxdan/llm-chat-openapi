from setuptools import setup, find_packages

setup(
    name='llm-chat-openapi',
    version='1.0.6',
    packages=find_packages(),
    author='helloxdan',
    author_email='hello.xdan@gmail.com',
    description='chat api  collection for popular LLM',
    long_description='chat api  collection for popular LLM',
    long_description_content_type='text/markdown',
    url='https://github.com/helloxdan/llm-chat-openapi',
    install_requires=[
        # List of dependencies
		'flask>=2.0.2',
		'flask-cors>=4.0.0',
		'openai>0.19.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
