import distutils.version

import pystache
import requests
import sarge

GLIBC_REPO = 'sgerrand/alpine-pkg-glibc'
PROTOBUF_REPO = 'protocolbuffers/protobuf'
VERSION_FILE = '.version'


def main():
    glibc_version = get_latest_github_release(GLIBC_REPO)
    print('glibc_version =', glibc_version)

    protoc_versions = get_github_releases(PROTOBUF_REPO)
    print('protoc_versions =', protoc_versions)
    latest_release = get_latest_release()
    print('latest_release =', latest_release)
    protoc_version = get_next_release(protoc_versions, latest_release)
    print('protoc_version =', protoc_version)

    if not protoc_version:
        print('Already up to date.')
        return

    do_release(glibc_version, protoc_version)
    run(f'git add {VERSION_FILE} Dockerfile')
    run(f'git commit -m "{protoc_version}"')
    run('git push')
    run(f'git tag {protoc_version}')
    run('git push --tags')


def get_latest_github_release(repo):
    with requests.Session() as session:
        url = f'https://api.github.com/repos/{repo}/releases/latest'
        response = session.get(url)
        return response.json()['tag_name']


def get_github_releases(repo):
    with requests.Session() as session:
        next_url = f'https://api.github.com/repos/{repo}/releases'
        json = []
        while next_url:
            response = session.get(next_url)
            next_url = response.links['next']['url'] if 'next' in response.links else None
            json += response.json()
        return sorted(list(map(
            lambda release: release['tag_name'][1:],
            filter(
                lambda release: not release['draft'] and not release['prerelease'],
                json))), key=distutils.version.LooseVersion, reverse=True)


def get_latest_release():
    with open(VERSION_FILE, mode='r') as file:
        return file.readline()


def get_next_release(github_releases, latest_release):
    for index, release in enumerate(github_releases):
        if latest_release == release and index > 0:
            return github_releases[index - 1]


def do_release(glibc_version, protoc_version):
    with open(VERSION_FILE, mode='w') as file:
        file.write(protoc_version)
    with open('Dockerfile.mustache', mode='r') as template:
        with open('Dockerfile', mode='w') as result:
            result.write(pystache.render(template.read(), {
                'glibc_version': glibc_version,
                'protoc_version': protoc_version
            }))


def run(command):
    print(f'$ {command}')
    pipeline = sarge.run(command)
    if pipeline.returncode != 0:
        exit(pipeline.returncode)


if __name__ == '__main__':
    main()
