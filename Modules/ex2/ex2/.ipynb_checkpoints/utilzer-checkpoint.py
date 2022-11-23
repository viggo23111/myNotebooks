import utils

            
if __name__=='__main__':
    utils.get_file_names('/home/jovyan/my_notebooks/Modules/ex2', out='import_output1.txt')
    utils.get_all_file_names('/home/jovyan/my_notebooks/Modules/ex2', out='import_output2.txt')
    utils.print_line_one('test1.txt','test2.txt','test3.txt')
    utils.print_emails('test1.txt','test2.txt','test3.txt')
    utils.write_headlines('md1.md','md2.md','md3.md',out='import_output3.txt')