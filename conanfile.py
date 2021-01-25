from conans import CMake
from conans import ConanFile


class OpenTracingCppConan(ConanFile):
    name = "opentracing-cpp"
    version = "0.0.3"
    description = ""
    author = "Innokentii Mokin <mia@tomsksoft.com>"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = (
    )
    requires = (
    )
    exports = "*"

    def configure(self):
        self.options["*"].shared = False
        self.options["*"].fPIC = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["opentracing"]
