# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.get("/add")
def call_add():
    # TODO: Add docstring

    # TODO: implement function
    ...


@app.get("/sub")
def call_sub():
    # TODO: Add docstring

    # TODO: implement function

    ...


@app.get("/mult")
def call_mult():
    # TODO: Add docstring

    # TODO: implement function

    ...


@app.get("/div")
def call_div():
    # TODO: Add docstring

    # TODO: implement function

    ...
