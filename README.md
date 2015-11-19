# github-release

A helper tool for creating GitHub releases

## Example: Hooking the releases to CircleCI

Let's assume your CI build process creates release artifacts right to the ```$CIRCLE_ARTIFACTS``` directory. Add this to your ```circle.yml``` file to create a new GitHub release for every new master branch version:

```
deployment:
  release:
    branch: master
    commands:
      - python release.py $GITHUB_API_TOKEN $CIRCLE_PROJECT_USERNAME $CIRCLE_PROJECT_REPONAME $CIRCLE_ARTIFACTS/*
```

In this example we assume that the environment variable ```GITHUB_API_TOKEN``` contains a GitHub API token suitable for creating releases. The required scope depends on whether you release to a public or a private repository: **public_repo** for public, **repo** for private.
