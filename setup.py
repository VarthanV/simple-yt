from distutils.core import setup
from setuptools import setup,setuptools
import os 
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    readme = readme_file.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='simpleyt',
    version='1.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    long_description_content_type= 'text/markdown',
    long_description=open('README.md').read(),
    description = "A Simple Wrapper for Yotube Data Api v3 for Python which helps querying the public Youtube Data in a hassle free way",
    author = "Vishnu Varthan Rao",
    author_email="vishnulatha006@gmail.com",
    url='https://github.com/VarthanV/simple-yt',
    install_requires=[
        "requests",
        "isodate"
    ],
    license="MIT License",
    zip_safe=False,
    keywords='youtube,youtubeapi,youtube data,youtubevideo,youtube playlists, youtube channel, python youtube ,youtube,ytd',
     classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],

)