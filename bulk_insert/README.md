# Bulk Ingest sample


## Starting the environment


Install Task

`brew install go-task/tap/go-task`

To bring up the environment do:

```sh
task db-up
```

To bring down the environment do:

```sh
task db-down
```

To shell into the database

```sh
psql -h localhost -U postgres
```
