from distutils.core import setup
setup(
    name='gangagsoc',
    packages=['gangagsoc'],
    version='v2022',
    license='gpl-3.0',
    description='The Challenge for GSoC 2022 student to particpate in the Ganga project',
    author='Ulrik Egede',
    author_email='ulrik.egede@monash.edu',
    url='https://github.com/ganga-devs/GangaGSoC2022',
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
