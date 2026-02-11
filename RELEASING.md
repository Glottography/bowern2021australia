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
489     valid features
426     valid speaker areas
```

```shell
cldfbench geojson.glottolog_distance cldf --glottolog-version v5.2 --format tsv | csvformat -t | csvgrep -c Distance -r"^0\.?" -i | csvsort -c Distance | csvcut -c ID,Distance | csvformat -E | termgraph
```

```
bula1255: ▇▇▇▇▇▇▇▇▇▇▇▇ 1.05 
kala1379: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.13 
wang1288: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.24 
anda1282: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.29 
pint1250: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.32 
yard1234: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1.47 
lowe1403: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 2.21 
ayer1246: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 4.00 
kung1258: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 4.08 
```


## Release

Commit and push all changes.

Run
```
cldfbench glottography.release cldfbench_bowern2021australia.py vX.Y
```
and follow the instructions given in the output of the command.
