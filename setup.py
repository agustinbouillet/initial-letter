from distutils.core import setup

setup(
        name='initial_letter',
        version='1.0.0',
        py_modules=[
            'initialletter',
        ],
        data_files=[('demo',
                     [
                         'demo/test.py',
                         'demo/img/a.jpg',
                         'demo/gotham/Gotham-Bold.ttf',
                     ],
                     )],
        author='Agustin Bouillet',
        author_email='agustin.bouillet@gmail.com',
        url='http://www.bouillet.com.ar/',
        description='Letra inicial',
        # long_description = """Really long text here."""
)
