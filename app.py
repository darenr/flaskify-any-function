#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from flask import Flask, request, render_template, Response

from flask_swagger import swagger
from flask_restplus import Api, Resource, fields, reqparse, abort, fields, Model

import logging
import json
import time

from argparse import ArgumentParser
from importlib import import_module

flask_app = Flask(__name__)
app = Api(app=flask_app)
name_space = app.namespace('app', description='Flaskification of Fn')

logging.basicConfig(level=logging.DEBUG)

@name_space.route("/fn/<modulefn>")
class ModuleRunner(Resource):

    @name_space.expect([fields.String], validate=False)
    def post(self, modulefn):

        if not modulefn:
            abort(404, "no module specified")

        runner_args = request.json # the args to be passed to the function, a single value is first promoted to a list

        logging.info(f" * GET ModuleRunner:: module.fn: {modulefn} args: {runner_args}")

        try:
            start_time = time.time()

            p, m = modulefn.rsplit('.', 1)
            mod = import_module(p)

            if not mod:
                abort(404, f"no module found: {modulefn}")

            else:
                fn = getattr(mod, m)

                result = fn(*runner_args)
                logging.info(f" * GET ModuleRunner:: module.fn: {modulefn} args: {runner_args}, result: {result}")
                duration = time.time() - start_time

                return {
                    "modulefn": modulefn,
                    "args": runner_args,
                    "duration_ms": duration/1000.0,
                    "result": result
                }

        except Exception as e:
            return {
                "modulefn": modulefn,
                "args": runner_args,
                "error": str(e)
            }





if __name__ == '__main__':
    logging.info(f" * server starting")
    flask_app.run(host="0.0.0.0", debug=True)
