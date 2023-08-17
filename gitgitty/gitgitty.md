# gitgitty
## Source Code
https://github.com/yuujin-Q/gitgitty

## Video Demo
https://youtu.be/UFVhsYO08sY

## Implementation
Gitgitty is implemented using Python. For version control, gitgitty uses snapshots for a simpler implementation at the cost of storage.

When a repository is created, a folder `.gitgitty` is created with the following structure
```
.gitgitty
└───snapshots/
    └───0
    └───1
    └───2
    └───...
└───latest
└───log
└───head
```
Version ID is numbered starting from 0. `latest` is used to track latest commit version ID. `log` tracks commit logs (including version ID, date, time, and message). `head` is used to track current checkout ID.

## Commands
Available commands are as follows
```
usage: gitgitty <command> [<args>]
available commands:
     init                    create an empty gitgitty repository
     commit [-m <msg>]       record snapshot to the repository
     log                     show commit logs
     checkout <version-id>   change version head
```

`gitgitty` is substituted using `python <gitgitty.py path>` or using compiled binary PATH