from DashboardApp.models import Run, Benchmark, TotalResults, TaskGraphResults, HardwareConfiguration, SoftwareConfiguration, TaskResults
from django.http import Http404
from django.db import IntegrityError

class DatabaseManager:
    """
    Provides an API for the access to the DB
    """

    def clear_database(self):
        """
        Clears the contents of the database
        Warning: Does not reset auto-increment fields in tables
        :return: "ok" for successful operation, exception otherwise
        """
        Run.objects.all().delete()
        return "ok"

    def get_run(self, run_id):
        """
        Fetches a run from the DB in a dict.

        :param run_id: ID of the Run
        :return: Dict containing the run data
        :raise: Http404 exception when run not found
        """
        try:
            stored_run = Run.objects.get(pk=run_id)
        except Run.DoesNotExist:
            raise Http404(f"Run <{run_id}> does not exist!")

        run = {
            'RunID': stored_run.RunID,
            'DateTime': stored_run.DateTime,
            'CommitPoint': stored_run.CommitPoint,
            'LatestRelease': stored_run.LatestRelease,
            'Description': stored_run.Description,
        }
        return run

    def get_runs(self):
        """
        Fetches all runs from the DB

        :return: a list of run dicts
        """
        runs = Run.objects.all()
        run_data = []
        for stored_run in runs:
            run = {
                'RunID': stored_run.RunID,
                'DateTime': stored_run.DateTime,
                'CommitPoint': stored_run.CommitPoint,
                'LatestRelease': stored_run.LatestRelease,
                'Description': stored_run.Description,
            }
            run_data.append(run)
        return run_data

    def get_benchmarks(self, run_id):
        """
        Fetches benchmarks for a specific run from the DB

        :param run_id: ID of the Run
        :return: A list of benchmark data for the run
        :raise: Http404 when run is not found
        """
        try:
            run = Run.objects.get(pk=run_id)
        except Run.DoesNotExist:
            raise Http404(f"Run <{run_id}> does not exist!")

        benchmarks = []
        for benchmark in run.benchmarks.all():
            benchmark_data = {
                'BenchmarkID': benchmark.BenchmarkID,
                'BenchmarkName': benchmark.BenchmarkName,
                'NumberOfIterations': benchmark.NumberOfIterations,
                'BenchmarkFlags': benchmark.BenchmarkFlags,
                'MTMD': benchmark.MTMD,
                'SizeType': benchmark.SizeType,
                'SizeNumber': benchmark.SizeNumber,
                'Dimension': benchmark.Dimension,
            }
            benchmarks.append(benchmark_data)
        return benchmarks


    def get_total_results(self, benchmark_id):
        """
        Fetches total results for a specific benchmark from the DB

        :param benchmark_id: ID of the Benchmark
        :return: A list of total result data for the benchmark
        :raise: Http404 when benchmark is not found
        """
        try:
            benchmark = Benchmark.objects.get(pk=benchmark_id)
        except Benchmark.DoesNotExist:
            raise Http404(f"Benchmark <{benchmark_id}> does not exist!")

        total_results = []
        for result in benchmark.total_results.all():
            result_data = {
                'ResultID': result.ResultID,
                'TotalAverageTime': result.TotalAverageTime,
                'TotalMedianTime': result.TotalMedianTime,
                'TotalFirstIteration': result.TotalFirstIteration,
                'TotalBest': result.TotalBest,
                'TotalMinimum': result.TotalMinimum,
                'TotalSpeedup': result.TotalSpeedup,
            }
            total_results.append(result_data)
        return total_results

    def get_task_graph_results(self, result_id):
        """
        Fetches task graph results for a specific total result from the DB

        :param result_id: ID of the TotalResults
        :return: A list of task graph result data for the total result
        :raise: Http404 when total result is not found
        """
        try:
            total_results = TotalResults.objects.get(pk=result_id)
        except TotalResults.DoesNotExist:
            raise Http404(f"TotalResults <{result_id}> does not exist!")

        task_graph_results_data = {
            'TaskGraphID': total_results.task_graph_results.TaskGraphID,
            'MinimumKernelsTime': total_results.task_graph_results.MinimumKernelsTime,
            'KernelAverage': total_results.task_graph_results.KernelAverage,
            'Copy_IN': total_results.task_graph_results.Copy_IN,
            'Copy_OUT': total_results.task_graph_results.Copy_OUT,
            'Compilation_Graal': total_results.task_graph_results.Compilation_Graal,
            'Compilation_Driver': total_results.task_graph_results.Compilation_Driver,
            'Dispatch_Time': total_results.task_graph_results.Dispatch_Time,
        }
        return task_graph_results_data

    def get_hardware_configuration(self, hardware_info_id):
        """
        Fetches hardware configuration data from the DB

        :param hardware_info_id: ID of the HardwareConfiguration
        :return: Hardware configuration data
        :raise: Http404 when hardware configuration is not found
        """
        try:
            hardware_info = HardwareConfiguration.objects.get(pk=hardware_info_id)
        except HardwareConfiguration.DoesNotExist:
            raise Http404(f"HardwareConfiguration <{hardware_info_id}> does not exist!")

        hardware_info_data = {
            'HardwareInfo': hardware_info.HardwareInfo,
            'DeviceID': hardware_info.DeviceID,
            'DeviceTypeGPU': hardware_info.DeviceTypeGPU,
            'DeviceName': hardware_info.DeviceName,
            'GlobalMemorySize': hardware_info.GlobalMemorySize,
            'LocalMemorySize': hardware_info.LocalMemorySize,
            'GlobalThreadNumber': hardware_info.GlobalThreadNumber,
            'LocalThreadNumber': hardware_info.LocalThreadNumber,
            'MaxFrequency': hardware_info.MaxFrequency,
            'ComputeUnits': hardware_info.ComputeUnits,
            'DeviceExtensions': hardware_info.DeviceExtensions,
            'ComputeCapability': hardware_info.ComputeCapability,
            'DevicePartitioning': hardware_info.DevicePartitioning,
            'MaxWorkItemDimension': hardware_info.MaxWorkItemDimension,
            'UnifiedMemory': hardware_info.UnifiedMemory,
            'AtomicSupport': hardware_info.AtomicSupport,
            'HalfPrecisionSupport': hardware_info.HalfPrecisionSupport,
            'DoubleSupport': hardware_info.DoubleSupport,
        }
        return hardware_info_data

    def get_software_configuration(self, software_info_id):
        """
        Fetches software configuration data from the DB

        :param software_info_id: ID of the SoftwareConfiguration
        :return: Software configuration data
        :raise: Http404 when software configuration is not found
        """
        try:
            software_info = SoftwareConfiguration.objects.get(pk=software_info_id)
        except SoftwareConfiguration.DoesNotExist:
            raise Http404(f"SoftwareConfiguration <{software_info_id}> does not exist!")

        software_info_data = {
            'OSVersion': software_info.OSVersion,
            'DriverVersion': software_info.DriverVersion,
            'JVMVersion': software_info.JVMVersion,
            'GCCVersion': software_info.GCCVersion,
            'MavenVersion': software_info.MavenVersion,
            'CmakeVersion': software_info.CmakeVersion,
            'PythonVersion': software_info.PythonVersion,
        }
        return software_info_data

    def get_task_results(self, task_id):
        """
        Fetches task results for a specific task from the DB

        :param task_id: ID of the TaskResults
        :return: Task result data
        :raise: Http404 when task result is not found
        """
        try:
            task_results = TaskResults.objects.get(pk=task_id)
        except TaskResults.DoesNotExist:
            raise Http404(f"TaskResults <{task_id}> does not exist!")

        task_results_data = {
            'TaskID': task_results.TaskID,
            'HardwareInfo': self.get_hardware_configuration(task_results.HardwareInfo.HardwareInfo),
            'SoftwareInfo': self.get_software_configuration(task_results.SoftwareInfo.SoftwareID),
            'KernelTime': task_results.KernelTime,
            'CodeGenerationTime': task_results.CodeGenerationTime,
            'DriverCompilationTime': task_results.DriverCompilationTime,
        }
        return task_results_data


    def refresh_database(self, runs):
        '''
        This function purges the old contents of the DB and inserts the new ones

        :param runs: An array of details about each run
        :return: "ok" after a successful operation, an exception value if unsuccessful
        '''

        self.clear_database()

        try:
            for run_data in runs:
                run = Run.objects.create(
                    DateTime=run_data['DateTime'],
                    CommitPoint=run_data['CommitPoint'],
                    LatestRelease=run_data['LatestRelease'],
                    Description=run_data['Description']
                )

                for benchmark_data in run_data['benchmarks']:
                    benchmark = Benchmark.objects.create(
                        RunID=run,
                        BenchmarkName=benchmark_data['BenchmarkName'],
                        NumberOfIterations=benchmark_data['NumberOfIterations'],
                        BenchmarkFlags=benchmark_data['BenchmarkFlags'],
                        MTMD=benchmark_data['MTMD'],
                        SizeType=benchmark_data['SizeType'],
                        SizeNumber=benchmark_data['SizeNumber'],
                        Dimension=benchmark_data['Dimension']
                    )

                    total_results_data = benchmark_data.get('total_results')
                    if total_results_data:
                        total_results = TotalResults.objects.create(
                            BenchmarkID=benchmark,
                            TotalAverageTime=total_results_data['TotalAverageTime'],
                            TotalMedianTime=total_results_data['TotalMedianTime'],
                            TotalFirstIteration=total_results_data['TotalFirstIteration'],
                            TotalBest=total_results_data['TotalBest'],
                            TotalMinimum=total_results_data['TotalMinimum'],
                            TotalSpeedup=total_results_data['TotalSpeedup']
                        )

                        task_graph_results_data = total_results_data.get('task_graph_results')
                        if task_graph_results_data:
                            TaskGraphResults.objects.create(
                                ResultID=total_results,
                                MinimumKernelsTime=task_graph_results_data['MinimumKernelsTime'],
                                KernelAverage=task_graph_results_data['KernelAverage'],
                                Copy_IN=task_graph_results_data['Copy_IN'],
                                Copy_OUT=task_graph_results_data['Copy_OUT'],
                                Compilation_Graal=task_graph_results_data['Compilation_Graal'],
                                Compilation_Driver=task_graph_results_data['Compilation_Driver'],
                                Dispatch_Time=task_graph_results_data['Dispatch_Time']
                            )

                    hardware_info_data = benchmark_data.get('hardware_info')
                    software_info_data = benchmark_data.get('software_info')
                    if hardware_info_data and software_info_data:
                        hardware_info = HardwareConfiguration.objects.create(**hardware_info_data)
                        software_info = SoftwareConfiguration.objects.create(**software_info_data)
                        TaskResults.objects.create(
                            TaskGraphID=total_results.task_graph_results,
                            HardwareInfo=hardware_info,
                            SoftwareInfo=software_info,
                            KernelTime=benchmark_data['KernelTime'],
                            CodeGenerationTime=benchmark_data['CodeGenerationTime'],
                            DriverCompilationTime=benchmark_data['DriverCompilationTime']
                        )

        except IntegrityError as i:
            return "Integrity Error: " + str(i)

        return "ok"
