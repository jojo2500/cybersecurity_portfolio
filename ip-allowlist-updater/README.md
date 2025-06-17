# IP Allow List Updater

## Project Description
As a security professional at a healthcare company, I developed a Python algorithm to manage IP address access to restricted patient records. The script compares an allow list of permitted IP addresses against a remove list and automatically updates the allow list file by removing any IPs found in the remove list. This ensures only authorized personnel maintain access to sensitive data.

## Features
- Secure file handling with Python context managers
- Efficient comparison of allow and remove lists
- Simple, readable Python implementation
- Easily extensible for larger access control systems

## Usage

1. **Prepare `allow_list.txt`**:  
   List each allowed IP address on its own line.

2. **Prepare `remove_list.txt`**:  
   List each IP address to revoke, one per line.

3. **Run the script:**  
   ```bash
   python update_allow_list.py
   ```

4. **Result:**  
   The `allow_list.txt` file will be updated, removing any IPs listed in `remove_list.txt`.

## Files
- `update_allow_list.py` — Main Python script
- `allow_list.txt` — Example list of allowed IPs
- `remove_list.txt` — Example list of IPs to remove
- `example_run.md` — Example input, output, and explanation

## Example
See `example_run.md` for a full demonstration.

---
