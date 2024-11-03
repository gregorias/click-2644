# Click 2644

A repro repository for [pallets/click#2644](https://github.com/pallets/click/issues/2644).

Run (adapt to your shell if necessary):

```shell
poetry install
poetry env use 3.13.0
poetry shell
pip install --editable .
set -x PYTHONDEVMODE 1
_CLICK_2644_COMPLETE=fish_complete COMP_WORDS="click-2644" COMP_CWORD="click-2644" click-2644
```

You should see:

```
/Users/grzesiek/Library/Caches/pypoetry/virtualenvs/click-2644-4RRTPb9T-py3.12/lib/python3.12/site-packages/click/shell_completion.py:293: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.md' mode='r' encoding='UTF-8'>
  completions = self.get_completions(args, incomplete)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
```
