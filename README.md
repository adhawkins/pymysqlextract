# pysqlextract

A python script to extract individual tables from a MySQL dump file.

> usage: pymysqlextract.py [-h] [--tables table [table ...]] [--exclude]
>                          mysqldumpfile
>
> Extract some tables from a MySQL database dump file into individual files
>
> positional arguments:
>   mysqldumpfile         The MySQL dump file to be used as input
>
> optional arguments:
>   -h, --help            show this help message and exit
>   --tables table [table ...], -t table [table ...]
>                         Tables to include or exclude (if none specified, will
>                         include all tables)
>   --exclude, -x         If specified, the list of tables will be treated as an
>                         include list, rather than an exclude list
