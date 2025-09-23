import pathlib
import subprocess
import collections

from csvw.dsv import UnicodeWriter
from clldutils.jsonlib import dump
from cldfgeojson.create import feature_collection
import pyglottography

BASE_URL = "https://zenodo.org/record/4898185/files/"
FILES = [
    'AustralianPolygons.kml',
]
URL = 'https://zenodo.org/records/4898185/files/AustralianPolygons.kml?download=1'


class Dataset(pyglottography.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bowern2021australia"

    def cmd_download(self, args):
        """
        Convert the raw data from the Zenodo deposit into the two essential files expected for
        Glottography datasets:
        - `etc/features.csv`
        - `raw/dataset,geojson`
        """
        #self.raw_dir.download(URL, self.raw_dir / 'AustralianPolygons.kml')
        #subprocess.check_call(['k2g', str(self.raw_dir / 'AustralianPolygons.kml'), str(self.raw_dir)])
        #return

        langs = {l['Name']: l for l in self.etc_dir.read_csv('languages.csv', dicts=True)}
        fields = collections.Counter()
        md, features = [], []
        for i, f in enumerate(self.raw_dir.read_json('AustralianPolygons.geojson')['features']):
            props = f['properties']
            for a in {'styleUrl', 'path', 'auxiliary_storage_labeling_show'}:
                if a in props:
                    del props[a]
            if props.get('Family') == 'NonPny':
                props['Family'] = 'NonPNy'
            props['id'] = props.pop('fid')
            lg = langs[props['name']]
            props['glottocode'] = lg['Glottocode']
            props['year'] = 'traditional'
            props['map_name_full'] = 'Files for Australian Language Locations'
            md.append(props)
            fields.update(props.keys())
            f['properties'] = props
            features.append(f)
        cols = [k for k, _ in fields.most_common()]

        with UnicodeWriter('etc/features.csv') as w:
            w.writerow(cols)
            for d in md:
                w.writerow([d.get(col, '') for col in cols])
        dump(feature_collection(features), self.raw_dir / 'dataset.geojson')
