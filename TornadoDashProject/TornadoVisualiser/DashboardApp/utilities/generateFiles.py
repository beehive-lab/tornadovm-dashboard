import subprocess
import os

target_directory = "/Users/ksrivastava/Desktop/UoMInternship/TornadoVM"

os.chdir(target_directory)

# Combine all the commands using '&&' to run them in the same shell
combined_command = (
    "source setvars.sh && "
    "tornado --version && "
    "tornado --jvm='-Xms24G -Xmx24G -server -Dtornado.recover.bailout=False ' -m tornado.benchmarks/uk.ac.manchester.tornado.benchmarks.BenchmarkRunner --params='saxpy' && "
    "tornado --jvm='-Dtornado.profiler=True -Dtornado.log.profiler=True -Dtornado.profiler.dump.dir=/Users/ksrivastava/Desktop/UoMInternship/TornadoVM/info.json' -m tornado.benchmarks/uk.ac.manchester.tornado.benchmarks.BenchmarkRunner --params='sgemm' && "
    "python3 -c 'import platform; print(platform.system())' && "
    "clinfo && "
    "tornado --version && "
    "gcc --version && "
    "mvn --version && "
    "cmake --version && "
    "python3 --version"
)

# Create a file to capture the output
output_file = "/Users/ksrivastava/Desktop/UoMInternship/TornadoVM/out.txt"

with open(output_file, "w") as output:
    # Execute all the commands and redirect the output to the file
    subprocess.run(combined_command, shell=True, executable="/bin/bash", stdout=output)

print(f"Output saved to {output_file}")
