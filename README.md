## Deploying with Dokku

On the server:

````bash
dokku apps:create py-discord
dokku builder:set py-discord selected herokuish
dokku config:set py-discord DISCORD_TOKEN=$TOKEN DISCORD_GUILD="Coffee's server"```
dokku config:set py-discord SEPARATION_SYMBOL=?
````

From the repo:

```bash
git remote add dokku dokku@$SERVER:py-discord
git push dokku master
```
