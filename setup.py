from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_bowern2021australia',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_bowern2021australia'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'bowern2021australia=cldfbench_bowern2021australia:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
        'kml2geojson',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
