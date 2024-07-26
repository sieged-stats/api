## Sieged - API

### Prerequesites

1. Docker ( https://docs.docker.com/engine/install/ )
2. Docker compose ( https://docs.docker.com/compose/ )
3. Make ( https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/ )

### Commands

- `make build` : build docker image
- `make up` : up containers
- `make down` : down containers
- `make shell` : shell into container
- `make logs` : attach logs to your terminal
- `make re` : éteins puis redémarre les conteneurs

### Local start

1. Create env

```env
UBISOFT_MAIL=<YOUR-UBISOFT-MAIL>
UBISOFT_PASSWORD=<YOUR-UBISOFT-PASSWORD>
MYSQL_ROOT_PASSWORD=<DATABASE-PASSWORD -- CHOOSE YOURS IN LOCAL>
```

2. `make build`
3. `make up`
4. `make logs`
5. http://localhost:3000/docs
