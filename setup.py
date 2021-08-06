from setuptools import setup


name = 'zipdump'
version = '0.3'


setup(name=name,
    version=version,
    url='https://github.com/nlitsme/zipdump',
    author='Willem Hengeveld',
    author_email='itsme@xs4all.nl',
    description='Analyze zipfile, either local, or from url',
    classifiers=[
        "Programming Language :: Python",
    ],
    py_modules = [ 'urlstream', 'zipdump', 'webdump' ],
    zip_safe=False,
    entry_points="""
        [console_scripts]
        zipdump = zipdump:main
        webdump = webdump:main
    """,
)
