import os
import re


def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)


def extract_classes_and_functions_back(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    classes = re.findall(r'class\s+\w+', content)
    functions = re.findall(r'def\s+\w+', content)

    return classes, functions


def extract_classes_and_functions_front(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    classes = re.findall(r'interface\s+\w+', content)
    functions = re.findall(r'const\s+\w+', content)

    return classes, functions


def calculate_frontend(directory):
    file_lengths = []
    class_lengths = []
    function_lengths = []
    files_frontend = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.html', '.css', '.js', '.tsx')):
                files_frontend.append(file_path)

                file_length = count_lines(file_path)
                file_lengths.append(file_length)

                classes, functions = extract_classes_and_functions_front(file_path)
                if classes:
                    class_lengths.extend([file_length / len(classes)] * len(classes))
                if functions:
                    function_lengths.extend([file_length / len(functions)] * len(functions))

    avg_file_length = sum(file_lengths) / len(file_lengths) if file_lengths else 0
    avg_class_length = sum(class_lengths) / len(class_lengths) if class_lengths else 0
    avg_function_length = sum(function_lengths) / len(function_lengths) if function_lengths else 0

    return {
        'frontend_files': files_frontend,
        'avg_file_length': avg_file_length,
        'avg_class_length': avg_class_length,
        'avg_function_length': avg_function_length,
    }


def calculate_backend(directory):
    file_lengths = []
    class_lengths = []
    function_lengths = []
    files_back = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.py'):
                files_back.append(file_path)

                file_length = count_lines(file_path)
                file_lengths.append(file_length)

                classes, functions = extract_classes_and_functions_back(file_path)
                if classes:
                    class_lengths.extend([file_length / len(classes)] * len(classes))
                if functions:
                    function_lengths.extend([file_length / len(functions)] * len(functions))

    avg_file_length = sum(file_lengths) / len(file_lengths) if file_lengths else 0
    avg_class_length = sum(class_lengths) / len(class_lengths) if class_lengths else 0
    avg_function_length = sum(function_lengths) / len(function_lengths) if function_lengths else 0

    return {
        'backend_files': files_back,
        'avg_file_length': avg_file_length,
        'avg_class_length': avg_class_length,
        'avg_function_length': avg_function_length,
    }


def generate_statistics(frontend_metricss, backend_metricss):
    print(f"Number of frontend files: {len(frontend_metricss['frontend_files'])}")
    print(f"Average file length of frontend files: {frontend_metricss['avg_file_length']:.2f} lines")
    print(f"Average class length in frontend part: {frontend_metricss['avg_class_length']:.2f} lines")
    print(f"Average function length in frontend part: {frontend_metricss['avg_function_length']:.2f} lines")
    print()
    print(f"Number of backend files: {len(backend_metricss['backend_files'])}")
    print(f"Average file length of backend files: {backend_metricss['avg_file_length']:.2f} lines")
    print(f"Average class length in backend part: {backend_metricss['avg_class_length']:.2f} lines")
    print(f"Average function length in backend part: {backend_metricss['avg_function_length']:.2f} lines")


if __name__ == "__main__":
    directory_path_frontend = '../frontend/'
    directory_path_backend = '../backend/src/'
    frontend_metrics = calculate_frontend(directory_path_frontend)
    backend_metrics = calculate_backend(directory_path_backend)
    generate_statistics(frontend_metrics, backend_metrics)
