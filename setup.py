from pathlib import Path
from setuptools import setup
from os import path
base_dir = path.abspath(path.dirname(__file__))
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='TMFrame',
    packages=['TMFrame'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1',
    license='MIT',
    description='Music Thumbnail Maker',
    author='Krypton Byte',
    author_email='galaxyvplus6434@gmail.com',
    url='https://github.com/krypton-byte/MFrame',
    keywords=['Thumbnail', 'Music', 'Maker'],
    install_requires=[
            'pillow',
        ],
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
    ],
)
