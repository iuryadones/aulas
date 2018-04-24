# Git

## git log

 - git log
 - git log --online --decorate --graph --color
 - git log --online --decorate --all --graph --color
 - git log --stat

## git status

 - git status
 - git status --column=auto
 - git status --untracked-files=all --column=auto

## ~/.gitconfig

```
[user]
    name = First_name Family_name
    email = user@host.com
[core]
    editor = nvim
    excludesfile = ~/.gitignore-global
[alias]
    log-graph = log --decorate --oneline --graph --color
    log-all = log --decorate --oneline --graph --all --color
    status-column = status --untracked-files=all --column=auto
[merge]
    tool = vimdiff
```

## ~/.gitignore-global

```
# pyenv
.python-version

# python
*.py[cod]
```
