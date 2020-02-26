from distutils.core import setup
setup(
    name='gangagsoc',
    packages=['gangagsoc'],
    version='1.0',
    license='gpl-3.0',
    description='The Challenge for GSoC 2020 student to particpate in the Ganga project',
    author='Ulrik Egede',
    author_email='ulrik.egede@monash.edu',
    url='https://github.com/ganga-devs/GangaGSoC2020',
    keywords=['GSoC', 'Ganga', 'Challenge'],
    install_requires=[
          'pytest',
          'ganga',
      ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
