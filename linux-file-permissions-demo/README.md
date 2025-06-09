# Linux File Permissions Management

This project demonstrates how to inspect and update file and directory permissions in Linux to comply with organizational security requirements. It includes explanations, command usage, and before-and-after examples.

## Project Description

The research team at my organization needed to update file permissions for certain files and directories within the `projects` directory to better reflect authorization levels and improve security. This project documents the process of checking, explaining, and updating file permissions using Linux commands.

## Tasks Performed

1. **Check file and directory details**  
   Used `ls -la` to list all contents of the `projects` directory, including hidden files, and inspect their permissions.

2. **Describe the permissions string**  
   Explained the 10-character permissions string, including file type and read/write/execute permissions for user, group, and others.

3. **Change file permissions**  
   Used `chmod` to remove write access for "other" on `project_k.txt`.

4. **Change permissions on a hidden file**  
   Removed write permissions from user and group, and ensured read access for the group on `.project_x.txt`.

5. **Change directory permissions**  
   Restricted directory access so that only the `researcher2` user has execute permissions on the `drafts` directory.

## Key Commands Used

```bash
# List file and directory details
ls -la projects

# Remove write permission for "other" on a file
chmod o-w projects/project_k.txt

# Remove write permissions from user and group, add read for group on a hidden file
chmod u-w projects/.project_x.txt
chmod g-w projects/.project_x.txt
chmod g+r projects/.project_x.txt

# Remove execute permissions for group on a directory
chmod g-x projects/drafts
```



## Explanation of Permissions String

The permissions string (e.g. `-rw-rw-r--`) can be interpreted as:

| Position | Meaning                     |
|----------|-----------------------------|
| 1        | File type (`d` for dir, `-` for file) |
| 2-4      | User permissions (r/w/x)    |
| 5-7      | Group permissions (r/w/x)   |
| 8-10     | Other permissions (r/w/x)   |

See [docs/permissions_explanation.md](docs/permissions_explanation.md) for a full breakdown.

## Summary

This project demonstrates a practical workflow for managing file and directory permissions in Linux, providing a basis for secure file management in multi-user environments.

---
