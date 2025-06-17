# Example Run

## Original `allow_list.txt`
```
192.168.0.10
10.0.0.2
172.16.0.5
192.168.1.22
```

## `remove_list.txt`
```
192.168.0.10
10.0.0.2
```

## After running the script

### Updated `allow_list.txt`
```
172.16.0.5
192.168.1.22
```

---

## Step-by-Step Algorithm Explanation

1. **Open `allow_list.txt` and read the contents as a list of IP addresses.**
2. **Open `remove_list.txt` and read the contents as a list of IP addresses to remove.**
3. **Iterate through each IP in the remove list:**
   - If the IP exists in the allow list, remove it.
4. **Write the updated allow list back to `allow_list.txt`.**
