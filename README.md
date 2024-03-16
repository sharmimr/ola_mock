The backend file has the details to Django and sqlite integration. API definition, etc.
The frontend code has the React JS code - UI.

proxy in package.json file to the UI code to integrate with backend code and the CORS_ALLOWED_ORIGINS in settings.py in the backend helps to resolve CORS.

Front End: (http://localhost:3000)
npm install
npm start
Back End: (http://localhost:8000)
python manage.py runserver.

This will start both the server and UI. Then the application will run
