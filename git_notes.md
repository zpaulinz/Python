# Git Notes

## Check the installed Git version
```
git --version 
```

## Download Git - Windows, macOS
https://git-scm.com


## Install Git - Linux
```
sudo apt install git
```

## Git configuration
```
git config --global user.name "nazwa_użytkownika"
git config --global user.email "użytkownik@example.com"
git config --global init.defaultBranch main
```

## Ignoring files
To make Git ignore .pyc files and the __pycache__ directory, add the following entry to the .gitignore file:

__pycache__/

On macOS, it's also recommended to add .DS_Store. If needed, enable the display of hidden files in your system.


## Initializing a repository
create folder, create .gitignore file
```
git init
```

## Check status
```
git status
```

## Adding files to a repository
```
git add hello.html

git add .
```

## Committing files
```
git commit -m "Start a project"
```

## Checking project log
```
git log
git log --pretty=oneline
```

## Second commit
```
git commit -am "Rozbudowa powitania."
```

## Restoring the project to a previous state
```
git restore .
```
or
```
git restore file_name
```

## Restoring the project to the previous state
```
git log --pretty=oneline
```
945fa13af128a266d0114eebb7a3276f7d58ecd2 (HEAD -> main) Rozbudowa powitania.

cea13ddc51b885d05a410201a54faf20e0d2e246 Rozpoczęcie projektu.
```
git checkout cea13d
```
Note: checking out 'cea13d'.
```
git switch -
```

## Deleting a repository
```
rm -rf .git
```

