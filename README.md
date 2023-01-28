<p align="center">
  <img src="img/ytxt_logo.svg" alt="ytxt">
</p>

<h1 align="center">
  ytxt
</h1>

![asciinemagifgenerator](img/agg.gif)

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
- Easy customizable through flags. (for example: easy to choose different subtitle languages)
- Easy to use Command Line Interface thanks to argparse.

See [samples folder](samples/) for understanding how it works.

## Requirements
### For installation
[python-pip](https://pip.pypa.io/en/stable/) - pip is the package installer for Python. You can use it to install packages from the Python Package Index and other indexes.

### For building
[python-poetry](https://python-poetry.org/) - Python packaging and dependency management made easy.

Installing dependencies
```bash
poetry install
```

Installing dependencies
```bash
poetry install
```

Activating the virtual environment
```bash
poetry shell
```

Deactivating the virtual environment leaving the shell
```bash
exit
```
or `CTRL + D`


Deactivate the virtual environment without leaving the shell
```bash
deactivate
```

Update dependencies (in the same folder with `pyproject.toml` and `poetry.lock`)
```bash
poetry update
```

For more commands, check out [Python Poetry's Basic Usage](https://python-poetry.org/docs/basic-usage/).

## Installation
Locally:
```bash
pip install ytxt-0.1.1-py3-none-any.whl
```
From [PyPi](https://pypi.org/):
`Coming soon!`

## Troubleshooting
Windows: `pip` / `ytxt` is not recognized as an internal or external command, operable program or batch file.
1. Make sure that you installed python-pip and ytxt correctly.
2. If so, then the problem lies within `Path` environment variable that is needed to see where Python's scripts are installed and how it can execute it.

Solution for system's environment variables using admin privileges
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$HOME\AppData\Local\Programs\Python\Python311\Scripts", "Machine")
```

Where `Python311` is your version of Python.

Solution for system's environment variables using admin privileges
```powershell
[Environment]::SetEnvironmentVariable("INCLUDE", $env:INCLUDE + ";$HOME\AppData\Roaming\Python\Python311\Scripts", "User")
```

Where `Python311` is your version of Python.

GNU/Linux / MacOS: bash: `pip` / `ytxt`: command not found
1. Make sure that you installed python-pip and ytxt correctly.
2. If so, then the problem lies within `Path` environment variable that is needed to see where Python's scripts are installed and how it can execute it.

GNU/Linux / MacOS: bash: `ytxt`: command not found
1. Make sure that you installed python-pip and ytxt correctly.
2. If so, MacOS users are doomed and Linux users will figure it out.

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

Console output
```bash
usage: YTXT - YouTube Video to TXT [-h] [-l [LANG ...]] [-sl] URL [URL ...]

positional arguments:
  URL                   YouTube video URLs

options:
  -h, --help            show this help message and exit
  -l [LANG ...], --languages [LANG ...]
                        subtitles languages (default=['en', 'en-GB']) (list)
  -sl, --sub-langs      prints all available subtitles languages
```

### List subtitles' languages
Syntax
```bash
ytxt URL [URL ...] -sl, --sub-langs
```

Example
```bash
ytxt https://youtu.be/h6fcK_fRYaI -sl
```

Console output (without automatic caption output)
```bash
[youtube] Extracting URL: https://youtu.be/I9hJ_Rux9y0
[youtube] I9hJ_Rux9y0: Downloading webpage
[youtube] I9hJ_Rux9y0: Downloading android player API JSON
[info] Available subtitles for h6fcK_fRYaI:
Language Name                     Formats
ar       Arabic                   vtt, ttml, srv3, srv2, srv1, json3
az       Azerbaijani              vtt, ttml, srv3, srv2, srv1, json3
bn       Bangla                   vtt, ttml, srv3, srv2, srv1, json3
be       Belarusian               vtt, ttml, srv3, srv2, srv1, json3
bs       Bosnian                  vtt, ttml, srv3, srv2, srv1, json3
bg       Bulgarian                vtt, ttml, srv3, srv2, srv1, json3
my       Burmese                  vtt, ttml, srv3, srv2, srv1, json3
ca       Catalan                  vtt, ttml, srv3, srv2, srv1, json3
zh       Chinese                  vtt, ttml, srv3, srv2, srv1, json3
zh-CN    Chinese (China)          vtt, ttml, srv3, srv2, srv1, json3
zh-Hans  Chinese (Simplified)     vtt, ttml, srv3, srv2, srv1, json3
zh-TW    Chinese (Taiwan)         vtt, ttml, srv3, srv2, srv1, json3
hr       Croatian                 vtt, ttml, srv3, srv2, srv1, json3
cs       Czech                    vtt, ttml, srv3, srv2, srv1, json3
da       Danish                   vtt, ttml, srv3, srv2, srv1, json3
nl       Dutch                    vtt, ttml, srv3, srv2, srv1, json3
en-GB    English (United Kingdom) vtt, ttml, srv3, srv2, srv1, json3
eo       Esperanto                vtt, ttml, srv3, srv2, srv1, json3
et       Estonian                 vtt, ttml, srv3, srv2, srv1, json3
fil      Filipino                 vtt, ttml, srv3, srv2, srv1, json3
fi       Finnish                  vtt, ttml, srv3, srv2, srv1, json3
fr       French                   vtt, ttml, srv3, srv2, srv1, json3
fr-CA    French (Canada)          vtt, ttml, srv3, srv2, srv1, json3
fr-FR    French (France)          vtt, ttml, srv3, srv2, srv1, json3
ka       Georgian                 vtt, ttml, srv3, srv2, srv1, json3
de       German                   vtt, ttml, srv3, srv2, srv1, json3
el       Greek                    vtt, ttml, srv3, srv2, srv1, json3
iw       Hebrew                   vtt, ttml, srv3, srv2, srv1, json3
hi       Hindi                    vtt, ttml, srv3, srv2, srv1, json3
hu       Hungarian                vtt, ttml, srv3, srv2, srv1, json3
id       Indonesian               vtt, ttml, srv3, srv2, srv1, json3
it       Italian                  vtt, ttml, srv3, srv2, srv1, json3
ja       Japanese                 vtt, ttml, srv3, srv2, srv1, json3
kk       Kazakh                   vtt, ttml, srv3, srv2, srv1, json3
ko       Korean                   vtt, ttml, srv3, srv2, srv1, json3
ku       Kurdish                  vtt, ttml, srv3, srv2, srv1, json3
lv       Latvian                  vtt, ttml, srv3, srv2, srv1, json3
lt       Lithuanian               vtt, ttml, srv3, srv2, srv1, json3
ms       Malay                    vtt, ttml, srv3, srv2, srv1, json3
mn       Mongolian                vtt, ttml, srv3, srv2, srv1, json3
no       Norwegian                vtt, ttml, srv3, srv2, srv1, json3
fa       Persian                  vtt, ttml, srv3, srv2, srv1, json3
pl       Polish                   vtt, ttml, srv3, srv2, srv1, json3
pt       Portuguese               vtt, ttml, srv3, srv2, srv1, json3
pt-BR    Portuguese (Brazil)      vtt, ttml, srv3, srv2, srv1, json3
pt-PT    Portuguese (Portugal)    vtt, ttml, srv3, srv2, srv1, json3
ro       Romanian                 vtt, ttml, srv3, srv2, srv1, json3
ru       Russian                  vtt, ttml, srv3, srv2, srv1, json3
sr       Serbian                  vtt, ttml, srv3, srv2, srv1, json3
sr-Latn  Serbian (Latin)          vtt, ttml, srv3, srv2, srv1, json3
sk       Slovak                   vtt, ttml, srv3, srv2, srv1, json3
sl       Slovenian                vtt, ttml, srv3, srv2, srv1, json3
es       Spanish                  vtt, ttml, srv3, srv2, srv1, json3
es-419   Spanish (Latin America)  vtt, ttml, srv3, srv2, srv1, json3
es-MX    Spanish (Mexico)         vtt, ttml, srv3, srv2, srv1, json3
es-ES    Spanish (Spain)          vtt, ttml, srv3, srv2, srv1, json3
sv       Swedish                  vtt, ttml, srv3, srv2, srv1, json3
ta       Tamil                    vtt, ttml, srv3, srv2, srv1, json3
th       Thai                     vtt, ttml, srv3, srv2, srv1, json3
tr       Turkish                  vtt, ttml, srv3, srv2, srv1, json3
uz       Uzbek                    vtt, ttml, srv3, srv2, srv1, json3
vi       Vietnamese               vtt, ttml, srv3, srv2, srv1, json3
```

### Basic usage
Syntax
```
ytxt URL [URL ...]
```

Example
```
ytxt https://youtu.be/h6fcK_fRYaI
```

Console output
```bash
[youtube] Extracting URL: https://youtu.be/h6fcK_fRYaI
[youtube] h6fcK_fRYaI: Downloading webpage
[youtube] h6fcK_fRYaI: Downloading android player API JSON
[info] h6fcK_fRYaI: Downloading subtitles: en-GB
[info] h6fcK_fRYaI: Downloading 1 format(s): 248+251
[info] Writing video subtitles to: The Egg - A Short Story [h6fcK_fRYaI].en-GB.vtt
[download] Destination: The Egg - A Short Story [h6fcK_fRYaI].en-GB.vtt
[download] 100% of    9.44KiB in 00:00:00 at 83.42KiB/s
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
Finished saving The Egg - A Short Story [h6fcK_fRYaI].en-GB.txt
```

Also see 2 files saved in your relative path:
```bash
The Egg - A Short Story [h6fcK_fRYaI].en-GB.txt
The Egg - A Short Story [h6fcK_fRYaI].en-GB.vtt
```

### Changing default languages
Syntax
```bash
ytxt URL [URL ...] -l LANG [LANG ...], --languages LANG [LANG ...]
```

Example
```bash
ytxt https://youtu.be/h6fcK_fRYaI -l de pl
```

Console output
```bash
[youtube] Extracting URL: https://youtu.be/h6fcK_fRYaI
[youtube] h6fcK_fRYaI: Downloading webpage
[youtube] h6fcK_fRYaI: Downloading android player API JSON
[info] h6fcK_fRYaI: Downloading subtitles: de, pl
[info] h6fcK_fRYaI: Downloading 1 format(s): 248+251
Deleting existing file The Egg - A Short Story [h6fcK_fRYaI].de.vtt
[info] Writing video subtitles to: The Egg - A Short Story [h6fcK_fRYaI].de.vtt
[download] Destination: The Egg - A Short Story [h6fcK_fRYaI].de.vtt
[download] 100% of   11.30KiB in 00:00:00 at 98.05KiB/s
Deleting existing file The Egg - A Short Story [h6fcK_fRYaI].pl.vtt
[info] Writing video subtitles to: The Egg - A Short Story [h6fcK_fRYaI].pl.vtt
[download] Destination: The Egg - A Short Story [h6fcK_fRYaI].pl.vtt
[download] 100% of   10.02KiB in 00:00:00 at 85.40KiB/s
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
Finished saving The Egg - A Short Story [h6fcK_fRYaI].de.txt
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
Finished saving The Egg - A Short Story [h6fcK_fRYaI].pl.txt
```

Also see 4 files saved in your relative path:
```bash
The Egg - A Short Story [h6fcK_fRYaI].de.txt
The Egg - A Short Story [h6fcK_fRYaI].de.vtt
The Egg - A Short Story [h6fcK_fRYaI].pl.txt
The Egg - A Short Story [h6fcK_fRYaI].pl.vtt
```

## Contributing
Contributing guidelines work in progress.
However I am already open for pull requests.

## License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](https://choosealicense.com/licenses/gpl-3.0/)

Software licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).
