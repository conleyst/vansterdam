# Vansterdam

Adventures in moving from Vancouver to Amsterdam.

## Development

Start the application locally using,

```
docker compose up
```

The site should be accessible at `http://localhost:5000`.

### Running Migrations

Migrations are managed using the [`flask-migrate`](https://github.com/miguelgrinberg/Flask-Migrate) extension. Migrations are stored in the `migrations` directory. To automatically update migrations to reflect existing models, run,

```
flask db migrate -m "A brief, informative description"
```

Note that this only adds the migration to the previously mentioned directory. To run migrations, use,

```
flask db upgrade
```
