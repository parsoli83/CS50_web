# git
it is a really good thing :)

## main git commands

### clone
```
git clone <url>.git
```
to download a git repository onto your system

### commit

```
git add .
git commit -m "text"
git push
```

**git add** says you want to save the changes to the following thing
**git commit** makes the commit on your local repository
**git push** uploads the changes

```
git commit -am "text"
```
this adds all and commits at the same time

### pull
```
git pull
```
gets the latest state of the repository (updates and synchronizes local)

### log
```
git log
```
gives the data on all commits

### reset
```
git reset --hard <commit-hash>
git reset --hard origin/master
```
revert back to an older version of the repository
by providing the commit hash

## Branching
gits way to work on different parts of the repository at the same time
```
git checkout -b <branch-name>
```
makes a new branch and changes to it

```
git checkout <branch-name>
```
swiches branch to an existing one

```
git merge <branch-name>
```
merges the branch with main

## GitHub Features
### Forking
Fork and then send a pull request
### GitHub Pages

make a repository named like "parsoli.github.io"
then the repository will be hosted by github for you!!
