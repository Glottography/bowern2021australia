# Releasing the dataset

## Recreate the data extracted from the source

```shell
cldfbench download cldfbench_bowern2021australia.py
```

## Recreate the CLDF dataset

```shell
cldfbench makecldf cldfbench_bowern2021australia.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_bowern2021australia.py
cldfbench zenodo --communities glottography cldfbench_bowern2021australia.py
cldfbench readme cldfbench_bowern2021australia.py
```


## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --glottolog-version v5.2 --format tsv | csvformat -t | csvgrep -c Distance -r"^0\.?" -i | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```

```
bula1255: ▇▇▇▇▇▇▇▇▇▇▇▇ 1.05 
kala1379: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.13 
pint1250: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.32 
lowe1403: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.21 
kung1258: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 4.08 
```