#!/bin/sh
set -eu
SOURCE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
DEST="$HOME/Applications/Containerlab GUI.app"
if [ -e "$DEST" ]; then echo "Already installed at $DEST. Refusing to overwrite an existing installation." >&2; exit 1; fi
mkdir -p "$HOME/Applications"
/usr/bin/ditto "$SOURCE/Containerlab GUI.app" "$DEST"
echo "Installed: $DEST"
echo "Start from Finder, or run:"
echo "\"$DEST/Contents/Resources/runtime/node\" \"$DEST/Contents/Resources/packaging/cli.mjs\" serve --open"
