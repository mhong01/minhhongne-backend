#!/usr/bin/env python3

from aws_cdk import core

from minhhongne.minhhongne_stack import MinhhongneStack


app = core.App()
MinhhongneStack(app, "minhhongne")

app.synth()
