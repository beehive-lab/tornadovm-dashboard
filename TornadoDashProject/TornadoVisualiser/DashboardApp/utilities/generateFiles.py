
import subprocess

source_command = "source source.sh"
subprocess.run(source_command, shell=True, executable="/bin/bash")


# Command 1: Get commit point from 'tornado --version'
command1 = "tornado --version"
output1 = subprocess.check_output(command1, shell=True, universal_newlines=True)
commit_point = output1.strip()  # Extract commit point from the output

# Command 2: Get Description and BenchmarkName
command2 = 'tornado --jvm="-Xms24G -Xmx24G -server -Dtornado.recover.bailout=False" -m tornado.benchmarks/uk.ac.manchester.tornado.benchmarks.BenchmarkRunner --params="saxpy"'
output2 = subprocess.check_output(command2, shell=True, universal_newlines=True)
# Extract Description and BenchmarkName from the output
description = "Description: " + output2.split("Description: ")[1].split("\n")[0].strip()
benchmark_name = "BenchmarkName: " + output2.split("BenchmarkName: ")[1].split("\n")[0].strip()

# Command 3: Get OS and its version
import platform
operating_system = "OS: " + platform.system()  # Get OS name
os_version = "OS Version: " + platform.version()  # Get OS version

# Command 4: Get driver info from 'clinfo'
command4 = "clinfo"
driver_info = subprocess.check_output(command4, shell=True, universal_newlines=True)

# Command 5: Get JVM version from 'tornado --version'
command5 = "tornado --version"
output5 = subprocess.check_output(command5, shell=True, universal_newlines=True)
jvm_version = "JVM Version: " + output5.strip()  # Extract JVM version from the output

# Command 6: Get GCC version from 'gcc --version'
command6 = "gcc --version"
gcc_version = subprocess.check_output(command6, shell=True, universal_newlines=True)

# Command 7: Get Maven version from 'mvn --version'
command7 = "mvn --version"
maven_version = subprocess.check_output(command7, shell=True, universal_newlines=True)

# Command 8: Get CMake version from 'cmake --version'
command8 = "cmake --version"
cmake_version = subprocess.check_output(command8, shell=True, universal_newlines=True)

# Command 9: Get Python version from 'python3 --version'
command9 = "python3 --version"
python_version = subprocess.check_output(command9, shell=True, universal_newlines=True)

# Create output files for each piece of information
with open("commit_point.txt", "w") as f:
    f.write(commit_point)

with open("description.txt", "w") as f:
    f.write(description)

with open("benchmark_name.txt", "w") as f:
    f.write(benchmark_name)

with open("operating_system.txt", "w") as f:
    f.write(operating_system)

with open("os_version.txt", "w") as f:
    f.write(os_version)

with open("driver_info.txt", "w") as f:
    f.write(driver_info)

with open("jvm_version.txt", "w") as f:
    f.write(jvm_version)

with open("gcc_version.txt", "w") as f:
    f.write(gcc_version)

with open("maven_version.txt", "w") as f:
    f.write(maven_version)

with open("cmake_version.txt", "w") as f:
    f.write(cmake_version)

with open("python_version.txt", "w") as f:
    f.write(python_version)

print("All information extracted and saved to files.")
