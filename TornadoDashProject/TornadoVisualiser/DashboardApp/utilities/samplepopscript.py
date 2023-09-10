import json
from datetime import datetime
from DashboardApp.models import (Run, Benchmark, TotalResults, TaskGraphResults,
                                 HardwareConfiguration, SoftwareConfiguration, TaskResults)

# Load the JSON data from the "output.json" file
with open('output.json', 'r') as json_file:
    data = json.load(json_file)

# Extract information from the JSON data
device_name = data.get("Apple", {}).get("Device Name", "Unknown")
cmake_version = data.get("CMake", {}).get("CMake Version", "Unknown")
gcc_version = data.get("GCC", {}).get("GCC Version", "Unknown")
maven_version = data.get("Maven", {}).get("Maven Version", "Unknown")
python_version = data.get("Python", "Unknown")

saxpy_data = data.get("SaxpyOutput", {})
sgemm_data = data.get("SgemmProfilerOutput", {})

# Create a new Run record
run = Run(DateTime=datetime.now(),
          CommitPoint="Unknown",
          LatestRelease="Unknown",
          Description="")

run.save()  # Save the Run record to the database

# Create HardwareConfiguration record
hardware_info = HardwareConfiguration(HardwareInfo="Unknown",
                                      DeviceID=0,
                                      DeviceTypeGPU="Unknown",
                                      DeviceName=device_name,
                                      GlobalMemorySize=0,
                                      LocalMemorySize=0,
                                      GlobalThreadNumber=0,
                                      LocalThreadNumber=0,
                                      MaxFrequency=0.0,
                                      ComputeUnits=0,
                                      DeviceExtensions="Unknown",
                                      ComputeCapability="Unknown",
                                      DevicePartitioning="Unknown",
                                      MaxWorkItemDimension=0,
                                      UnifiedMemory=False,
                                      AtomicSupport=False,
                                      HalfPrecisionSupport=False,
                                      DoubleSupport=False)

hardware_info.save()  # Save the HardwareConfiguration record to the database

# Create SoftwareConfiguration record
software_info = SoftwareConfiguration(OSVersion="Unknown",
                                      DriverVersion="Unknown",
                                      JVMVersion="Unknown",
                                      GCCVersion=gcc_version,
                                      MavenVersion=maven_version,
                                      CmakeVersion=cmake_version,
                                      PythonVersion=python_version)

software_info.save()  # Save the SoftwareConfiguration record to the database

# Loop through the Saxpy data and create Benchmark and TotalResults records
for benchmark_name, benchmark_info in saxpy_data.items():
    benchmark = Benchmark(RunID=run,
                          BenchmarkName=benchmark_name,
                          NumberOfIterations=0,
                          BenchmarkFlags="",
                          MTMD=0,
                          SizeType=0,
                          SizeNumber="",
                          Dimension=0)
    
    benchmark.save()  # Save the Benchmark record to the database

    total_results = TotalResults(BenchmarkID=benchmark,
                                 TotalAverageTime=benchmark_info["Average"],
                                 TotalMedianTime=benchmark_info["Median"],
                                 TotalFirstIteration=benchmark_info["FirstIteration"],
                                 TotalBest=benchmark_info["Best"],
                                 TotalMinimum=0,
                                 TotalSpeedup=0.0)

    total_results.save()  # Save the TotalResults record to the database

# Loop through the Sgemm data and create Benchmark and TotalResults records
for benchmark_name, benchmark_info in sgemm_data.items():
    benchmark = Benchmark(RunID=run,
                          BenchmarkName=benchmark_name,
                          NumberOfIterations=0,
                          BenchmarkFlags="",
                          MTMD=0,
                          SizeType=0,
                          SizeNumber="",
                          Dimension=0)
    
    benchmark.save()  # Save the Benchmark record to the database

    total_results = TotalResults(BenchmarkID=benchmark,
                                 TotalAverageTime=benchmark_info["KernelAvg"],
                                 TotalMedianTime=benchmark_info["KernelAvg"],
                                 TotalFirstIteration=0,
                                 TotalBest=0,
                                 TotalMinimum=benchmark_info["KernelMin"],
                                 TotalSpeedup=0.0)

    total_results.save()  # Save the TotalResults record to the database

# Print a message to indicate that the data has been populated
print("Data has been populated into the database.")
