import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from keep import utils


def _seed_commands(tmp_path, monkeypatch):
    monkeypatch.setattr(utils, "dir_path", str(tmp_path))
    commands = {"ls -la": {"desc": "list files", "alias": ""}}
    with open(os.path.join(str(tmp_path), "commands.json"), "w") as f:
        json.dump(commands, f)


def test_grep_invalid_regex_does_not_crash(tmp_path, monkeypatch):
    _seed_commands(tmp_path, monkeypatch)
    assert utils.grep_commands("[") == []


def test_grep_valid_regex_still_works(tmp_path, monkeypatch):
    _seed_commands(tmp_path, monkeypatch)
    assert utils.grep_commands("ls.*") == [("ls -la", "list files")]
