
# Data Visualisation Site

This is a sample site built using Django to read and siplay data charts. The site is has 2 differnt ways of functioning.

1. Standard Django site with a SQLite database with average house prices in the UK and a charting feature to visualize the data. The following frameworks and libraries were used: Django, BootStrap, crispy-forms and Plotly.

2. Metabase site. The build script will deploy Metabase along with the Django app and can be accessed at http://localhost:3000 there are additional steps located below to setup the Metabase platform.

## Features

- Visualize data using Plotly
- User authentication

## Installation

Download and run the build script  

For Windows:

```bash
.\build.ps1
```

For MacOS/Linux:

```bash
.\build.sh
```

The default development server IP should be http://127.0.0.1:8000/



## Django:
Once build script has succesfully run, go to http://localhost:8000 to view the project.

## Metabase
Once build script has succesfully run, go to http://localhost:3000 to launch Metabase.

Once the platform opens, follow the registration process. When asked to link a database select SQLite. Give it a name and the filename path of /metabase-data/db.sqlite3

You can then start experimenting
