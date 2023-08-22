from django.utils import timezone
from DashboardApp.models import Run, Benchmark, TotalResults, TaskGraphResults, HardwareConfiguration, SoftwareConfiguration, TaskResults

# Create and save a Run instance with timezone-aware DateTime
run = Run.objects.create(
    DateTime=timezone.now(),  # Use timezone-aware datetime
    CommitPoint="abc123",
    LatestRelease="v1.2",
    Description="Test run description"
)
run.save()
print("Run ID: " + str(run.RunID))

# Create and save a Benchmark instance related to the Run
benchmark = Benchmark.objects.create(
    RunID=run,
    BenchmarkName="Test Benchmark",
    NumberOfIterations=10,
    BenchmarkFlags="flag1 flag2",
    MTMD=5,
    SizeType=1,
    SizeNumber="small",
    Dimension=2
)
benchmark.save()
print("Benchmark ID: " + str(benchmark.BenchmarkID))

# Create and save a TotalResults instance related to the Benchmark
total_results = TotalResults.objects.create(
    BenchmarkID=benchmark,
    TotalAverageTime=1000,
    TotalMedianTime=800,
    TotalFirstIteration=1200,
    TotalBest=700,
    TotalMinimum=600,
    TotalSpeedup=1.5
)
total_results.save()
print("Total Results ID: " + str(total_results.ResultID))

# Create and save a TaskGraphResults instance related to the TotalResults
task_graph_results = TaskGraphResults.objects.create(
    ResultID=total_results,
    MinimumKernelsTime=200,
    KernelAverage=180,
    Copy_IN=50,
    Copy_OUT=60,
    Compilation_Graal=100,
    Compilation_Driver=80,
    Dispatch_Time=40
)
task_graph_results.save()
print("Task Graph Results ID: " + str(task_graph_results.TaskGraphID))

# Create and save a HardwareConfiguration instance
hardware_config = HardwareConfiguration.objects.create(
    HardwareInfo="Sample Hardware Info",
    DeviceID=1,
    DeviceTypeGPU="GPU",
    DeviceName="Sample GPU",
    GlobalMemorySize=8192,
    LocalMemorySize=2048,
    GlobalThreadNumber=256,
    LocalThreadNumber=64,
    MaxFrequency=2.0,
    ComputeUnits=32,
    DeviceExtensions="OpenCL 2.0",
    ComputeCapability="7.5",
    DevicePartitioning="None",
    MaxWorkItemDimension=3,
    UnifiedMemory=True,
    AtomicSupport=True,
    HalfPrecisionSupport=True,
    DoubleSupport=False
)
hardware_config.save()
print("Hardware Configuration Info: " + hardware_config.HardwareInfo)

# Create and save a SoftwareConfiguration instance
software_config = SoftwareConfiguration.objects.create(
    OSVersion="Ubuntu 20.04",
    DriverVersion="NVIDIA 470.42.01",
    JVMVersion="OpenJDK 11.0.12",
    GCCVersion="GCC 9.3.0",
    MavenVersion="Maven 3.6.3",
    CmakeVersion="CMake 3.16.3",
    PythonVersion="Python 3.8.10"
)
software_config.save()
print("Software Configuration ID: " + str(software_config.SoftwareID))

# Create and save a TaskResults instance related to the TaskGraphResults, HardwareConfiguration, and SoftwareConfiguration
task_results = TaskResults.objects.create(
    TaskGraphID=task_graph_results,
    HardwareInfo=hardware_config,
    SoftwareInfo=software_config,
    KernelTime=150,
    CodeGenerationTime=80,
    DriverCompilationTime=50
)
task_results.save()
print("Task Results ID: " + str(task_results.TaskID))

print("Database populated with test data.")
