from pat import execute_pat, read_output_file, delete_output_file, parse_output

def main():
    execute_pat()
    output = read_output_file()
    delete_output_file()
    parse_output(output)
    
    
if __name__ == "__main__":
    main()