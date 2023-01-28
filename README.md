<p align="center">
  <img src="img/ytxt_logo.svg" alt="ytxt">
</p>

<h1 align="center">
  ytxt
</h1>

<p align="center">
  This module downloads subtitles in .vtt file format then it opens it as a regular .txt file removes not needed stuff and in the end it saves to a clean looking .txt file with the same name.
</p>

# Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Troubleshooting](#troubleshooting)
5. [Usage with examples](#usage-with-examples)
6. [Contributing](#contributing)
7. [License](#license)

## Features
- Downloads .vtt subtitle files and saves it to a clean looking .txt file with the same name.
- Easy customizable through flags. (for example easy to choose different subtitle languages)
- Easy to use Command Line Interface thanks to argparse.

## Requirements
### For installation
[python-pip](https://pip.pypa.io/en/stable/) - pip is the package installer for Python. You can use it to install packages from the Python Package Index and other indexes.

### For building
[python-poetry](https://python-poetry.org/) - Python packaging and dependency management made easy.

Installing dependencies
```bash
poetry install
```

Update dependencies (in the same folder with `pyproject.toml` and `poetry.lock`)
```bash
poetry update
```

For more commands check out [Python's Poetry Basic Usage](https://python-poetry.org/docs/basic-usage/).

## Installation
Locally:
```bash
pip install ytxt-0.1.0-py3-none-any.whl
```
From [PyPi](https://pypi.org/):

`After fixing the -l / --languages bug.`

## Troubleshooting
pip not found

Windows does not recognize ytxt

## Usage with examples

### Getting help
Syntax
```bash
ytxt -h, --help
```

Example
```bash
ytxt -h
```

Output
```bash
usage: YTXT - YouTube Video to TXT [-h] [-l LANG [LANG ...]] [-sl] [URL ...]

positional arguments:
  URL                   YouTube video URLs

options:
  -h, --help            show this help message and exit
  -l LANG [LANG ...], --languages LANG [LANG ...]
                        subtitles languages (default=['en', 'en-GB']) (list)
  -sl, --sub-langs      prints all available subtitles languages
```

### List subtitles languages
Syntax
```bash
ytxt -sl, --sub-langs [URL ...]
```

Example
```bash
ytxt -sl https://youtu.be/I9hJ_Rux9y0
```

Console output (shorten automatic caption)
```bash
[youtube] Extracting URL: https://youtu.be/I9hJ_Rux9y0
[youtube] I9hJ_Rux9y0: Downloading webpage
[youtube] I9hJ_Rux9y0: Downloading android player API JSON
[info] Available subtitles for I9hJ_Rux9y0:
Language Name                     Formats
zh-Hant  Chinese (Traditional)    vtt, ttml, srv3, srv2, srv1, json3
en-GB    English (United Kingdom) vtt, ttml, srv3, srv2, srv1, json3
iw       Hebrew                   vtt, ttml, srv3, srv2, srv1, json3
it       Italian                  vtt, ttml, srv3, srv2, srv1, json3
ja       Japanese                 vtt, ttml, srv3, srv2, srv1, json3
ko       Korean                   vtt, ttml, srv3, srv2, srv1, json3
ro       Romanian                 vtt, ttml, srv3, srv2, srv1, json3
th       Thai                     vtt, ttml, srv3, srv2, srv1, json3
tr       Turkish                  vtt, ttml, srv3, srv2, srv1, json3
```

### Basic usage
Syntax
```
ytxt [URL ...]
```

Example
```
ytxt https://youtu.be/I9hJ_Rux9y0
```

Console output
```bash
[youtube] Extracting URL: https://youtu.be/I9hJ_Rux9y0
[youtube] I9hJ_Rux9y0: Downloading webpage
[youtube] I9hJ_Rux9y0: Downloading android player API JSON
[info] I9hJ_Rux9y0: Downloading subtitles: en-GB
[info] I9hJ_Rux9y0: Downloading 1 format(s): 303+251
[info] Writing video subtitles to: Why You Are Lonely and How to Make Friends [I9hJ_Rux9y0].en-GB.vtt
[download] Destination: Why You Are Lonely and How to Make Friends [I9hJ_Rux9y0].en-GB.vtt
[download] 100% of   18.64KiB in 00:00:00 at 148.37KiB/s
Deleting subtitles heading...
Done 1/5
Deleting subtitles timestamps...
Done 2/5
Deleting subtitles newlines...
Done 3/5
Deleting start and end whitespace...
Done 4/5
Deleting double or more whitespace...
Done. 5/5
Creating the txt file...
Finished saving Why You Are Lonely and How to Make Friends [I9hJ_Rux9y0].en-GB.txt
```

And 2 files in your relative pathtoo:
```bash
Why You Are Lonely and How to Make Friends [I9hJ_Rux9y0].en-GB.txt
Why You Are Lonely and How to Make Friends [I9hJ_Rux9y0].en-GB.vtt
```

### Changing default languages
Syntax
```bash
ytxt -l LANG [LANG ...], --languages LANG [LANG ...]
```

Example
```bash
ytxt -l pl de https://youtu.be/h6fcK_fRYaI
```

Console output WIP
```bash

```

## Contributing
Contributing guidelines work in progress, however I am already open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).

# TODO
- Thumbnail for this repo
- Settings for this repo
