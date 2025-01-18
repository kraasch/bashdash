
# bashdash

My dashboard collection for bash.

## to-do

 - [ ] make dashboard for tasks and system info.
   - [X] display current month.
   - [X] display to-do list (from markdown wiki)
   - [X] display meteorological data.
   - [X] run git-walker (git repo scan).
   - [X] run hub-walker (install script scan).
   - [X] display astronomical data.
   - [ ] run watchcat (directory validator).
 - [ ] make dashboard for calendar.
   - [ ] display 3 month calendar (showing holidays).
   - [ ] display 3 weeks calendar (showing tasks).
 - [ ] make dashboard for finances.
   - [ ] run check monthly budget (eg ledger-cli).
 - ideas.
   - [ ] maybe use tmuxifier or tumuxify to manage sessions instead of bashdash.

## info on sampler

Depends on sampler (the [sampler](https://github.com/sqshq/sampler) Github page).

Install sampler:

```bash sudo wget https://github.com/sqshq/sampler/releases/download/v1.1.0/sampler-1.1.0-linux-amd64 -O /usr/local/bin/sampler
sudo chmod +x /usr/local/bin/sampler
```

Download example file:

```bash
wget https://raw.githubusercontent.com/sqshq/sampler/master/example.yml
```

