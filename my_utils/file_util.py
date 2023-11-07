__all__ = ['print_file_info', 'append_file']

def print_file_info(file_name):
    file = None
    try:
        file = open(file_name, "r", encoding="utf-8")
        print(file.read())
    except Exception as e:
        print(e)
    finally:
        if file in locals():
            file.close()

def append_file(file_name, data):
    file = None
    try:
        file = open(file_name, "a", encoding="utf-8")
        file.write(data)
        file.write("\n")
        file.flush()
    except Exception as e:
        print(e)
    finally:
        if file in locals():
            file.close()