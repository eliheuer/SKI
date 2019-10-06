#!/bin/bash
set -e

prDir="~/Google/fonts/ofl/"
familyName="SKI"

echo "[INFO] Preparing a new $familyName pull request at $prDir"

cp fonts/vf/$familyName-VF.ttf ~/Google/fonts/ofl/Ski/$familyName[wght].ttf

echo "[INFO] Done preparing $familyName pull request at $prDir"
