import json
from datetime import datetime
from DashboardApp.models import Run, Benchmark, TotalResults, TaskGraphResults, HardwareConfiguration, SoftwareConfiguration, TaskResults

filepath = ""

    
test_data = {
    "Run": {
        "DateTime": "2023-07-11 10:00:00",
        "CommitPoint": "abc123",
        "LatestRelease": "v1.2",
        "Description": "Test run description"
    },
    "Benchmark": {
        "BenchmarkName": "Test Benchmark",
        "NumberOfIterations": 10,
        "BenchmarkFlags": "flag1 flag2",
        "MTMD": 5,
        "SizeType": 1,
        "SizeNumber": "small",
        "Dimension": 2
    }
}

for item in test_data:
    run = Run(
        DateTime=datetime.strptime(item['DateTime'], '%Y-%m-%d %H:%M:%S'),
        CommitPoint=item['CommitPoint'],
        LatestRelease=item['LatestRelease'],
        Description=item['Description']
    )
    run.save()

    benchmark = Benchmark(
        RunID=run,
        BenchmarkName=item['BenchmarkName'],
        NumberOfIterations=item['NumberOfIterations'],
        BenchmarkFlags=item['BenchmarkFlags'],
        MTMD=item['MTMD'],
        SizeType=item['SizeType'],
        SizeNumber=item['SizeNumber'],
        Dimension=item['Dimension']
    )
    benchmark.save()
    
# with open(filepath, 'r') as json_file:
#     data = json.load(json_file)
    

# for item in data:
#     run = Run(
#         DateTime=datetime.strptime(item['DateTime'], '%Y-%m-%d %H:%M:%S'),
#         CommitPoint=item['CommitPoint'],
#         LatestRelease=item['LatestRelease'],
#         Description=item['Description']
#     )
#     run.save()

#     benchmark = Benchmark(
#         RunID=run,
#         BenchmarkName=item['BenchmarkName'],
#         NumberOfIterations=item['NumberOfIterations'],
#         BenchmarkFlags=item['BenchmarkFlags'],
#         MTMD=item['MTMD'],
#         SizeType=item['SizeType'],
#         SizeNumber=item['SizeNumber'],
#         Dimension=item['Dimension']
#     )
#     benchmark.save()

#     total_results = TotalResults(
#         BenchmarkID=benchmark,
#         TotalAverageTime=item['TotalAverageTime'],
#         TotalMedianTime=item['TotalMedianTime'],
#         TotalFirstIteration=item['TotalFirstIteration'],
#         TotalBest=item['TotalBest'],
#         TotalMinimum=item['TotalMinimum'],
#         TotalSpeedup=item['TotalSpeedup']
#     )
#     total_results.save()

#     task_graph_results = TaskGraphResults(
#         ResultID=total_results,
#         MinimumKernelsTime=item['MinimumKernelsTime'],
#         KernelAverage=item['KernelAverage'],
#         Copy_IN=item['Copy_IN'],
#         Copy_OUT=item['Copy_OUT'],
#         Compilation_Graal=item['Compilation_Graal'],
#         Compilation_Driver=item['Compilation_Driver'],
#         Dispatch_Time=item['Dispatch_Time']
#     )
#     task_graph_results.save()

#     hardware_configuration = HardwareConfiguration(**item['HardwareInfo'])
#     hardware_configuration.save()

#     software_configuration = SoftwareConfiguration(**item['SoftwareInfo'])
#     software_configuration.save()

#     task_results = TaskResults(
#         TaskGraphID=task_graph_results,
#         HardwareInfo=hardware_configuration,
#         SoftwareInfo=software_configuration,
#         KernelTime=item['KernelTime'],
#         CodeGenerationTime=item['CodeGenerationTime'],
#         DriverCompilationTime=item['DriverCompilationTime']
#     )
#     task_results.save()
