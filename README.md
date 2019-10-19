# protobuf-alpine

[![GitHub Latest Tag](https://img.shields.io/github/v/tag/meMo-Minsk/protobuf-alpine?label=github+tag)](https://github.com/meMo-Minsk/protobuf-alpine)
[![Travis Build Status](https://img.shields.io/travis/meMo-Minsk/protobuf-alpine?label=travis+build)](https://travis-ci.org/meMo-Minsk/protobuf-alpine/builds)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/memominsk/protobuf-alpine)](https://hub.docker.com/r/memominsk/protobuf-alpine/builds)

## Usage

Using `docker run`:

```shell
# Create output dir
mkdir java_out
# Invoke protoc
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --java_out=/mnt/java_out /mnt/contract.proto
```

Using `protoc` alias:

```shell
# Define alias
alias protoc="docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest"
# Create output dir
mkdir java_out
# Invoke protoc
protoc --java_out=/mnt/java_out /mnt/contract.proto
```


### Generate C++ header and source

```bash
mkdir cpp_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --cpp_out=/mnt/cpp_out /mnt/contract.proto
`````

### Generate C# source file

```bash
mkdir csharp_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --csharp_out=/mnt/csharp_out /mnt/contract.proto
```

### Generate Java source file

```bash
mkdir java_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --java_out=/mnt/java_out /mnt/contract.proto
```

### Generate JavaScript source

```bash
mkdir js_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --js_out=/mnt/js_out /mnt/contract.proto
```

### Generate Objective C header and source

```bash
mkdir objc_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --objc_out=/mnt/objc_out /mnt/contract.proto
```

### Generate PHP source file

```bash
mkdir php_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --php_out=/mnt/php_out /mnt/contract.proto
```

### Generate Python source file

```bash
mkdir python_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --python_out=/mnt/python_out /mnt/contract.proto
```

### Generate Ruby source file

```bash
mkdir ruby_out
docker run --rm -v $(pwd):/mnt memominsk/protobuf-alpine:latest --ruby_out=/mnt/ruby_out /mnt/contract.proto
```
