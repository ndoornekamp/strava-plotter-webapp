This webapp uses https://github.com/ndoornekamp/strava-plotter to plot your personal Strava data with satellite images as background. 

# Local development
1. If you haven't done so when cloning the main project, clone the strava-plotter submodule:
    `git submodule init`
    `git submodule update`
2. Create a conda env with the required dependencies by running `conda env create -f environment.yml`
3. Start the Django server by running`python3 manage.py runserver`