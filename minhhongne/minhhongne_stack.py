from aws_cdk import core
from . import resume_service

class MinhhongneStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        resume_service.ResumeService(self, "ResumeApis")
