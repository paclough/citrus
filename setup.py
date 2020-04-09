from setuptools import setup

setup(
    name='citrus',
    version='0.0.1',
    packages=['citrus'],
    url='http://github.com/mrmiguez/citrus',
    license='MIT',
    author='Matthew Miguez',
    author_email='r.m.miguez@gmail.com',
    description='Collective Information Transformation and Reconciliation Utility Service',
    long_description=open('README.rst').read() + '\n\n' +
    open('CHANGES.rst').read(),
    platforms='any',
    install_requires=[
        'pymods>=2.0.6',
        'sickle>=0.6.5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Text Processing :: Markup :: XML',
    ],
    test_suite='citrus.tests',
    keywords='oai-pmh metadata digital-libraries',
)