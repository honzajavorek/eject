# eject

Force ejecting external drive on macOS

## Why?

When I browse photo files on my external drive connected to my MacBook and I use the "quick look" feature of Finder, macOS never allows me to disconnect the drive as it gets blocked by some "quick look" processes. This tool automates the process of killing the processes and ejecting the drive.

## Installation

```
brew install https://raw.githubusercontent.com/honzajavorek/eject/master/eject.rb
```

## Release

1. `git tag v1.0.1`
2. `git push origin master --tags`
3. `wget https://github.com/honzajavorek/eject/archive/v1.0.1.zip`
4. `sha256sum *.zip`
5. Edit [eject.rb](eject.rb)
6. `git commit -am "release to homebrew" && git push origin master`
