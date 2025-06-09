## Linux File Permissions String Breakdown

- **1st character:** File type (`d` for directory, `-` for regular file)
- **2nd-4th:** User permissions (read, write, execute)
- **5th-7th:** Group permissions (read, write, execute)
- **8th-10th:** Other permissions (read, write, execute)

Example:  
`-rw-rw-r--`  
- `-` : Regular file  
- `rw-` : User can read and write  
- `rw-` : Group can read and write  
- `r--` : Others can only read

See the main [README.md](../README.md) for usage examples.
