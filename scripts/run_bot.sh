#!/bin/bash

VENV=./venv
DEPLOY_FLAG=/opt/invest/deploy_state.flag

touch $DEPLOY_FLAG

if [ ! -d $VENV ]; then
    `which python3` -m venv $VENV
    $VENV/bin/pip install -U pip
fi

$VENV/bin/pip install -U pip
echo "$?"

$VENV/bin/pip install -r requirements.txt
echo "$?"

$VENV/bin/python src/bot/bot.py

rm -f $DEPLOY_FLAG

echo "Run Bot"
