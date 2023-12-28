# Strava plotter webapp

This webapp uses https://github.com/ndoornekamp/strava-plotter to plot your personal Strava data with satellite images as background.

## Running the app locally

1. Clone the strava-plotter inside strava-plotter-webapp: `git clone https://github.com/ndoornekamp/strava-plotter.git`
2. Follow section B of [Strava's instructions for creating an app](https://developers.strava.com/docs/getting-started/).
3. Rename '.env.example' to '.env' and fill the CLIENT_ID, CLIENT_SECRET you obtained in the previous steps.
4. Create a conda env with the required dependencies by running `conda env create -f environment.yml`
5. Start the Django server by running`python3 manage.py runserver`
