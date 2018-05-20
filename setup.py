from distutils.core import setup

setup(
    name='flarmnet',
    version='0.1.2',
    author='Tobias Bieniek',
    author_email='Tobias.Bieniek@gmx.de',
    url='https://github.com/Turbo87/flarmnet.py',
    description='FlarmNet data file reader for python',
    keywords=['flarm', 'flarmnet', 'butterfly'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['flarmnet'],
    scripts=['scripts/flarmnet-lookup'],
)
