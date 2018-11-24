from snapcraft.plugins.make import MakePlugin


class MicroPythonMakePlugin(MakePlugin):

    def __init__(self, name, options, project):
        super().__init__(name, options, project)

    def make(self, env=None):
        """
        Make axtls before make is required until MicroPython v1.9.4.
        This plugin can be retired after MicroPython v1.9.5 release.
        """

        command = ["make"]
        self.run(command + ["axtls"], env=env)

        super().make(env)
