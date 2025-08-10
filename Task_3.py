def merge_files(input_files, output_file):
    files_info = []
    for filename in input_files:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            files_info.append((filename, len(lines), lines))

        files_info.sort(key=lambda x: x[1]) # эту строку списала из чата gpt и совсем не поняла, что она означает


    with open(output_file, 'w', encoding='utf-8') as f_out:
        for filename, line_count, lines in files_info:
            f_out.write(f"{filename}\n{line_count}\n")
            f_out.writelines(lines)