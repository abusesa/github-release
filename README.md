# github-release

A helper tool for creating GitHub releases

## Example: Hooking the releases to CircleCI

First you need to install the ```github-release``` tool to your CI environment. For example you can add the following to the ```dependencies``` section of your ```circle.yml``` file:

```
dependencies:
  pre:
    - pip install https://github.com/abusesa/github-release/archive/master.tar.gz
```

Let's assume your CI build process creates release artifacts right to the ```$CIRCLE_ARTIFACTS``` directory. Modify ```circle.yml``` to create a new GitHub release for every new tag matching ```/\d+(\.\d+)*/```:

```
deployment:
  build:
    tag: /\d+(\.\d+)*/
    commands:
      - github-release $GITHUB_API_TOKEN $CIRCLE_PROJECT_USERNAME $CIRCLE_PROJECT_REPONAME $CIRCLE_TAG $CIRCLE_ARTIFACTS/*
```

In this example we assume that the environment variable ```GITHUB_API_TOKEN``` contains a GitHub API token suitable for creating releases. The required scope depends on whether you release to a public or a private repository: **public_repo** for public, **repo** for private.

A GitHub user has to have at least **write** level access to the repository to be able to create and edit releases.
