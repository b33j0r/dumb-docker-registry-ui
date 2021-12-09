# `dumb-docker-registry-ui`

I was setting up a throw-away docker registry in my homelab one night. On this particular occasion, I couldn't get the most popular solutions to work right away, though the docker registry API was working fine. 

Figuring it'd be quicker, I made a dumb flask app to hit the API and render the result to a template. Then it turned out to be kinda fun, so I styled it.

<img src="docs/screenshots/2021-12-08-001.png?raw=true" width=50%>

For local/dev use only. No emphasis on security or features at this time. It's just a way to browse the API, assuming you can already. And limited browsing, at that.

Dumb and mildly-useful fun!

## Config

```yaml
---
# ./config/dumb.yml
registry:
  name: registry.local
  url: http://registry.local:5000
  version: v2
```

Inside the container, the app will search for the `dumb.yml` file at `/config/dumb.yml`. The provided `docker-compose.yml` looks for it in the project root `config` dir, which you can obviously adjust for your needs: 

```yaml
# docker-compose.yml (excerpt)
volumes:
  - "./config/dumb.yml:/config/dumb.yml:ro"
```

## Run

```shell
docker-compose up -d
```

## License

Created by [Brian Jorgensen](https://github.com/b33j0r) for himself; shared with you under the MIT license. All yours!
