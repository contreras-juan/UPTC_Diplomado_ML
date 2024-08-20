# Template Proyecto en Ciencia de Datos

By: autor_del_proyecto

Descripción del proyecto: plantilla para proyectos de ciencia de datos.

## License

Especificar el tipo de licencia del proyecto.

## Prerrequisitos

- [Anaconda](https://www.anaconda.com/download/) >=4.x

## Creación de Ambiente virtual

```bash
conda env create -f environment.yml
activate mi_entorno_virtual_ds
```
or 

```bash
mamba env create -f environment.yml
activate mi_entorno_virtual_ds
```

## Organización del Proyecto

    palntilla_ciencia_de_datos
        ├── data
        │   ├── processed      <- Forma final de los datos procesados.
        │   └── raw            <- Data original sin procesar.
        │
        ├── notebooks          <- Jupyter notebooks. Se recomienda que cada notebook tenga el nombre del 
        |                         proceso que representa, por ejemplo 'eda_data_cleaning.ipynb', 
        |                         'ml_modeling.ipynb'.
        │                         
        │                       
        ├── envs               <- Ubiación del ambiente virtual.
        ├── models             <- Locación de los modelos entrenados exportados.
        │
        ├── .gitignore         <- Archivos a ignorar por `git`.
        │
        ├── environment.yml    <- Requerimientos para reproducir el actual proyecto, ambiente virtual.
        │
        └── README.md          <- Top-level README para developers.


