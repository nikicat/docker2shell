import setuptools

if __name__ == '__main__':
    setuptools.setup(
            name='docker2shell',
            version='0.1',
            url='https://github.com/nikicat/docker2shell',
            license='GPLv3',
            author='Nikolay Bryskin',
            author_email='devel.niks@gmail.com',
            description='tool to create shell invocation command for existing docker container',
            platforms='linux',
            packages=setuptools.find_packages(),
            entry_points={'console_scripts': ['docker2shell = docker2shell:main']},
            install_requires=['argh', 'argcomplete'],
    )
