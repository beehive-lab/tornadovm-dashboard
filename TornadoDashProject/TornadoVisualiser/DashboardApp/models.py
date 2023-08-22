from django.db import models

class Run(models.Model):
    RunID = models.AutoField(primary_key=True)
    DateTime = models.DateTimeField()
    CommitPoint = models.CharField(max_length=255)
    LatestRelease = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)

class Benchmark(models.Model):
    BenchmarkID = models.AutoField(primary_key=True)
    RunID = models.ForeignKey(Run, on_delete=models.CASCADE, related_name='benchmarks')
    BenchmarkName = models.CharField(max_length=255)
    NumberOfIterations = models.IntegerField()
    BenchmarkFlags = models.CharField(max_length=255)
    MTMD = models.IntegerField()
    SizeType = models.IntegerField()
    SizeNumber = models.CharField(max_length=255)
    Dimension = models.IntegerField()

class TotalResults(models.Model):
    ResultID = models.AutoField(primary_key=True)
    BenchmarkID = models.ForeignKey(Benchmark, on_delete=models.CASCADE, related_name='total_results')
    TotalAverageTime = models.BigIntegerField()
    TotalMedianTime = models.BigIntegerField()
    TotalFirstIteration = models.BigIntegerField()
    TotalBest = models.BigIntegerField()
    TotalMinimum = models.BigIntegerField()
    TotalSpeedup = models.FloatField()

class TaskGraphResults(models.Model):
    TaskGraphID = models.AutoField(primary_key=True)
    ResultID = models.ForeignKey(TotalResults, on_delete=models.CASCADE, related_name='task_graph_results')
    MinimumKernelsTime = models.IntegerField()
    KernelAverage = models.IntegerField()
    Copy_IN = models.IntegerField()
    Copy_OUT = models.IntegerField()
    Compilation_Graal = models.IntegerField()
    Compilation_Driver = models.IntegerField()
    Dispatch_Time = models.IntegerField()

class HardwareConfiguration(models.Model):
    HardwareInfo = models.CharField(primary_key=True, max_length=255)
    DeviceID = models.IntegerField()
    DeviceTypeGPU = models.CharField(max_length=255)
    DeviceName = models.CharField(max_length=255)
    GlobalMemorySize = models.IntegerField()
    LocalMemorySize = models.IntegerField()
    GlobalThreadNumber = models.IntegerField()
    LocalThreadNumber = models.IntegerField()
    MaxFrequency = models.FloatField()
    ComputeUnits = models.IntegerField()
    DeviceExtensions = models.CharField(max_length=255)
    ComputeCapability = models.CharField(max_length=255)
    DevicePartitioning = models.CharField(max_length=255)
    MaxWorkItemDimension = models.IntegerField()
    UnifiedMemory = models.BooleanField()
    AtomicSupport = models.BooleanField()
    HalfPrecisionSupport = models.BooleanField()
    DoubleSupport = models.BooleanField()

class SoftwareConfiguration(models.Model):
    SoftwareID = models.AutoField(primary_key=True)
    OSVersion = models.CharField(max_length=255)
    DriverVersion = models.CharField(max_length=255)
    JVMVersion = models.CharField(max_length=255)
    GCCVersion = models.CharField(max_length=255)
    MavenVersion = models.CharField(max_length=255)
    CmakeVersion = models.CharField(max_length=255)
    PythonVersion = models.CharField(max_length=255)

class TaskResults(models.Model):
    TaskID = models.AutoField(primary_key=True)
    TaskGraphID = models.ForeignKey(TaskGraphResults, on_delete=models.CASCADE, related_name='task_results')
    HardwareInfo = models.OneToOneField(HardwareConfiguration, on_delete=models.CASCADE, related_name='task_results')
    SoftwareInfo = models.OneToOneField(SoftwareConfiguration, on_delete=models.CASCADE, related_name='task_results')
    KernelTime = models.IntegerField()
    CodeGenerationTime = models.IntegerField()
    DriverCompilationTime = models.IntegerField()
