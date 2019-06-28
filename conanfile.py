from conans import ConanFile, CMake, tools


class FooConan(ConanFile):
    name = "foo"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    no_copy_source = True

    def build(self):
        tools.download("https://speed.hetzner.de/100MB.bin", "100MB.bin")

    def package(self):
        self.copy("*.bin", dst="res")
