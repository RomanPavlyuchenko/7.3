import os


def sort_line_count(path_to_folder, path_to_result):
    files_list = os.listdir(path_to_folder)
    os.chdir('files')
    files = {}

    for file in files_list:
        count_lines = sum(1 for line in open(file))
        files[file] = count_lines

    counts_lines = list(files.items())
    counts_lines.sort(key=lambda i: i[1])

    with open(path_to_result, 'w') as w_file:
        for i in counts_lines:
            w_file.write(i[0])
            w_file.write('\n')
            w_file.write(str(i[1]))
            w_file.write('\n')
            with open(os.path.join(path_to_files, i[0])) as file:
                w_file.write(file.read())
            w_file.write('\n')


path_to_files = os.path.join(os.getcwd(), 'files')
path_to_result = os.path.join(os.getcwd(), 'result.txt')
sort_line_count(path_to_files, path_to_result)
