# protobuf-alpine

[![GitHub Latest Tag](https://img.shields.io/github/v/tag/meMo-Minsk/protobuf-alpine?label=github+tag)](https://github.com/meMo-Minsk/protobuf-alpine)
[![Travis Build Status](https://img.shields.io/travis/meMo-Minsk/protobuf-alpine?label=travis+build)](https://travis-ci.org/meMo-Minsk/protobuf-alpine/builds)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/memominsk/protobuf-alpine)](https://hub.docker.com/r/memominsk/protobuf-alpine/builds)

```shell
docker pull memominsk/protobuf-alpine:latest
```

```shell
docker run --rm -v $PWD:/mnt memominsk/protobuf-alpine:latest \
    -I=/mnt --java_out=/mnt/java /mnt/example.proto
```
